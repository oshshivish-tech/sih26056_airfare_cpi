export type LeadTimeHorizon = '1d' | '7d' | '15d' | '30d' | '45d';

export type AirlineCode = 'INDIGO' | 'AIR_INDIA' | 'SPICEJET' | 'AKASA' | 'VISTARA';

export type ScrapingSource = 'INDIGO_DIRECT' | 'AIR_INDIA_DIRECT' | 'MAKEMYTRIP' | 'EASEMYTRIP' | 'YATRA';

export interface FlightFare {
  id: string;
  flightNumber: string;
  airline: AirlineCode;
  airlineName: string;
  origin: string;
  originName: string;
  destination: string;
  destinationName: string;
  corridor: string;
  departureDate: string;
  scrapingTimestamp: string;
  leadTimeHorizon: LeadTimeHorizon;
  baseFare: number;
  fuelSurcharge: number;
  airportUserFee: number;
  gstAndTaxes: number;
  totalFare: number;
  source: ScrapingSource;
  cabinClass: 'ECONOMY' | 'PREMIUM_ECONOMY' | 'BUSINESS';
  isRefundable: boolean;
  seatAvailability: number;
}

export interface RouteWeight {
  corridorId: string;
  origin: string;
  destination: string;
  corridorName: string;
  annualPassengersMillions: number;
  weightPercentage: number; // e.g. 14.5% for DEL-BOM
  tierCategory: 'METRO_METRO' | 'METRO_TIER2' | 'UDAN_REGIONAL';
  baseYearPrice: number; // 2024-25 baseline average fare in INR
}

export interface CPIIndexPoint {
  date: string;
  periodLabel: string;
  jevonsIndex: number; // Geometric Mean (UN/ILO recommended for unweighted item level)
  dutotIndex: number; // Ratio of Arithmetic Means
  weightedLaspeyresIndex: number; // Weighted by DGCA Route Passenger Volume
  officialMoSPICPIBaseline: number; // Official historical manual CPI index for comparison
  sampleCount: number;
  leadTimeFilter: LeadTimeHorizon | 'ALL';
  yoyInflationRate: number; // Percentage
  momInflationRate: number; // Percentage
}

export interface ScraperSourceStatus {
  id: string;
  name: ScrapingSource;
  displayName: string;
  type: 'AIRLINE_DIRECT' | 'OTA_AGGREGATOR';
  status: 'ONLINE' | 'DEGRADED' | 'RATE_LIMITED' | 'OFFLINE';
  latencyMs: number;
  successRate: number; // Percentage e.g. 99.4
  recordsExtracted24h: number;
  lastSyncTime: string;
  bypassStrategy: 'STEALTH_PLAYWRIGHT' | 'API_INTERCEPT' | 'RESILIENT_DOM_PARSER';
  activeProxies: number;
}

export interface OutlierRecord {
  id: string;
  flightNumber: string;
  corridor: string;
  airline: string;
  observedFare: number;
  expectedRouteMedianFare: number;
  zScore: number;
  iqrBounds: [number, number];
  action: 'EXCLUDED_FROM_INDEX' | 'ADJUSTED' | 'RETAINED';
  reason: 'FLEXI_SURGE_PRICING' | 'FIRST_CLASS_ANOMALY' | 'LAST_MINUTE_SCALPING' | 'PROMOTIONAL_DISCOUNT';
  timestamp: string;
}

export interface MoSPIExportReport {
  generatedAt: string;
  baseYear: number;
  currentAirfareIndex: number;
  monthlyInflationChange: number;
  totalRoutesMonitored: number;
  totalDataPointsCollected: number;
  methodologyNotes: string;
  dataSignature: string;
}
