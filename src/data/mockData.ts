import { RouteWeight, ScraperSourceStatus, CPIIndexPoint, FlightFare, OutlierRecord, AirlineCode, ScrapingSource, LeadTimeHorizon } from '../types';

// Top Indian Air Corridors based on DGCA Passenger Traffic Data & MoSPI Weighting Matrix
export const MOCK_ROUTE_WEIGHTS: RouteWeight[] = [
  {
    corridorId: 'DEL-BOM',
    origin: 'DEL',
    destination: 'BOM',
    corridorName: 'Delhi (DEL) ↔ Mumbai (BOM)',
    annualPassengersMillions: 7.25,
    weightPercentage: 14.8,
    tierCategory: 'METRO_METRO',
    baseYearPrice: 4850
  },
  {
    corridorId: 'BLR-DEL',
    origin: 'BLR',
    destination: 'DEL',
    corridorName: 'Bengaluru (BLR) ↔ Delhi (DEL)',
    annualPassengersMillions: 5.40,
    weightPercentage: 11.0,
    tierCategory: 'METRO_METRO',
    baseYearPrice: 5120
  },
  {
    corridorId: 'BOM-BLR',
    origin: 'BOM',
    destination: 'BLR',
    corridorName: 'Mumbai (BOM) ↔ Bengaluru (BLR)',
    annualPassengersMillions: 4.80,
    weightPercentage: 9.8,
    tierCategory: 'METRO_METRO',
    baseYearPrice: 3950
  },
  {
    corridorId: 'CCU-DEL',
    origin: 'CCU',
    destination: 'DEL',
    corridorName: 'Kolkata (CCU) ↔ Delhi (DEL)',
    annualPassengersMillions: 3.90,
    weightPercentage: 7.9,
    tierCategory: 'METRO_METRO',
    baseYearPrice: 5400
  },
  {
    corridorId: 'HYD-DEL',
    origin: 'HYD',
    destination: 'DEL',
    corridorName: 'Hyderabad (HYD) ↔ Delhi (DEL)',
    annualPassengersMillions: 3.65,
    weightPercentage: 7.4,
    tierCategory: 'METRO_METRO',
    baseYearPrice: 4680
  },
  {
    corridorId: 'MAA-DEL',
    origin: 'MAA',
    destination: 'DEL',
    corridorName: 'Chennai (MAA) ↔ Delhi (DEL)',
    annualPassengersMillions: 3.20,
    weightPercentage: 6.5,
    tierCategory: 'METRO_METRO',
    baseYearPrice: 5290
  },
  {
    corridorId: 'DEL-PNQ',
    origin: 'DEL',
    destination: 'PNQ',
    corridorName: 'Delhi (DEL) ↔ Pune (PNQ)',
    annualPassengersMillions: 2.80,
    weightPercentage: 5.7,
    tierCategory: 'METRO_TIER2',
    baseYearPrice: 4410
  },
  {
    corridorId: 'DEL-AMD',
    origin: 'DEL',
    destination: 'AMD',
    corridorName: 'Delhi (DEL) ↔ Ahmedabad (AMD)',
    annualPassengersMillions: 2.50,
    weightPercentage: 5.1,
    tierCategory: 'METRO_TIER2',
    baseYearPrice: 3820
  },
  {
    corridorId: 'DEL-GAU',
    origin: 'DEL',
    destination: 'GAU',
    corridorName: 'Delhi (DEL) ↔ Guwahati (GAU)',
    annualPassengersMillions: 1.95,
    weightPercentage: 4.0,
    tierCategory: 'METRO_TIER2',
    baseYearPrice: 6150
  },
  {
    corridorId: 'BOM-GOI',
    origin: 'BOM',
    destination: 'GOI',
    corridorName: 'Mumbai (BOM) ↔ Goa (GOI)',
    annualPassengersMillions: 2.20,
    weightPercentage: 4.5,
    tierCategory: 'METRO_TIER2',
    baseYearPrice: 3450
  },
  {
    corridorId: 'DEL-IXR',
    origin: 'DEL',
    destination: 'IXR',
    corridorName: 'Delhi (DEL) ↔ Ranchi (IXR) [UDAN]',
    annualPassengersMillions: 1.10,
    weightPercentage: 2.2,
    tierCategory: 'UDAN_REGIONAL',
    baseYearPrice: 4200
  },
  {
    corridorId: 'BOM-PAT',
    origin: 'BOM',
    destination: 'PAT',
    corridorName: 'Mumbai (BOM) ↔ Patna (PAT) [UDAN]',
    annualPassengersMillions: 1.25,
    weightPercentage: 2.5,
    tierCategory: 'UDAN_REGIONAL',
    baseYearPrice: 5800
  }
];

// Scraping Engine Source Health Statuses
export const MOCK_SCRAPER_SOURCES: ScraperSourceStatus[] = [
  {
    id: 'src-1',
    name: 'INDIGO_DIRECT',
    displayName: 'IndiGo Official Portal (goindigo.in)',
    type: 'AIRLINE_DIRECT',
    status: 'ONLINE',
    latencyMs: 340,
    successRate: 99.6,
    recordsExtracted24h: 14280,
    lastSyncTime: 'Just now (10s ago)',
    bypassStrategy: 'STEALTH_PLAYWRIGHT',
    activeProxies: 32
  },
  {
    id: 'src-2',
    name: 'AIR_INDIA_DIRECT',
    displayName: 'Air India Web Direct (airindia.com)',
    type: 'AIRLINE_DIRECT',
    status: 'ONLINE',
    latencyMs: 410,
    successRate: 98.9,
    recordsExtracted24h: 11450,
    lastSyncTime: 'Just now (15s ago)',
    bypassStrategy: 'API_INTERCEPT',
    activeProxies: 28
  },
  {
    id: 'src-3',
    name: 'MAKEMYTRIP',
    displayName: 'MakeMyTrip OTA (makemytrip.com)',
    type: 'OTA_AGGREGATOR',
    status: 'ONLINE',
    latencyMs: 290,
    successRate: 99.8,
    recordsExtracted24h: 28400,
    lastSyncTime: 'Just now (5s ago)',
    bypassStrategy: 'API_INTERCEPT',
    activeProxies: 45
  },
  {
    id: 'src-4',
    name: 'EASEMYTRIP',
    displayName: 'EaseMyTrip OTA (easemytrip.com)',
    type: 'OTA_AGGREGATOR',
    status: 'ONLINE',
    latencyMs: 220,
    successRate: 99.9,
    recordsExtracted24h: 19800,
    lastSyncTime: 'Just now (8s ago)',
    bypassStrategy: 'RESILIENT_DOM_PARSER',
    activeProxies: 20
  },
  {
    id: 'src-5',
    name: 'YATRA',
    displayName: 'Yatra Online (yatra.com)',
    type: 'OTA_AGGREGATOR',
    status: 'DEGRADED',
    latencyMs: 890,
    successRate: 94.2,
    recordsExtracted24h: 8200,
    lastSyncTime: '2 mins ago',
    bypassStrategy: 'STEALTH_PLAYWRIGHT',
    activeProxies: 15
  }
];

// Historical Airfare CPI Series (Monthly & Daily Data) for MoSPI Comparison
export const MOCK_CPI_HISTORICAL: CPIIndexPoint[] = [
  { date: '2025-10', periodLabel: 'Oct 2025', jevonsIndex: 100.0, dutotIndex: 100.0, weightedLaspeyresIndex: 100.0, officialMoSPICPIBaseline: 100.0, sampleCount: 14200, leadTimeFilter: 'ALL', yoyInflationRate: 4.2, momInflationRate: 0.0 },
  { date: '2025-11', periodLabel: 'Nov 2025', jevonsIndex: 102.3, dutotIndex: 102.8, weightedLaspeyresIndex: 102.1, officialMoSPICPIBaseline: 101.8, sampleCount: 15800, leadTimeFilter: 'ALL', yoyInflationRate: 4.8, momInflationRate: 2.1 },
  { date: '2025-12', periodLabel: 'Dec 2025', jevonsIndex: 114.5, dutotIndex: 116.2, weightedLaspeyresIndex: 115.2, officialMoSPICPIBaseline: 112.5, sampleCount: 18400, leadTimeFilter: 'ALL', yoyInflationRate: 8.9, momInflationRate: 12.8 },
  { date: '2026-01', periodLabel: 'Jan 2026', jevonsIndex: 106.8, dutotIndex: 107.5, weightedLaspeyresIndex: 106.2, officialMoSPICPIBaseline: 105.4, sampleCount: 16200, leadTimeFilter: 'ALL', yoyInflationRate: 5.1, momInflationRate: -6.7 },
  { date: '2026-02', periodLabel: 'Feb 2026', jevonsIndex: 103.4, dutotIndex: 104.1, weightedLaspeyresIndex: 103.1, officialMoSPICPIBaseline: 102.9, sampleCount: 17100, leadTimeFilter: 'ALL', yoyInflationRate: 4.5, momInflationRate: -3.2 },
  { date: '2026-03', periodLabel: 'Mar 2026', jevonsIndex: 105.1, dutotIndex: 105.8, weightedLaspeyresIndex: 104.9, officialMoSPICPIBaseline: 104.2, sampleCount: 16900, leadTimeFilter: 'ALL', yoyInflationRate: 5.3, momInflationRate: 1.6 },
  { date: '2026-04', periodLabel: 'Apr 2026', jevonsIndex: 108.9, dutotIndex: 109.8, weightedLaspeyresIndex: 108.5, officialMoSPICPIBaseline: 107.6, sampleCount: 19200, leadTimeFilter: 'ALL', yoyInflationRate: 6.7, momInflationRate: 3.6 },
  { date: '2026-05', periodLabel: 'May 2026', jevonsIndex: 118.2, dutotIndex: 120.4, weightedLaspeyresIndex: 117.8, officialMoSPICPIBaseline: 115.0, sampleCount: 22100, leadTimeFilter: 'ALL', yoyInflationRate: 9.8, momInflationRate: 8.5 },
  { date: '2026-06', periodLabel: 'Jun 2026', jevonsIndex: 112.6, dutotIndex: 113.9, weightedLaspeyresIndex: 112.1, officialMoSPICPIBaseline: 110.8, sampleCount: 20500, leadTimeFilter: 'ALL', yoyInflationRate: 7.2, momInflationRate: -4.7 },
  { date: '2026-07', periodLabel: 'Jul 2026', jevonsIndex: 107.4, dutotIndex: 108.1, weightedLaspeyresIndex: 107.0, officialMoSPICPIBaseline: 106.5, sampleCount: 18900, leadTimeFilter: 'ALL', yoyInflationRate: 5.4, momInflationRate: -4.6 },
  { date: '2026-08', periodLabel: 'Aug 2026', jevonsIndex: 109.8, dutotIndex: 110.6, weightedLaspeyresIndex: 109.4, officialMoSPICPIBaseline: 108.2, sampleCount: 21400, leadTimeFilter: 'ALL', yoyInflationRate: 6.1, momInflationRate: 2.2 },
  { date: '2026-09', periodLabel: 'Sep 2026 (Live)', jevonsIndex: 111.4, dutotIndex: 112.5, weightedLaspeyresIndex: 111.0, officialMoSPICPIBaseline: 109.5, sampleCount: 24850, leadTimeFilter: 'ALL', yoyInflationRate: 6.9, momInflationRate: 1.5 },
];

// Sample Outliers Detected & Excluded by Algorithm
export const MOCK_OUTLIERS: OutlierRecord[] = [
  {
    id: 'out-101',
    flightNumber: '6E-2041',
    corridor: 'DEL ↔ BOM',
    airline: 'IndiGo',
    observedFare: 24500,
    expectedRouteMedianFare: 5200,
    zScore: 4.82,
    iqrBounds: [3200, 7800],
    action: 'EXCLUDED_FROM_INDEX',
    reason: 'LAST_MINUTE_SCALPING',
    timestamp: '2026-09-06 18:45:12'
  },
  {
    id: 'out-102',
    flightNumber: 'AI-805',
    corridor: 'BLR ↔ DEL',
    airline: 'Air India',
    observedFare: 38900,
    expectedRouteMedianFare: 5400,
    zScore: 6.15,
    iqrBounds: [3400, 8100],
    action: 'EXCLUDED_FROM_INDEX',
    reason: 'FIRST_CLASS_ANOMALY',
    timestamp: '2026-09-06 17:30:05'
  },
  {
    id: 'out-103',
    flightNumber: 'QP-1302',
    corridor: 'BOM ↔ BLR',
    airline: 'Akasa Air',
    observedFare: 1450,
    expectedRouteMedianFare: 4100,
    zScore: -3.21,
    iqrBounds: [2800, 6200],
    action: 'ADJUSTED',
    reason: 'PROMOTIONAL_DISCOUNT',
    timestamp: '2026-09-06 16:10:44'
  },
  {
    id: 'out-104',
    flightNumber: 'SG-8191',
    corridor: 'CCU ↔ DEL',
    airline: 'SpiceJet',
    observedFare: 19800,
    expectedRouteMedianFare: 5600,
    zScore: 3.75,
    iqrBounds: [3600, 8400],
    action: 'EXCLUDED_FROM_INDEX',
    reason: 'FLEXI_SURGE_PRICING',
    timestamp: '2026-09-06 15:22:00'
  }
];

// Helper to generate simulated live scraped flights across Indian routes
export const generateLiveScrapedFares = (): FlightFare[] => {
  const airlines: { code: AirlineCode; name: string }[] = [
    { code: 'INDIGO', name: 'IndiGo' },
    { code: 'AIR_INDIA', name: 'Air India' },
    { code: 'AKASA', name: 'Akasa Air' },
    { code: 'SPICEJET', name: 'SpiceJet' }
  ];

  const sources: ScrapingSource[] = ['INDIGO_DIRECT', 'AIR_INDIA_DIRECT', 'MAKEMYTRIP', 'EASEMYTRIP', 'YATRA'];
  const horizons: LeadTimeHorizon[] = ['1d', '7d', '15d', '30d', '45d'];

  const results: FlightFare[] = [];

  MOCK_ROUTE_WEIGHTS.forEach((route, rIdx) => {
    horizons.forEach(horizon => {
      // Add multiplier based on lead time horizon (closer = pricier)
      const horizonMultiplier = horizon === '1d' ? 1.65 : horizon === '7d' ? 1.25 : horizon === '15d' ? 1.05 : horizon === '30d' ? 0.90 : 0.82;

      airlines.forEach((air, aIdx) => {
        const base = Math.round((route.baseYearPrice * horizonMultiplier) * (0.92 + (Math.random() * 0.16)));
        const fuel = Math.round(base * 0.18);
        const userFee = 450;
        const gst = Math.round((base + fuel + userFee) * 0.05);
        const total = base + fuel + userFee + gst;

        results.push({
          id: `fare-${rIdx}-${horizon}-${aIdx}-${Date.now()}`,
          flightNumber: `${air.code === 'INDIGO' ? '6E' : air.code === 'AIR_INDIA' ? 'AI' : air.code === 'AKASA' ? 'QP' : 'SG'}-${1000 + Math.floor(Math.random() * 8999)}`,
          airline: air.code,
          airlineName: air.name,
          origin: route.origin,
          originName: route.corridorName.split('↔')[0].trim(),
          destination: route.destination,
          destinationName: route.corridorName.split('↔')[1].trim(),
          corridor: route.corridorId,
          departureDate: new Date(Date.now() + (horizon === '1d' ? 86400000 : horizon === '7d' ? 7*86400000 : horizon === '15d' ? 15*86400000 : horizon === '30d' ? 30*86400000 : 45*86400000)).toISOString().split('T')[0],
          scrapingTimestamp: new Date().toISOString(),
          leadTimeHorizon: horizon,
          baseFare: base,
          fuelSurcharge: fuel,
          airportUserFee: userFee,
          gstAndTaxes: gst,
          totalFare: total,
          source: sources[Math.floor(Math.random() * sources.length)],
          cabinClass: 'ECONOMY',
          isRefundable: Math.random() > 0.6,
          seatAvailability: Math.floor(Math.random() * 18) + 2
        });
      });
    });
  });

  return results;
};
