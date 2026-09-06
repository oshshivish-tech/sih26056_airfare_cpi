"""
MoSPI Airfare CPI Engine (SIH Problem Statement 26056)
Standalone Python Data Pipeline & Scraper CLI

Usage:
    python scraper_cli.py --corridor DEL-BOM --lead-days 7 --calculate-index
"""

import json
import math
import argparse
from datetime import datetime, timedelta
import random

# DGCA Top Corridors and Passenger Volume Weights
DGCA_ROUTE_WEIGHTS = {
    "DEL-BOM": {"name": "Delhi ↔ Mumbai", "weight": 0.148, "base_price": 4850},
    "BLR-DEL": {"name": "Bengaluru ↔ Delhi", "weight": 0.110, "base_price": 5120},
    "BOM-BLR": {"name": "Mumbai ↔ Bengaluru", "weight": 0.098, "base_price": 3950},
    "CCU-DEL": {"name": "Kolkata ↔ Delhi", "weight": 0.079, "base_price": 5400},
    "HYD-DEL": {"name": "Hyderabad ↔ Delhi", "weight": 0.074, "base_price": 4680},
    "MAA-DEL": {"name": "Chennai ↔ Delhi", "weight": 0.065, "base_price": 5290},
    "DEL-PNQ": {"name": "Delhi ↔ Pune", "weight": 0.057, "base_price": 4410},
    "DEL-AMD": {"name": "Delhi ↔ Ahmedabad", "weight": 0.051, "base_price": 3820},
    "DEL-GAU": {"name": "Delhi ↔ Guwahati", "weight": 0.040, "base_price": 6150},
    "BOM-GOI": {"name": "Mumbai ↔ Goa", "weight": 0.045, "base_price": 3450},
}

class JevonsCPIEngine:
    """
    Implements UN/ILO Jevons Geometric Mean Index calculation
    Formula: I_Jevons = exp( (1/N) * sum( ln( P_t / P_0 ) ) ) * 100
    """
    @staticmethod
    def compute_jevons(quotes: list) -> float:
        if not quotes:
            return 100.0
        log_sum = sum(math.log(q["current_price"] / q["base_price"]) for q in quotes)
        mean_log = log_sum / len(quotes)
        return round(math.exp(mean_log) * 100, 2)

    @staticmethod
    def compute_weighted_laspeyres(route_averages: dict) -> float:
        """
        Formula: I_Weighted = sum( w_c * ( P_c,t / P_c,0 ) ) * 100
        """
        total_weighted_rel = 0.0
        total_weight = 0.0
        for route_id, avg_price in route_averages.items():
            if route_id in DGCA_ROUTE_WEIGHTS:
                info = DGCA_ROUTE_WEIGHTS[route_id]
                rel = avg_price / info["base_price"]
                total_weighted_rel += info["weight"] * rel
                total_weight += info["weight"]
        
        if total_weight == 0:
            return 100.0
        return round((total_weighted_rel / total_weight) * 100, 2)

def simulate_airfare_scrape(corridor: str, lead_days: int) -> list:
    """Simulates real-time price extraction for a given corridor and lead window."""
    airlines = ["IndiGo", "Air India", "Akasa Air", "SpiceJet"]
    quotes = []
    base_info = DGCA_ROUTE_WEIGHTS.get(corridor, {"base_price": 5000})
    
    multiplier = 1.65 if lead_days <= 1 else 1.25 if lead_days <= 7 else 1.05 if lead_days <= 14 else 0.90
    
    for air in airlines:
        fare = round(base_info["base_price"] * multiplier * random.uniform(0.92, 1.15))
        quotes.append({
            "corridor": corridor,
            "airline": air,
            "lead_days": lead_days,
            "base_price": base_info["base_price"],
            "current_price": fare,
            "scraped_at": datetime.now().isoformat()
        })
    return quotes

def main():
    parser = argparse.ArgumentParser(description="MoSPI Airfare CPI Engine (SIH 26056)")
    parser.add_argument("--corridor", type=str, default="DEL-BOM", help="Flight corridor ID")
    parser.add_argument("--lead-days", type=int, default=7, help="Advance purchase horizon (1, 7, 14, 30)")
    parser.add_argument("--calculate-index", action="store_true", help="Run full national CPI calculation")

    args = parser.parse_args()

    print("=" * 60)
    print("  MoSPI Airfare CPI Engine (SIH Problem Statement 26056)")
    print("  National Statistical Office (NSO) Augmentation CLI")
    print("=" * 60)

    if args.calculate_index:
        all_quotes = []
        route_averages = {}
        for corridor in DGCA_ROUTE_WEIGHTS.keys():
            quotes = simulate_airfare_scrape(corridor, args.lead_days)
            all_quotes.extend(quotes)
            avg_fare = sum(q["current_price"] for q in quotes) / len(quotes)
            route_averages[corridor] = avg_fare

        jevons = JevonsCPIEngine.compute_jevons(all_quotes)
        laspeyres = JevonsCPIEngine.compute_weighted_laspeyres(route_averages)

        print(f"\n[+] Total Airfare Quotes Scraped Across India: {len(all_quotes)}")
        print(f"[+] Jevons Geometric Mean Index (UN/ILO Standard): {jevons} (Base 2025=100)")
        print(f"[+] DGCA Passenger Volume Weighted Laspeyres Index: {laspeyres} (Base 2025=100)")
        print(f"[+] Estimated YoY Airfare Inflation: +{round(jevons - 100, 2)}%\n")
    else:
        quotes = simulate_airfare_scrape(args.corridor, args.lead_days)
        print(f"\nScraped quotes for {args.corridor} ({args.lead_days}-day lead time):")
        print(json.dumps(quotes, indent=2))

if __name__ == "__main__":
    main()
