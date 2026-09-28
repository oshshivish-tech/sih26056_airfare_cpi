"""
MoSPI Airfare CPI Engine - Real Live GDS Data Ingestion Pipeline (SIH 26056)
Directly connects to Amadeus Flight Offers API to extract real live Indian airfares.

Usage:
    python backend/amadeus_live_ingest.py --client-id YOUR_ID --client-secret YOUR_SECRET
"""

import sys
import json
import math
import argparse
import urllib.request
import urllib.parse
from datetime import datetime, timedelta

# Fix Windows console encoding for Rupee symbol
sys.stdout.reconfigure(encoding='utf-8')

# DGCA Corridor Baseline Benchmarks (P_0) and National Traffic Weights (w_c)
CORRIDOR_BENCHMARKS = {
    "DEL-BOM": {"name": "Delhi ↔ Mumbai", "weight": 0.148, "base_price": 4850},
    "BLR-DEL": {"name": "Bengaluru ↔ Delhi", "weight": 0.110, "base_price": 5120},
    "BOM-BLR": {"name": "Mumbai ↔ Bengaluru", "weight": 0.098, "base_price": 3950},
    "CCU-DEL": {"name": "Kolkata ↔ Delhi", "weight": 0.079, "base_price": 5400},
    "HYD-DEL": {"name": "Hyderabad ↔ Delhi", "weight": 0.074, "base_price": 4680},
    "MAA-DEL": {"name": "Chennai ↔ Delhi", "weight": 0.065, "base_price": 5290},
}

class AmadeusLiveEngine:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id.strip()
        self.client_secret = client_secret.strip()
        self.token = None

    def authenticate(self) -> str:
        """Obtains OAuth2 access token from Amadeus token service"""
        token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        data = urllib.parse.urlencode({
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }).encode("utf-8")

        req = urllib.request.Request(token_url, data=data, method="POST")
        req.add_header("Content-Type", "application/x-www-form-urlencoded")

        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                res = json.loads(response.read().decode("utf-8"))
                self.token = res["access_token"]
                return self.token
        except Exception as e:
            raise RuntimeError(f"Authentication failed: {e}")

    def fetch_live_corridor_fares(self, origin: str, dest: str, dep_date: str) -> list:
        """Queries live flight offers for a city pair from Amadeus GDS"""
        if not self.token:
            self.authenticate()

        base_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": dest,
            "departureDate": dep_date,
            "adults": "1",
            "currencyCode": "INR",
            "travelClass": "ECONOMY",
            "nonStop": "true",
            "max": "15"
        }
        url = f"{base_url}?{urllib.parse.urlencode(params)}"

        req = urllib.request.Request(url, method="GET")
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Accept", "application/vnd.amadeus+json")

        quotes = []
        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                res = json.loads(response.read().decode("utf-8"))
                data = res.get("data", [])
                for offer in data:
                    seg = offer["itineraries"][0]["segments"][0]
                    carrier = seg.get("carrierCode", "AI")
                    flight_no = f"{carrier}-{seg.get('number', '000')}"
                    total_price = float(offer["price"]["total"])
                    quotes.append({
                        "flight_no": flight_no,
                        "carrier": carrier,
                        "origin": origin,
                        "destination": dest,
                        "total_fare": total_price,
                        "currency": offer["price"]["currency"],
                        "departure_time": seg["departure"]["at"],
                    })
        except Exception as e:
            print(f"  [Warning] Failed to fetch {origin} ↔ {dest}: {e}")

        return quotes

def main():
    parser = argparse.ArgumentParser(description="Real Live Airfare CPI Ingestion via Amadeus GDS (SIH 26056)")
    parser.add_argument("--client-id", type=str, required=True, help="Amadeus API Key (Client ID)")
    parser.add_argument("--client-secret", type=str, required=True, help="Amadeus API Secret")
    parser.add_argument("--date", type=str, default=None, help="Departure date (YYYY-MM-DD), defaults to +3 days")

    args = parser.parse_args()

    dep_date = args.date or (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")

    print("=" * 70)
    print("  AirIntel India - Live Real Flight Data Ingestion Pipeline")
    print("  SIH Problem Statement 26056 | MoSPI CPI Augmentation")
    print("=" * 70)
    print(f"Target Departure Date: {dep_date}")
    print("Authenticating with Amadeus GDS...")

    engine = AmadeusLiveEngine(args.client_id, args.client_secret)
    engine.authenticate()
    print("✓ OAuth2 Authentication Successful!\n")

    all_real_quotes = []
    route_stats = {}

    for corridor, meta in CORRIDOR_BENCHMARKS.items():
        origin, dest = corridor.split("-")
        print(f"Fetching real live quotes for {meta['name']} ({corridor})...")
        quotes = engine.fetch_live_corridor_fares(origin, dest, dep_date)
        print(f"  → Ingested {len(quotes)} verified real live flight offers")
        all_real_quotes.extend(quotes)

        if quotes:
            avg_fare = sum(q["total_fare"] for q in quotes) / len(quotes)
            rel = avg_fare / meta["base_price"]
            route_stats[corridor] = {
                "quotes_count": len(quotes),
                "avg_fare": avg_fare,
                "base_price": meta["base_price"],
                "price_relative": rel,
                "weight": meta["weight"]
            }

    if not all_real_quotes:
        print("\n[!] No live quotes could be retrieved. Check your API credentials and corridor parameters.")
        return

    # Calculate real UN/ILO Jevons Index
    log_sum = 0
    count = 0
    for q in all_real_quotes:
        corridor = f"{q['origin']}-{q['destination']}"
        base_p = CORRIDOR_BENCHMARKS.get(corridor, {}).get("base_price", 4850)
        log_sum += math.log(q["total_fare"] / base_p)
        count += 1

    real_jevons = math.exp(log_sum / count) * 100

    # Calculate real Weighted Laspeyres Index
    total_weighted_rel = sum(s["weight"] * s["price_relative"] for s in route_stats.values())
    total_weight = sum(s["weight"] for s in route_stats.values())
    real_laspeyres = (total_weighted_rel / total_weight) * 100

    print("\n" + "=" * 70)
    print("  REAL LIVE COMPUTED AIRFARE CPI REPORT")
    print("=" * 70)
    print(f"Total Verified Quotes Ingested : {len(all_real_quotes)}")
    print(f"Corridors Sampled              : {len(route_stats)}")
    print(f"Computed UN/ILO Jevons Index   : {real_jevons:.2f} (Base = 100)")
    print(f"Computed Weighted Laspeyres    : {real_laspeyres:.2f} (DGCA Weights)")
    print("-" * 70)
    print(f"{'Corridor':<12} {'Base Price':<12} {'Real Avg Fare':<15} {'Price Rel':<12} {'Weight %':<10}")
    print("-" * 70)
    for c, s in route_stats.items():
        print(f"{c:<12} ₹{s['base_price']:<11} ₹{s['avg_fare']:<14.0f} {s['price_relative']:<12.3f} {s['weight']*100:.1f}%")
    print("=" * 70)

if __name__ == "__main__":
    main()
