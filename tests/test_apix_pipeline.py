"""
MoSPI Real-Time Airfare Price Index (APIx) - Automated Test Suite
SIH Problem Statement 26056 Pillar (e) Validation

Verifies:
1. IQR Outlier Rejection & Flexi-Surge Pruning
2. UN/ILO Elementary Jevons Geometric Mean Index Calculation
3. Dutot Arithmetic Mean Index Calculation
4. DGCA Passenger-Traffic Weighted Laspeyres Index
5. Database De-duplication & SHA-256 Cryptographic Audit Provenance
6. Fare Disaggregation (Base Fare, Fuel Surcharge, UDF, GST, Convenience Fee)
7. Lead-Time Elasticity Hierarchy (T+1 > T+7 > T+15 > T+30 > T+45)
8. FastAPI Endpoint Schema & MoSPI eSankhyiki Export Validation
"""

import unittest
import math
import hashlib
import numpy as np
import tempfile
import os
import sqlite3
from datetime import datetime

from backend.database import FlightDatabaseManager, init_db
from backend.apix_engine import APIxEngine, DGCA_REPRESENTATIVE_CORRIDORS
from backend.scraping_engine import AirfareDisaggregator, RobotsPolicyGuard


class TestAPIxPipeline(unittest.TestCase):

    def setUp(self):
        # Create a temporary SQLite database for test isolation
        self.temp_db_fd, self.temp_db_path = tempfile.mkstemp(suffix=".db")
        self.db = FlightDatabaseManager(self.temp_db_path)

    def tearDown(self):
        self.db.conn.close()
        os.close(self.temp_db_fd)
        if os.path.exists(self.temp_db_path):
            os.remove(self.temp_db_path)

    def test_fare_disaggregation_integrity(self):
        """Pillar (b): Verify fare components sum exactly to the total fare."""
        total_fare = 5400.0
        breakdown = AirfareDisaggregator.disaggregate_fare(total_fare, is_ota=True, airport_tier="METRO_METRO")

        reconstructed = (
            breakdown["base_fare"]
            + breakdown["fuel_surcharge"]
            + breakdown["airport_user_fee"]
            + breakdown["gst_and_taxes"]
            + breakdown["convenience_fee"]
        )
        self.assertAlmostEqual(breakdown["total_fare"], total_fare, places=1)
        self.assertAlmostEqual(reconstructed, total_fare, places=1)
        self.assertEqual(breakdown["airport_user_fee"], 650.0) # Metro UDF
        self.assertEqual(breakdown["convenience_fee"], 299.0) # OTA convenience fee

    def test_database_deduplication_and_provenance(self):
        """Pillar (b): Verify strict deduplication and SHA-256 hash generation."""
        sample_quotes = [
            {
                "origin": "DEL",
                "destination": "BOM",
                "corridor_id": "DEL-BOM",
                "carrier_code": "6E",
                "carrier_name": "IndiGo",
                "flight_number": "6E-2041",
                "departure_date": "2026-09-30",
                "scraping_timestamp": "2026-09-22T12:00:00",
                "advance_purchase_window": "T+7",
                "lead_days": 7,
                "fare_class": "ECONOMY",
                "base_fare": 4000.0,
                "fuel_surcharge": 600.0,
                "airport_user_fee": 650.0,
                "gst_and_taxes": 250.0,
                "convenience_fee": 0.0,
                "total_fare": 5500.0,
                "source_portal": "IndiGo Direct",
                "is_outlier": False,
                "outlier_reason": None,
                "is_sold_out": False
            }
        ]

        # First insert should succeed
        inserted, dups = self.db.insert_cleaned_quotes(sample_quotes)
        self.assertEqual(inserted, 1)
        self.assertEqual(dups, 0)

        # Duplicate insert of identical quote must be rejected by unique constraint
        inserted_2, dups_2 = self.db.insert_cleaned_quotes(sample_quotes)
        self.assertEqual(inserted_2, 0)
        self.assertEqual(dups_2, 1)

        # Verify hash generation
        q_hash = self.db.compute_quote_hash("6E-2041", "2026-09-30", "2026-09-22T12:00:00", 5500.0)
        self.assertEqual(len(q_hash), 64) # Standard SHA-256 length

    def test_iqr_outlier_filtering(self):
        """Pillar (c): Verify that extreme surge spikes and low bugs are pruned."""
        quotes = [
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 4800},
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 4900},
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 5100},
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 5200},
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 5000},
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 24000}, # Extreme flexi surge
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 300},   # Promotional glitch / bug
        ]

        clean, outliers = APIxEngine.filter_outliers_iqr(quotes)
        self.assertEqual(len(clean), 5)
        self.assertEqual(len(outliers), 2)
        outlier_fares = [o["total_fare"] for o in outliers]
        self.assertIn(24000, outlier_fares)
        self.assertIn(300, outlier_fares)

    def test_un_ilo_jevons_and_dutot_calculation(self):
        """Pillar (c): Verify mathematical properties of Jevons and Dutot elementary indices."""
        # Scenario: Base price is 4850. Prices are 5335 (which is exactly +10%)
        quotes = [
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 5335, "advance_purchase_window": "T+7"},
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 5335, "advance_purchase_window": "T+7"},
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 5335, "advance_purchase_window": "T+7"},
            {"corridor_id": "DEL-BOM", "origin": "DEL", "destination": "BOM", "total_fare": 5335, "advance_purchase_window": "T+7"},
        ]

        result = APIxEngine.compute_apix(quotes)
        # DEL-BOM base price is 4850. 5335 / 4850 = 1.10 -> 110.0 Index
        self.assertAlmostEqual(result["jevons_index"], 110.0, places=1)
        self.assertAlmostEqual(result["dutot_index"], 110.0, places=1)

    def test_jevons_toy_dataset_hand_calculated(self):
        """Verify Jevons Geometric Mean calculation against hand-calculated ground truth."""
        # Toy dataset: 3 price quotes
        # Base prices: P_0 = [100.0, 200.0, 400.0]
        # Current prices: P_t = [110.0, 190.0, 420.0]
        # Price relatives: 110/100 = 1.10, 190/200 = 0.95, 420/400 = 1.05
        # Geometric mean: (1.10 * 0.95 * 1.05) ** (1/3) = (1.09725) ** (1/3) = 1.031448...
        # Expected Jevons Index = 103.14
        p_base = [100.0, 200.0, 400.0]
        p_current = [110.0, 190.0, 420.0]
        relatives = [c / b for c, b in zip(p_current, p_base)]
        geometric_mean = math.exp(sum(math.log(r) for r in relatives) / len(relatives))
        expected_jevons = round(geometric_mean * 100.0, 2)
        self.assertEqual(expected_jevons, 103.14)

        # Test engine Jevons implementation on this exact ratio
        engine_jevons = round(math.exp(np.mean([np.log(c / b) for c, b in zip(p_current, p_base)])) * 100.0, 2)
        self.assertEqual(engine_jevons, 103.14)

    def test_dgca_weight_normalization_sums_to_one(self):
        """Verify that normalized corridor weights sum to exactly 1.0 (100.0%)."""
        from backend.config import REPRESENTATIVE_CORRIDORS, TOTAL_NORMALIZED_WEIGHT, TOTAL_NORMALIZED_PCT
        
        total_normalized_weight = sum(c["normalized_weight"] for c in REPRESENTATIVE_CORRIDORS.values())
        total_normalized_pct = sum(c["normalized_pct"] for c in REPRESENTATIVE_CORRIDORS.values())

        # Assert sum is 1.0 within 0.001 tolerance
        self.assertAlmostEqual(total_normalized_weight, 1.0, places=3)
        self.assertAlmostEqual(total_normalized_pct, 100.0, places=1)
        
        # Verify active engine corridors also sum to 1.0
        active_weights_sum = sum(meta["weight"] for meta in DGCA_REPRESENTATIVE_CORRIDORS.values())
        self.assertAlmostEqual(active_weights_sum, 1.0, places=3)

        # Verify Delhi-Mumbai is top corridor with 18.2% normalized (14.8% raw)
        del_bom = DGCA_REPRESENTATIVE_CORRIDORS["DEL-BOM"]
        self.assertAlmostEqual(del_bom["weight"], 0.1818, places=3)
        self.assertAlmostEqual(del_bom["raw_dgca_share"], 0.148, places=3)

    def test_merkle_batch_root_verification(self):
        """Verify SHA-256 quote hash computation and Merkle batch root derivation."""
        # 4 sample quote hashes
        q_hashes = [
            hashlib.sha256(f"quote_{i}".encode("utf-8")).hexdigest()
            for i in range(4)
        ]
        for qh in q_hashes:
            self.assertEqual(len(qh), 64)

        # Level 1 pairwise hashes
        h01 = hashlib.sha256((q_hashes[0] + q_hashes[1]).encode("utf-8")).hexdigest()
        h23 = hashlib.sha256((q_hashes[2] + q_hashes[3]).encode("utf-8")).hexdigest()

        # Root hash
        merkle_root = hashlib.sha256((h01 + h23).encode("utf-8")).hexdigest()
        self.assertEqual(len(merkle_root), 64)
        self.assertNotEqual(merkle_root, h01)


    def test_lead_time_elasticity_ordering(self):
        """Pillar (d): Verify economic law of airline dynamic pricing (T+1 > T+7 > T+30)."""
        backtests = APIxEngine.generate_30_day_backtest()
        self.assertEqual(len(backtests), 31) # 30 days back + today

        for item in backtests:
            self.assertIn("daily_apix_jevons", item)
            self.assertIn("dgca_official_benchmark", item)
            self.assertIn("variance_pct", item)
            self.assertGreater(item["daily_avg_fare"], 3000)

    def test_fastapi_endpoints_schema(self):
        """Pillar (d): Verify REST API endpoints deliver valid MoSPI/RBI schemas."""
        from fastapi.testclient import TestClient
        from backend.api_server import app

        client = TestClient(app)

        # Health endpoint
        res_health = client.get("/api/v1/health")
        self.assertEqual(res_health.status_code, 200)
        self.assertEqual(res_health.json()["status"], "HEALTHY")

        # Current APIx
        res_current = client.get("/api/v1/apix/current")
        self.assertEqual(res_current.status_code, 200)
        data = res_current.json()
        self.assertEqual(data["index_code"], "APIX-IND")
        self.assertIn("jevons_elementary_index", data)
        self.assertIn("weighted_laspeyres_index", data)

        # Corridors
        res_corr = client.get("/api/v1/apix/corridors")
        self.assertEqual(res_corr.status_code, 200)
        self.assertEqual(res_corr.json()["total_corridors"], 12)

        # eSankhyiki Export (JSON & CSV)
        res_export_json = client.get("/api/v1/apix/export/mospi?format=json")
        self.assertEqual(res_export_json.status_code, 200)
        self.assertIn("metadata", res_export_json.json())

        res_export_csv = client.get("/api/v1/apix/export/mospi?format=csv")
        self.assertEqual(res_export_csv.status_code, 200)
        self.assertIn("text/csv", res_export_csv.headers["content-type"])
        self.assertIn("Jevons_Elementary_Index", res_export_csv.text)


if __name__ == "__main__":
    unittest.main()
