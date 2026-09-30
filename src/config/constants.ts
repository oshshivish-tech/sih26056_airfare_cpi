/**
 * VayuSuchak - Central Configuration & Single Source of Truth
 * Smart India Hackathon 2026 | Problem Statement ID: SIH26056
 * Team Roorkies
 * 
 * Every number, route weight, booking horizon, and base period across the
 * presentation deck, dashboard, and backend engine is strictly defined here.
 */

export interface CorridorConfig {
  corridorId: string;
  origin: string;
  destination: string;
  corridorName: string;
  tierCategory: 'METRO_METRO' | 'METRO_TIER2' | 'UDAN_REGIONAL';
  annualPassengersMillions: number;
  rawDgcaSharePercentage: number;   // Raw % share of total national scheduled domestic passengers
  normalizedWeight: number;          // Rescaled basket weight w_c (sums to exactly 1.0 across 12 corridors)
  normalizedPercentage: number;      // Normalized weight in percentage (sums to 100.0%)
  baseYearPrice: number;             // Baseline reference fare in INR (Oct 2025)
}

export interface HorizonConfig {
  days: number;
  code: '1d' | '7d' | '14d' | '30d' | '45d';
  label: string;
  category: string;
  weightPercentage: number;
  description: string;
}

export interface AirlineConfig {
  code: string;
  name: string;
  marketSharePercentage: number;
  portalUrl: string;
}

// 1. Data Attribution & Source Metadata
export const DATA_METADATA = {
  systemName: 'VayuSuchak',
  tagline: 'Real-time Airfare Price Index for India',
  problemStatementId: 'SIH26056',
  teamName: 'Team Roorkies',
  version: '2.4.0',
  dataStatusBadge: 'Prototype data: Sample',
  dataStatusDescription: 'Calibrated sample flight fare dataset for prototype demonstration; live web collection operates under compliant rate-limited policies.',
  
  // Base Period Definition
  basePeriod: '[FILL: Oct 2025 = 100.0]',
  basePeriodNotes: 'New routes and carriers enter the index via chain-linking at the next January rebase cycle.',
  
  // Official Benchmark Data Sources
  dgcaReportCitation: 'DGCA Scheduled Domestic Passenger Traffic Report [FILL: exact report title + month, e.g., City-Pair Passenger Traffic Dec 2024]',
  mospiGuidelinesCitation: 'MoSPI NSO Consumer Price Index Concepts & Methods (Base 2012=100) Guidelines',
  unIloManualCitation: 'UN, ILO, IMF, OECD, Eurostat, World Bank (2020) Consumer Price Index Manual: Concepts and Methods, Chapter 10: Elementary Indices',
  academicCitationDiewert: 'Diewert, W. E. (2004). Elementary Indices. In Consumer Price Index Theory, IMF Handbook.',
  academicCitationCavallo: 'Cavallo, A., & Rigobon, R. (2016). The Billion Prices Project: Using Online Data for Measurement. Journal of Economic Perspectives, 30(2), 151-178. doi:10.1257/jep.30.2.151'
};

// 2. The 5 Booking Horizons (Strictly T+1, T+7, T+14, T+30, T+45)
export const BOOKING_HORIZONS: HorizonConfig[] = [
  {
    days: 1,
    code: '1d',
    label: 'T+1 Days',
    category: 'Urgent / Emergency',
    weightPercentage: 15.0,
    description: 'Urgent / Emergency Booking (1 Day Out)'
  },
  {
    days: 7,
    code: '7d',
    label: 'T+7 Days',
    category: 'Short-Term / Business',
    weightPercentage: 30.0,
    description: 'Short-Term / Business Booking (7 Days Out)'
  },
  {
    days: 14,
    code: '14d',
    label: 'T+14 Days',
    category: 'Standard Advance',
    weightPercentage: 35.0,
    description: 'Standard Advance Purchase (14 Days Out)'
  },
  {
    days: 30,
    code: '30d',
    label: 'T+30 Days',
    category: 'Leisure Travel',
    weightPercentage: 15.0,
    description: 'Leisure Travel Booking (30 Days Out)'
  },
  {
    days: 45,
    code: '45d',
    label: 'T+45 Days',
    category: 'Far-Advance / Holiday',
    weightPercentage: 5.0,
    description: 'Far-Advance / Holiday Booking (45 Days Out)'
  }
];

// 3. Target Carriers
export const TARGET_AIRLINES: AirlineConfig[] = [
  { code: '6E', name: 'IndiGo', marketSharePercentage: 62.5, portalUrl: 'https://www.goindigo.in' },
  { code: 'AI', name: 'Air India Group', marketSharePercentage: 26.8, portalUrl: 'https://www.airindia.com' },
  { code: 'SG', name: 'SpiceJet', marketSharePercentage: 4.2, portalUrl: 'https://www.spicejet.com' },
  { code: 'QP', name: 'Akasa Air', marketSharePercentage: 4.8, portalUrl: 'https://www.akasaair.com' }
];

// 4. 12 Representative Corridors & DGCA Weighting Matrix
// Raw DGCA national share sums to 81.4%. Normalized basket weight w_c sums to exactly 1.000 (100.0%).
export const REPRESENTATIVE_CORRIDORS: CorridorConfig[] = [
  {
    corridorId: 'DEL-BOM',
    origin: 'DEL',
    destination: 'BOM',
    corridorName: 'Delhi (DEL) ↔ Mumbai (BOM)',
    tierCategory: 'METRO_METRO',
    annualPassengersMillions: 7.25,
    rawDgcaSharePercentage: 14.8,
    normalizedWeight: 0.1818,
    normalizedPercentage: 18.2,
    baseYearPrice: 4850
  },
  {
    corridorId: 'BLR-DEL',
    origin: 'BLR',
    destination: 'DEL',
    corridorName: 'Bengaluru (BLR) ↔ Delhi (DEL)',
    tierCategory: 'METRO_METRO',
    annualPassengersMillions: 5.40,
    rawDgcaSharePercentage: 11.0,
    normalizedWeight: 0.1351,
    normalizedPercentage: 13.5,
    baseYearPrice: 5120
  },
  {
    corridorId: 'BOM-BLR',
    origin: 'BOM',
    destination: 'BLR',
    corridorName: 'Mumbai (BOM) ↔ Bengaluru (BLR)',
    tierCategory: 'METRO_METRO',
    annualPassengersMillions: 4.80,
    rawDgcaSharePercentage: 9.8,
    normalizedWeight: 0.1204,
    normalizedPercentage: 12.0,
    baseYearPrice: 3950
  },
  {
    corridorId: 'CCU-DEL',
    origin: 'CCU',
    destination: 'DEL',
    corridorName: 'Kolkata (CCU) ↔ Delhi (DEL)',
    tierCategory: 'METRO_METRO',
    annualPassengersMillions: 3.90,
    rawDgcaSharePercentage: 7.9,
    normalizedWeight: 0.0971,
    normalizedPercentage: 9.7,
    baseYearPrice: 5400
  },
  {
    corridorId: 'HYD-DEL',
    origin: 'HYD',
    destination: 'DEL',
    corridorName: 'Hyderabad (HYD) ↔ Delhi (DEL)',
    tierCategory: 'METRO_METRO',
    annualPassengersMillions: 3.65,
    rawDgcaSharePercentage: 7.4,
    normalizedWeight: 0.0909,
    normalizedPercentage: 9.1,
    baseYearPrice: 4680
  },
  {
    corridorId: 'MAA-DEL',
    origin: 'MAA',
    destination: 'DEL',
    corridorName: 'Chennai (MAA) ↔ Delhi (DEL)',
    tierCategory: 'METRO_METRO',
    annualPassengersMillions: 3.20,
    rawDgcaSharePercentage: 6.5,
    normalizedWeight: 0.0799,
    normalizedPercentage: 8.0,
    baseYearPrice: 5290
  },
  {
    corridorId: 'DEL-PNQ',
    origin: 'DEL',
    destination: 'PNQ',
    corridorName: 'Delhi (DEL) ↔ Pune (PNQ)',
    tierCategory: 'METRO_TIER2',
    annualPassengersMillions: 2.80,
    rawDgcaSharePercentage: 5.7,
    normalizedWeight: 0.0700,
    normalizedPercentage: 7.0,
    baseYearPrice: 4410
  },
  {
    corridorId: 'DEL-AMD',
    origin: 'DEL',
    destination: 'AMD',
    corridorName: 'Delhi (DEL) ↔ Ahmedabad (AMD)',
    tierCategory: 'METRO_TIER2',
    annualPassengersMillions: 2.50,
    rawDgcaSharePercentage: 5.1,
    normalizedWeight: 0.0627,
    normalizedPercentage: 6.3,
    baseYearPrice: 3820
  },
  {
    corridorId: 'BOM-GOI',
    origin: 'BOM',
    destination: 'GOI',
    corridorName: 'Mumbai (BOM) ↔ Goa (GOI)',
    tierCategory: 'METRO_TIER2',
    annualPassengersMillions: 2.20,
    rawDgcaSharePercentage: 4.5,
    normalizedWeight: 0.0553,
    normalizedPercentage: 5.5,
    baseYearPrice: 3450
  },
  {
    corridorId: 'DEL-GAU',
    origin: 'DEL',
    destination: 'GAU',
    corridorName: 'Delhi (DEL) ↔ Guwahati (GAU)',
    tierCategory: 'METRO_TIER2',
    annualPassengersMillions: 1.95,
    rawDgcaSharePercentage: 4.0,
    normalizedWeight: 0.0491,
    normalizedPercentage: 4.9,
    baseYearPrice: 6150
  },
  {
    corridorId: 'BOM-PAT',
    origin: 'BOM',
    destination: 'PAT',
    corridorName: 'Mumbai (BOM) ↔ Patna (PAT) [UDAN]',
    tierCategory: 'UDAN_REGIONAL',
    annualPassengersMillions: 1.25,
    rawDgcaSharePercentage: 2.5,
    normalizedWeight: 0.0307,
    normalizedPercentage: 3.1,
    baseYearPrice: 5800
  },
  {
    corridorId: 'DEL-IXR',
    origin: 'DEL',
    destination: 'IXR',
    corridorName: 'Delhi (DEL) ↔ Ranchi (IXR) [UDAN]',
    tierCategory: 'UDAN_REGIONAL',
    annualPassengersMillions: 1.10,
    rawDgcaSharePercentage: 2.2,
    normalizedWeight: 0.0270,
    normalizedPercentage: 2.7,
    baseYearPrice: 4200
  }
];

// Helper: Verify Normalized Weights Sum to 1.0 (within 1e-4)
export const TOTAL_NORMALIZED_WEIGHT = Number(
  REPRESENTATIVE_CORRIDORS.reduce((acc, c) => acc + c.normalizedWeight, 0).toFixed(4)
);
export const TOTAL_NORMALIZED_PERCENTAGE = Number(
  REPRESENTATIVE_CORRIDORS.reduce((acc, c) => acc + c.normalizedPercentage, 0).toFixed(1)
);
