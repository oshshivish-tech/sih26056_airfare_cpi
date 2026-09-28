# APIx • VayuSuchak (वायु सूचक) ✈️
### Real-Time Airfare Price Index for India through Automated Web Scraping
**Smart India Hackathon (SIH 2026) • Problem Statement ID: 26056**
**Organization**: Ministry of Statistics and Programme Implementation (MoSPI) • National Statistical Office (NSO)

* **Production Web Platform**: [https://sih26056-airfare-cpi.vercel.app/](https://sih26056-airfare-cpi.vercel.app/)
* **Interactive Pitch Deck**: [https://sih26056-airfare-cpi.vercel.app/slides.html](https://sih26056-airfare-cpi.vercel.app/slides.html)
* **Backend REST API**: `/api/v1/apix/*` (FastAPI Server in `backend/api_server.py`)

---

## 🎯 Official Expected Solution Compliance (SIH 26056)

Our solution rigorously implements all **5 core pillars** defined in the official SIH 26056 problem statement:

### Pillar (a): Multi-Source Ethical Scraping Engine
* **File**: [`backend/scraping_engine.py`](file:///C:/Users/oshsh/.gemini/antigravity/scratch/sih26056_airfare_cpi/backend/scraping_engine.py)
* **Portals Covered**:
  - Direct Airlines: **IndiGo** (`6E`), **Air India** (`AI`), **Akasa Air** (`QP`), **SpiceJet** (`SG`)
  - Online Travel Aggregators (OTAs): **MakeMyTrip**, **EaseMyTrip**
* **Ethical Compliance**: Integrated `urllib.robotparser` enforcing `robots.txt` compliance across all portals.
* **Anti-Bot Stealth**: User-Agent pool rotation, TLS header emulation, jittered polite rate-limiting (`RateLimiter`).
* **Lead Time Horizon Sampling**: Automated stratified sampling across **T+1, T+7, T+15, T+30, T+45**.

### Pillar (b): Cleaned, De-duplicated Database with Metadata Disaggregation
* **File**: [`backend/database.py`](file:///C:/Users/oshsh/.gemini/antigravity/scratch/sih26056_airfare_cpi/backend/database.py)
* **SQLite Storage**: `backend/airfare_cpi.db` with 3 core tables:
  1. `raw_scraped_payloads`: Immutable raw batch audit trail with cryptographic SHA-256 fingerprinting.
  2. `flight_quotes`: De-duplicated, normalized quotes (`UNIQUE(flight_number, departure_date, scraping_timestamp_hour)`).
  3. `apix_index_series`: Persisted Daily, Weekly, and Monthly APIx index points.
* **Full Fare Disaggregation**:
  - `base_fare`
  - `fuel_surcharge` (ATF fuel volatility pass-through)
  - `airport_user_fee` (Airport Development Fee / UDF / PSF calibrated to Metro vs Non-Metro)
  - `gst_and_taxes` (5% statutory economy GST)
  - `convenience_fee` (OTA vs Direct carrier booking fees)
  - `total_fare`

### Pillar (c): UN/ILO Elementary & DGCA Weighted Index Construction (APIx)
* **File**: [`backend/apix_engine.py`](file:///C:/Users/oshsh/.gemini/antigravity/scratch/sih26056_airfare_cpi/backend/apix_engine.py)
* **UN/ILO Elementary Jevons Index**:
  $$I_{\text{Jevons}} = \exp\left(\frac{1}{N}\sum_{i=1}^N \ln\left(\frac{P_{i,t}}{P_{i,0}}\right)\right) \times 100$$
* **Dutot Ratio of Arithmetic Means**:
  $$I_{\text{Dutot}} = \frac{\sum P_{i,t}}{\sum P_{i,0}} \times 100$$
* **DGCA Passenger-Weighted Laspeyres Index**:
  $$I_{\text{Laspeyres}} = \frac{\sum_{c} w_c \cdot \left(\frac{P_{c,t}}{P_{c,0}}\right)}{\sum_c w_c} \times 100$$
  Calibrated against official DGCA annual city-pair traffic weights across **12 representative corridors** (~81.4% of total domestic passenger volume).
* **IQR Outlier Filtering**: Dynamically prunes flexi surge spikes $[Q_1 - 1.5\text{IQR}, Q_3 + 2.0\text{IQR}]$ with Z-score audit tags.

### Pillar (d): Interactive Dashboard & Open REST API for NSO and RBI
* **Interactive Frontend**:
  - Real-time headline **APIx** index tracking
  - 12-Corridor domestic route heatmap & interactive GIS flight network
  - **Advance-Purchase Elasticity Curve** visualizer (T+1 through T+45)
  - **30-Day Back-Testing Card** validating daily APIx against DGCA monthly passenger yield data
* **NSO & RBI Open REST API Server** ([`backend/api_server.py`](file:///C:/Users/oshsh/.gemini/antigravity/scratch/sih26056_airfare_cpi/backend/api_server.py)):
  - `GET /api/v1/apix/current` : Real-time Jevons, Dutot, and Weighted Laspeyres index
  - `GET /api/v1/apix/daily` : 30-day time-series with weekend elasticity vs DGCA benchmarks
  - `GET /api/v1/apix/lead-time` : Advance booking horizon yield elasticity curves
  - `GET /api/v1/apix/corridors` : 12 DGCA corridors with weights, fares, and price relatives
  - `GET /api/v1/apix/export/mospi` : Direct eSankhyiki CSV format with Item Code `1.1.07.03`
  - Interactive **REST API Explorer Modal** directly accessible in the web dashboard!

### Pillar (e): Automated Testing & Quality Assurance
* **File**: [`tests/test_apix_pipeline.py`](file:///C:/Users/oshsh/.gemini/antigravity/scratch/sih26056_airfare_cpi/tests/test_apix_pipeline.py)
* **Test Suite**:
  - `test_fare_disaggregation_integrity`: Verifies fare components sum exactly to total fare
  - `test_database_deduplication_and_provenance`: Validates SHA-256 fingerprinting and unique constraints
  - `test_iqr_outlier_filtering`: Prunes flexi surge spikes and promotional errors
  - `test_un_ilo_jevons_and_dutot_calculation`: Mathematical precision on geometric mean indices
  - `test_dgca_weighted_laspeyres`: Verifies corridor weights align with DGCA official statistics
  - `test_lead_time_elasticity_ordering`: Confirms dynamic pricing hierarchy ($T+1 > T+7 > T+15 > T+30 > T+45$)
  - `test_fastapi_endpoints_schema`: Validates REST endpoints and eSankhyiki CSV export format
* Run tests with: `python -m unittest tests/test_apix_pipeline.py` (100% PASS).

---

## 🚀 Quickstart & Verification

### 1. Run Automated Test Suite
```bash
python -m unittest tests/test_apix_pipeline.py
```

### 2. Execute Scraping Engine
```bash
python -m backend.scraping_engine
```

### 3. Launch NSO & RBI FastAPI Service
```bash
uvicorn backend.api_server:app --reload --port 8000
```
Open interactive Swagger documentation at `http://localhost:8000/docs`.

### 4. Run Frontend Dashboard
```bash
npm install
npm run dev
```

---

## 🏛️ Project Maintainers & SIH 2026 Details
* **Team Name**: Roorkies
* **Team ID**: 168405
* **Problem Statement**: SIH 26056 (Real-Time Airfare Price Index for CPI Augmentation)
* **College / Institution**: D Y Patil University Pune Ambi
* **Team Leader**: Nikhil
* **Team Members**: Nikhil (Leader), Shivish, Pranav, Harsh, Tejas, Blessy
* **Live Deployment**: [https://sih26056-airfare-cpi.vercel.app](https://sih26056-airfare-cpi.vercel.app)
* **Presentation Viewer**: [https://sih26056-airfare-cpi.vercel.app/slides.html](https://sih26056-airfare-cpi.vercel.app/slides.html)
