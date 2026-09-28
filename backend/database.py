"""
MoSPI Airfare Price Index (APIx) - Database & Data Cleaning Module
SIH Problem Statement 26056

Implements:
- Persistent SQLite storage for scraped flight quotes
- Strict de-duplication pipeline
- SHA-256 cryptographic provenance hashing
- Disaggregation of Base Fare, Taxes, User Development Fee (UDF), and Convenience Fees
"""

import sqlite3
import hashlib
import json
from datetime import datetime
from typing import List, Dict, Optional, Tuple

DB_PATH = "backend/airfare_cpi.db"

def init_db(db_path: str = DB_PATH) -> sqlite3.Connection:
    """Initializes the SQLite database with proper schema, indexes, and constraints."""
    conn = sqlite3.connect(db_path, check_same_thread=False)
    cursor = conn.cursor()

    # Table 1: Raw Ingestion Audit Trail (Immutable)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS raw_scraped_payloads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sha256_hash TEXT UNIQUE NOT NULL,
        portal TEXT NOT NULL,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        payload_json TEXT NOT NULL,
        quotes_count INTEGER NOT NULL,
        ingested_at TEXT NOT NULL
    );
    """)

    # Table 2: Cleaned and De-duplicated Flight Quotes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flight_quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote_hash TEXT UNIQUE NOT NULL,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        corridor_id TEXT NOT NULL,
        carrier_code TEXT NOT NULL,
        carrier_name TEXT NOT NULL,
        flight_number TEXT NOT NULL,
        departure_date TEXT NOT NULL,
        scraping_timestamp TEXT NOT NULL,
        advance_purchase_window TEXT NOT NULL, -- T+1, T+7, T+15, T+30, T+45
        lead_days INTEGER NOT NULL,
        fare_class TEXT DEFAULT 'ECONOMY',
        base_fare REAL NOT NULL,
        fuel_surcharge REAL NOT NULL,
        airport_user_fee REAL NOT NULL, -- UDF / PSF
        gst_and_taxes REAL NOT NULL,
        convenience_fee REAL NOT NULL,
        total_fare REAL NOT NULL,
        source_portal TEXT NOT NULL,
        is_outlier INTEGER DEFAULT 0,
        outlier_reason TEXT,
        is_sold_out INTEGER DEFAULT 0
    );
    """)

    # Table 3: Daily, Weekly, and Monthly Computed Airfare Price Index (APIx)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS apix_index_series (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        period_type TEXT NOT NULL, -- 'DAILY', 'WEEKLY', 'MONTHLY'
        period_date TEXT NOT NULL,
        jevons_index REAL NOT NULL,
        dutot_index REAL NOT NULL,
        weighted_laspeyres_index REAL NOT NULL,
        sample_count INTEGER NOT NULL,
        avg_fare REAL NOT NULL,
        yoy_inflation REAL,
        mom_inflation REAL,
        dgca_benchmark_fare REAL,
        computed_at TEXT NOT NULL,
        UNIQUE(period_type, period_date)
    );
    """)

    # Performance Indexes
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_flight_corridor ON flight_quotes(corridor_id, departure_date);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_flight_lead ON flight_quotes(advance_purchase_window);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_flight_date ON flight_quotes(scraping_timestamp);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_apix_date ON apix_index_series(period_type, period_date);")

    conn.commit()
    return conn

class FlightDatabaseManager:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.conn = init_db(db_path)

    def compute_quote_hash(self, flight_number: str, departure_date: str, scrape_time: str, total_fare: float) -> str:
        """Generates an immutable SHA-256 fingerprint for deduplication and auditability."""
        raw = f"{flight_number}_{departure_date}_{scrape_time[:13]}_{total_fare:.2f}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def insert_raw_batch(self, portal: str, origin: str, destination: str, raw_quotes: List[Dict]) -> str:
        """Stores immutable raw payload in raw_scraped_payloads."""
        payload_str = json.dumps(raw_quotes)
        batch_hash = hashlib.sha256(f"{portal}_{origin}_{destination}_{datetime.now().isoformat()}_{payload_str}".encode("utf-8")).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO raw_scraped_payloads (sha256_hash, portal, origin, destination, payload_json, quotes_count, ingested_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (batch_hash, portal, origin, destination, payload_str, len(raw_quotes), datetime.now().isoformat()))
        self.conn.commit()
        return batch_hash

    def insert_cleaned_quotes(self, quotes: List[Dict]) -> Tuple[int, int]:
        """
        Inserts cleaned quotes with automatic de-duplication and disaggregation.
        Returns: (inserted_count, duplicates_skipped)
        """
        cursor = self.conn.cursor()
        inserted = 0
        duplicates = 0

        for q in quotes:
            q_hash = self.compute_quote_hash(
                q["flight_number"],
                q["departure_date"],
                q["scraping_timestamp"],
                q["total_fare"]
            )

            try:
                cursor.execute("""
                    INSERT INTO flight_quotes (
                        quote_hash, origin, destination, corridor_id, carrier_code, carrier_name,
                        flight_number, departure_date, scraping_timestamp, advance_purchase_window,
                        lead_days, fare_class, base_fare, fuel_surcharge, airport_user_fee,
                        gst_and_taxes, convenience_fee, total_fare, source_portal, is_outlier, outlier_reason, is_sold_out
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    q_hash,
                    q["origin"],
                    q["destination"],
                    q.get("corridor_id", f"{q['origin']}-{q['destination']}"),
                    q["carrier_code"],
                    q["carrier_name"],
                    q["flight_number"],
                    q["departure_date"],
                    q["scraping_timestamp"],
                    q.get("advance_purchase_window", "T+7"),
                    q.get("lead_days", 7),
                    q.get("fare_class", "ECONOMY"),
                    q["base_fare"],
                    q.get("fuel_surcharge", 0),
                    q.get("airport_user_fee", 0),
                    q.get("gst_and_taxes", 0),
                    q.get("convenience_fee", 0),
                    q["total_fare"],
                    q.get("source_portal", "DIRECT_PORTAL"),
                    1 if q.get("is_outlier") else 0,
                    q.get("outlier_reason"),
                    1 if q.get("is_sold_out") else 0
                ))
                inserted += 1
            except sqlite3.IntegrityError:
                duplicates += 1

        self.conn.commit()
        return inserted, duplicates

    def get_corridor_quotes(self, corridor_id: str, exclude_outliers: bool = True) -> List[Dict]:
        """Retrieves quotes for a specific corridor."""
        cursor = self.conn.cursor()
        query = "SELECT * FROM flight_quotes WHERE corridor_id = ?"
        params = [corridor_id]
        if exclude_outliers:
            query += " AND is_outlier = 0"

        cursor.execute(query, params)
        cols = [col[0] for col in cursor.description]
        return [dict(zip(cols, row)) for row in cursor.fetchall()]

    def record_apix_index(self, period_type: str, period_date: str, jevons: float, dutot: float,
                          laspeyres: float, sample_count: int, avg_fare: float,
                          yoy: float = 0.0, mom: float = 0.0, dgca_benchmark: float = None):
        """Records computed APIx point into persistent series."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO apix_index_series (
                period_type, period_date, jevons_index, dutot_index, weighted_laspeyres_index,
                sample_count, avg_fare, yoy_inflation, mom_inflation, dgca_benchmark_fare, computed_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            period_type, period_date, jevons, dutot, laspeyres, sample_count,
            avg_fare, yoy, mom, dgca_benchmark, datetime.now().isoformat()
        ))
        self.conn.commit()

    def get_latest_index(self, period_type: str = "DAILY") -> Optional[Dict]:
        """Fetches the latest computed index point."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM apix_index_series 
            WHERE period_type = ? 
            ORDER BY period_date DESC LIMIT 1
        """, (period_type,))
        row = cursor.fetchone()
        if not row:
            return None
        cols = [col[0] for col in cursor.description]
        return dict(zip(cols, row))
