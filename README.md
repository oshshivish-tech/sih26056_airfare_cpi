# VayuSuchak (वायु सूचक) ✈️
### Real-Time Airfare Price Index & Automated Ingestion Engine for MoSPI eSankhyiki
**Smart India Hackathon (SIH 2026) • Problem Statement ID: 26056**

* **Live Web Application**: [https://sih26056-airfare-cpi.vercel.app/](https://sih26056-airfare-cpi.vercel.app/)
* **Interactive Pitch Deck**: [https://sih26056-airfare-cpi.vercel.app/slides.html](https://sih26056-airfare-cpi.vercel.app/slides.html)

---

## 📌 Problem Overview
India's domestic civil aviation sector experiences rapid algorithmic dynamic pricing that creates extreme intraday and lead-time fare dispersion. Under the existing Consumer Price Index (CPI) framework:
1. **Manual Collection Lag**: Traditional physical survey collection introduces a ~15-30 day lag before fare quotes are reflected in official indices.
2. **Volatile Dynamic Pricing**: Conventional monthly price checks fail to capture advance booking horizons (1d, 7d, 15d, 30d, 45d).
3. **Surge Substitution Bias**: Standard arithmetic averages (Dutot) suffer from upward substitution bias caused by holiday surges.

**VayuSuchak** solves this by automating multi-portal extraction, pruning outliers using Interquartile Range (IQR), computing the **UN/ILO Jevons Elementary Geometric Mean**, and weighting corridors by official **DGCA passenger traffic volumes**.

---

## 🏛️ System Architecture

```
[ Ingestion Layer ]
  ├── Playwright Stealth Chromium (Direct Airline Portals: IndiGo, Air India)
  └── XHR API Interception (Aggregators: MakeMyTrip, EaseMyTrip, Yatra)
            │
            ▼ (Raw Flight Quotes)
[ Cleansing & Normalization ]
  ├── Fare Decomposition: Base Fare + Fuel Surcharge + Airport Fees (UDF) + GST
  ├── Multi-Horizon Stratification: 1-Day, 7-Day, 15-Day, 30-Day, 45-Day
  └── IQR Outlier Filter: [Q1 - 1.5×IQR, Q3 + 2.0×IQR] & Z-Score Validation
            │
            ▼ (Clean Quotes)
[ Statistical Calculation Engine ]
  ├── UN/ILO Jevons Geometric Mean: I_Jevons = exp( (1/N) * ∑ ln(P_t / P_0) ) * 100
  ├── Dutot Arithmetic & Laspeyres Comparison Series
  └── DGCA Passenger Volume Weighting: 12 Key Domestic Corridors (∑w_c = 1.0)
            │
            ▼ (Verified Index Points)
[ Provenance & eSankhyiki Integration ]
  ├── SHA-256 Merkle-Style Cryptographic Audit Vault
  └── Standardized eSankhyiki / MoSPI Form 4 Output (Base = 100)
```

---

## ⚙️ Tech Stack
* **Web Scraping**: Python 3.13, Playwright Headless Stealth, XHR Interception
* **Statistical Modeling**: UN/ILO CPI Manual Standards, NumPy, SciPy, Pandas
* **Frontend Dashboard**: React 19, TypeScript, Vite, Tailwind CSS, Recharts SVG
* **Database & Storage**: PostgreSQL (TimescaleDB time-series partitioning)
* **Automation & CI/CD**: GitHub Actions Scheduled Cron (04:00 AM IST) + Vercel Edge CDN
