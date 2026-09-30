# VayuSuchak: Data Access, Ethics & Scraping Compliance Policy
**Smart India Hackathon 2026 | Problem Statement ID: SIH26056**  
**Team Roorkies**

---

## 1. Objective & Scope

VayuSuchak is an academic and research prototype developed for **SIH 2026** to demonstrate how real-time, automated airfare price collection can eliminate the 15-day reporting lag in India's official Consumer Price Index (CPI), currently maintained by the Ministry of Statistics and Programme Implementation (MoSPI).

This document establishes our **strict ethical, technical, and regulatory compliance standards** governing how fare data is collected, validated, and stored.

---

## 2. Ethical Data Collection Principles

### 2.1 Robots.txt Verification
- All automated harvesters verify each target domain's `/robots.txt` policy prior to making HTTP requests using Python's standard `urllib.robotparser.RobotFileParser`.
- The engine checks whether the intended flight search path is disallowed for our user-agent and halts extraction immediately if restricted.

### 2.2 Conservative Request Rates & Polite Pacing
- The prototype enforces conservative crawl rates:
  - Minimum request delay of 1.5 to 3.0 seconds between consecutive route queries.
  - Queries are scheduled during off-peak hours (02:00 AM – 04:00 AM IST) when domestic airline booking traffic is at its daily minimum.
  - Total queries per carrier are strictly capped to ensure 0% load disruption to airline servers.

### 2.3 Transparent & Descriptive User-Agent Identification
We do not impersonate arbitrary consumer browsers or conceal the identity of the research crawler. All HTTP headers explicitly declare:
```http
User-Agent: VayuSuchak-Research-Bot/1.0 (+https://sih26056-airfare-cpi.vercel.app; research-contact@roorkies.edu)
Accept: application/json, text/plain, */*
```
Website administrators and site reliability engineers can identify our research traffic, consult our public documentation, or contact the research team directly.

### 2.4 Exponential Backoff Protocol
If a target portal issues HTTP status codes `429 (Too Many Requests)` or `503 (Service Unavailable)`:
- The crawler halts all requests to that carrier immediately.
- Implements randomized exponential backoff ($T_{\text{wait}} = 2^n \times \text{jitter}$).
- If repeated after 3 attempts, the carrier collection is aborted for that scheduled batch window and flagged in the system health log.

### 2.5 Prohibition of Circumvention Technologies
Our submission repository strictly prohibits and removes:
- Fingerprint-evasion patches or header deception.
- Commercial or residential proxy pool rotation to bypass access restrictions.
- Automated CAPTCHA solving mechanisms.

---

## 3. Transition Roadmap: From Prototype to Sovereign Production

Scraping is strictly an initial prototype validation path. In production, sovereign statistical agencies like MoSPI and DGCA do not rely on scraping. The VayuSuchak architectural roadmap establishes a 3-phase transition:

| Phase | Deployment Stage | Data Access Mechanism | Governance |
| :--- | :--- | :--- | :--- |
| **Phase 1 (Current)** | Prototype Pilot (12 Corridors) | Rate-limited, robots.txt-compliant Playwright & public API queries | Academic research compliance under SIH 26056 guidelines |
| **Phase 2** | National Expansion (Top 50 Routes) | Official airline NDC (New Distribution Capability) feeds & GDS sandbox | Bilateral data-sharing MoUs facilitated through MoCA / DGCA |
| **Phase 3** | Sovereign Integration (250+ Corridors) | Direct server-to-server API push from scheduled Indian carriers | MoSPI National Data Sharing and Accessibility Policy (NDSAP) |

---

## 4. Cryptographic Provenance & Audit Integrity

To ensure every price quote can be legally scrutinized and verified by MoSPI inspectors:
1. **Raw Quote Hashing**: Every flight quote received is normalized into a standard JSON schema and hashed using **SHA-256**:
   $$\text{Hash} = \text{SHA256}(\text{Airline} \parallel \text{FlightNo} \parallel \text{DepDate} \parallel \text{Timestamp} \parallel \text{BaseFare})$$
2. **Merkle Proof Batches**: Daily batch quotes are compiled into a cryptographic Merkle Tree. The daily Merkle Root is recorded in an append-only ledger, ensuring any retrospective alteration or tampering of price history is mathematically detectable.
