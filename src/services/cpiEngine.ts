import { FlightFare, RouteWeight, CPIIndexPoint, LeadTimeHorizon, OutlierRecord } from '../types';
import { MOCK_ROUTE_WEIGHTS } from '../data/mockData';

export interface CPIComputationResult {
  jevonsIndex: number;
  dutotIndex: number;
  weightedLaspeyresIndex: number;
  sampleCount: number;
  excludedOutliersCount: number;
  corridorBreakdown: Record<string, { avgFare: number; priceRelative: number; weight: number }>;
}

export class MoSPICPIEngine {
  /**
   * Filters raw flight fare sample data using Interquartile Range (IQR) outlier pruning
   */
  static filterOutliers(fares: FlightFare[]): { cleanFares: FlightFare[]; outliers: OutlierRecord[] } {
    const cleanFares: FlightFare[] = [];
    const outliers: OutlierRecord[] = [];

    // Group fares by corridor to find route-specific IQR bounds
    const groupedByCorridor: Record<string, FlightFare[]> = {};
    fares.forEach(f => {
      if (!groupedByCorridor[f.corridor]) {
        groupedByCorridor[f.corridor] = [];
      }
      groupedByCorridor[f.corridor].push(f);
    });

    Object.entries(groupedByCorridor).forEach(([corridorId, corridorFares]) => {
      const sortedPrices = corridorFares.map(f => f.totalFare).sort((a, b) => a - b);
      const q1Index = Math.floor(sortedPrices.length * 0.25);
      const q3Index = Math.floor(sortedPrices.length * 0.75);
      
      const q1 = sortedPrices[q1Index] || sortedPrices[0];
      const q3 = sortedPrices[q3Index] || sortedPrices[sortedPrices.length - 1];
      const iqr = q3 - q1;

      const lowerBound = Math.max(800, q1 - 1.5 * iqr);
      const upperBound = q3 + 2.0 * iqr; // Slight tolerance for dynamic pricing

      // Calculate mean & std dev for Z-score
      const mean = sortedPrices.reduce((a, b) => a + b, 0) / sortedPrices.length;
      const stdDev = Math.sqrt(sortedPrices.reduce((sq, n) => sq + Math.pow(n - mean, 2), 0) / sortedPrices.length) || 1;

      corridorFares.forEach(f => {
        const zScore = Number(((f.totalFare - mean) / stdDev).toFixed(2));
        if (f.totalFare < lowerBound || f.totalFare > upperBound) {
          outliers.push({
            id: `out-gen-${f.id}`,
            flightNumber: f.flightNumber,
            corridor: f.corridor,
            airline: f.airlineName,
            observedFare: f.totalFare,
            expectedRouteMedianFare: Math.round(mean),
            zScore,
            iqrBounds: [Math.round(lowerBound), Math.round(upperBound)],
            action: f.totalFare > upperBound ? 'EXCLUDED_FROM_INDEX' : 'ADJUSTED',
            reason: f.totalFare > upperBound ? 'FLEXI_SURGE_PRICING' : 'PROMOTIONAL_DISCOUNT',
            timestamp: f.scrapingTimestamp
          });
          if (f.totalFare <= upperBound) {
            cleanFares.push(f);
          }
        } else {
          cleanFares.push(f);
        }
      });
    });

    return { cleanFares, outliers };
  }

  /**
   * Calculates Jevons Geometric Index, Dutot Index, and Weighted Laspeyres Index
   */
  static calculateIndex(
    fares: FlightFare[],
    routeWeights: RouteWeight[] = MOCK_ROUTE_WEIGHTS,
    leadTimeFilter: LeadTimeHorizon | 'ALL' = 'ALL'
  ): CPIComputationResult {
    const filteredFares = leadTimeFilter === 'ALL'
      ? fares
      : fares.filter(f => f.leadTimeHorizon === leadTimeFilter);

    const { cleanFares, outliers } = this.filterOutliers(filteredFares);

    if (cleanFares.length === 0) {
      return {
        jevonsIndex: 100.0,
        dutotIndex: 100.0,
        weightedLaspeyresIndex: 100.0,
        sampleCount: 0,
        excludedOutliersCount: outliers.length,
        corridorBreakdown: {}
      };
    }

    // 1. Group clean fares by corridor
    const corridorData: Record<string, number[]> = {};
    cleanFares.forEach(f => {
      if (!corridorData[f.corridor]) corridorData[f.corridor] = [];
      corridorData[f.corridor].push(f.totalFare);
    });

    const corridorBreakdown: Record<string, { avgFare: number; priceRelative: number; weight: number }> = {};
    let totalWeightApplied = 0;
    let weightedLaspeyresSum = 0;
    
    // For Jevons (Geometric Mean of Price Relatives across all quotes)
    let logPriceRelativeSum = 0;
    let totalQuoteCount = 0;

    // For Dutot (Arithmetic Mean of current vs baseline across all quotes)
    let totalCurrentFareSum = 0;
    let totalBaseYearFareSum = 0;

    routeWeights.forEach(rw => {
      const faresForCorridor = corridorData[rw.corridorId] || [rw.baseYearPrice];
      const avgCurrentFare = faresForCorridor.reduce((a, b) => a + b, 0) / faresForCorridor.length;
      const priceRelative = avgCurrentFare / rw.baseYearPrice;

      corridorBreakdown[rw.corridorId] = {
        avgFare: Math.round(avgCurrentFare),
        priceRelative: Number(priceRelative.toFixed(4)),
        weight: rw.weightPercentage
      };

      // Weighted Laspeyres computation
      weightedLaspeyresSum += priceRelative * (rw.weightPercentage / 100);
      totalWeightApplied += (rw.weightPercentage / 100);

      // Accumulate for overall Jevons & Dutot
      faresForCorridor.forEach(p => {
        const rel = p / rw.baseYearPrice;
        logPriceRelativeSum += Math.log(rel);
        totalQuoteCount++;

        totalCurrentFareSum += p;
        totalBaseYearFareSum += rw.baseYearPrice;
      });
    });

    // Final Jevons Index Formula: exp( (1/N) * sum(ln(P_t / P_0)) ) * 100
    const jevonsIndex = Number((Math.exp(logPriceRelativeSum / totalQuoteCount) * 100).toFixed(2));

    // Final Dutot Index Formula: (sum(P_t) / sum(P_0)) * 100
    const dutotIndex = Number(((totalCurrentFareSum / totalBaseYearFareSum) * 100).toFixed(2));

    // Final Weighted Laspeyres Index Formula: sum(w_c * (P_c,t / P_c,0)) * 100
    const weightedLaspeyresIndex = Number(((weightedLaspeyresSum / totalWeightApplied) * 100).toFixed(2));

    return {
      jevonsIndex,
      dutotIndex,
      weightedLaspeyresIndex,
      sampleCount: cleanFares.length,
      excludedOutliersCount: outliers.length,
      corridorBreakdown
    };
  }
}
