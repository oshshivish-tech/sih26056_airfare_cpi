"""
VayuSuchak - Central Configuration & Single Source of Truth (Backend)
Smart India Hackathon 2026 | Problem Statement ID: SIH26056
Team Roorkies

Identical parameters, weights, and horizons mirroring src/config/constants.ts
"""

from typing import Dict, List, Any

DATA_METADATA = {
    "system_name": "VayuSuchak",
    "problem_statement_id": "SIH26056",
    "team_name": "Team Roorkies",
    "base_period": "October 2025 = 100.0",
    "dgca_report_citation": "DGCA Scheduled Domestic Passenger Traffic Report, December 2024 (Table 3.2: City-Pair Passenger Traffic)",
    "user_agent": "VayuSuchak-Research-Bot/1.0 (+https://sih26056-airfare-cpi.vercel.app; research-contact@roorkies.edu)",
}

# The 5 Booking Horizons (Strictly T+1, T+7, T+14, T+30, T+45)
BOOKING_HORIZONS: List[Dict[str, Any]] = [
    {"days": 1, "code": "1d", "label": "T+1 Days", "category": "Urgent", "weight_pct": 15.0},
    {"days": 7, "code": "7d", "label": "T+7 Days", "category": "Short-Term", "weight_pct": 30.0},
    {"days": 14, "code": "14d", "label": "T+14 Days", "category": "Standard", "weight_pct": 35.0},
    {"days": 30, "code": "30d", "label": "T+30 Days", "category": "Leisure", "weight_pct": 15.0},
    {"days": 45, "code": "45d", "label": "T+45 Days", "category": "Far-Advance", "weight_pct": 5.0},
]

# 12 Representative Corridors & DGCA Weighting Matrix
# Raw DGCA national share sums to 81.4%. Normalized basket weight w_c sums to exactly 1.000 (100.0%).
REPRESENTATIVE_CORRIDORS: Dict[str, Dict[str, Any]] = {
    "DEL-BOM": {
        "name": "Delhi ↔ Mumbai",
        "origin": "DEL",
        "destination": "BOM",
        "tier": "METRO_METRO",
        "annual_pax_millions": 7.25,
        "raw_dgca_share_pct": 14.8,
        "normalized_weight": 0.1818,
        "normalized_pct": 18.2,
        "base_year_price": 4850,
    },
    "BLR-DEL": {
        "name": "Bengaluru ↔ Delhi",
        "origin": "BLR",
        "destination": "DEL",
        "tier": "METRO_METRO",
        "annual_pax_millions": 5.40,
        "raw_dgca_share_pct": 11.0,
        "normalized_weight": 0.1351,
        "normalized_pct": 13.5,
        "base_year_price": 5120,
    },
    "BOM-BLR": {
        "name": "Mumbai ↔ Bengaluru",
        "origin": "BOM",
        "destination": "BLR",
        "tier": "METRO_METRO",
        "annual_pax_millions": 4.80,
        "raw_dgca_share_pct": 9.8,
        "normalized_weight": 0.1204,
        "normalized_pct": 12.0,
        "base_year_price": 3950,
    },
    "CCU-DEL": {
        "name": "Kolkata ↔ Delhi",
        "origin": "CCU",
        "destination": "DEL",
        "tier": "METRO_METRO",
        "annual_pax_millions": 3.90,
        "raw_dgca_share_pct": 7.9,
        "normalized_weight": 0.0971,
        "normalized_pct": 9.7,
        "base_year_price": 5400,
    },
    "HYD-DEL": {
        "name": "Hyderabad ↔ Delhi",
        "origin": "HYD",
        "destination": "DEL",
        "tier": "METRO_METRO",
        "annual_pax_millions": 3.65,
        "raw_dgca_share_pct": 7.4,
        "normalized_weight": 0.0909,
        "normalized_pct": 9.1,
        "base_year_price": 4680,
    },
    "MAA-DEL": {
        "name": "Chennai ↔ Delhi",
        "origin": "MAA",
        "destination": "DEL",
        "tier": "METRO_METRO",
        "annual_pax_millions": 3.20,
        "raw_dgca_share_pct": 6.5,
        "normalized_weight": 0.0799,
        "normalized_pct": 8.0,
        "base_year_price": 5290,
    },
    "DEL-PNQ": {
        "name": "Delhi ↔ Pune",
        "origin": "DEL",
        "destination": "PNQ",
        "tier": "METRO_TIER2",
        "annual_pax_millions": 2.80,
        "raw_dgca_share_pct": 5.7,
        "normalized_weight": 0.0700,
        "normalized_pct": 7.0,
        "base_year_price": 4410,
    },
    "DEL-AMD": {
        "name": "Delhi ↔ Ahmedabad",
        "origin": "DEL",
        "destination": "AMD",
        "tier": "METRO_TIER2",
        "annual_pax_millions": 2.50,
        "raw_dgca_share_pct": 5.1,
        "normalized_weight": 0.0627,
        "normalized_pct": 6.3,
        "base_year_price": 3820,
    },
    "BOM-GOI": {
        "name": "Mumbai ↔ Goa",
        "origin": "BOM",
        "destination": "GOI",
        "tier": "METRO_TIER2",
        "annual_pax_millions": 2.20,
        "raw_dgca_share_pct": 4.5,
        "normalized_weight": 0.0553,
        "normalized_pct": 5.5,
        "base_year_price": 3450,
    },
    "DEL-GAU": {
        "name": "Delhi ↔ Guwahati",
        "origin": "DEL",
        "destination": "GAU",
        "tier": "METRO_TIER2",
        "annual_pax_millions": 1.95,
        "raw_dgca_share_pct": 4.0,
        "normalized_weight": 0.0491,
        "normalized_pct": 4.9,
        "base_year_price": 6150,
    },
    "BOM-PAT": {
        "name": "Mumbai ↔ Patna",
        "origin": "BOM",
        "destination": "PAT",
        "tier": "UDAN_REGIONAL",
        "annual_pax_millions": 1.25,
        "raw_dgca_share_pct": 2.5,
        "normalized_weight": 0.0307,
        "normalized_pct": 3.1,
        "base_year_price": 5800,
    },
    "DEL-IXR": {
        "name": "Delhi ↔ Ranchi",
        "origin": "DEL",
        "destination": "IXR",
        "tier": "UDAN_REGIONAL",
        "annual_pax_millions": 1.10,
        "raw_dgca_share_pct": 2.2,
        "normalized_weight": 0.0270,
        "normalized_pct": 2.7,
        "base_year_price": 4200,
    },
}

TOTAL_NORMALIZED_WEIGHT = round(sum(c["normalized_weight"] for c in REPRESENTATIVE_CORRIDORS.values()), 4)
TOTAL_NORMALIZED_PCT = round(sum(c["normalized_pct"] for c in REPRESENTATIVE_CORRIDORS.values()), 1)
