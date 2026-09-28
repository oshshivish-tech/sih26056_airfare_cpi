import os

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>VayuSuchak (वायु सूचक) - SIH 2026 Presentation (PS ID: 26056)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Inter:wght@400;500;600;700;800&family=Merriweather:wght@700;900&family=Roboto:wght@400;500;700;900&display=swap');
    
    * {
      box-sizing: border-box;
    }

    body {
      background-color: #0f172a;
      color: #0f172a;
      overflow: hidden;
      margin: 0;
      padding: 0;
      user-select: none;
      font-family: 'Roboto', 'Inter', sans-serif;
    }

    .serif-title {
      font-family: 'Times New Roman', 'Merriweather', serif;
    }

    .slide-viewport {
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    .slide-frame {
      width: 95vw;
      max-width: 1540px;
      aspect-ratio: 16 / 9;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 12px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      display: none;
      flex-direction: column;
      padding: 1.8rem 2.8rem;
      position: relative;
      overflow: hidden;
    }

    .slide-frame.active {
      display: flex;
      animation: fadeIn 0.25s ease-out;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.995); }
      to { opacity: 1; transform: scale(1); }
    }

    .pill-team {
      border: 2px solid #4338ca;
      border-radius: 9999px;
      padding: 0.25rem 1.4rem;
      font-weight: 700;
      color: #4338ca;
      background: #fff;
    }

    @media print {
      body {
        overflow: visible;
        background: white;
      }
      .controls { display: none !important; }
      .slide-viewport { display: block; height: auto; }
      .slide-frame {
        display: flex !important;
        page-break-after: always;
        width: 100vw;
        height: 100vh;
        border: none;
        box-shadow: none;
        border-radius: 0;
        margin: 0;
        padding: 2rem 3rem;
      }
    }
  </style>
</head>
<body>

<div class="slide-viewport">

  <!-- ======================================================== -->
  <!-- SLIDE 1: Title Slide (Centered Title, Short PS, No Members, No Footer) -->
  <!-- ======================================================== -->
  <div class="slide-frame active" id="slide-1">
    <!-- Centered Header -->
    <div class="flex items-center justify-between mb-1">
      <div class="w-16"></div>
      <div class="text-center flex-1">
        <h1 class="serif-title text-4xl lg:text-5xl font-black text-[#1b365d] tracking-wide text-center">
          SMART INDIA HACKATHON 2026
        </h1>
        <div class="text-sm font-bold text-[#184c94] mt-1">
          Sovereign Digital Public Infrastructure for MoSPI NSO &amp; RBI Inflation Targeting
        </div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <!-- Main Content -->
    <div class="grid grid-cols-12 gap-8 flex-1 items-center my-auto">
      <!-- Left Metadata Box -->
      <div class="col-span-8 bg-slate-50 border border-slate-300 rounded-2xl p-6 shadow-sm space-y-4 text-left">
        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• Problem Statement ID – </span>
          <span class="font-black text-[#184c94]">SIH26056</span>
        </div>

        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• Problem Statement Title – </span>
          <span class="font-black text-[#184c94]">Real-time Airfare Price Index for CPI Augmentation</span>
        </div>

        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• Theme – </span>
          <span class="font-black text-[#184c94]">Smart Governance / Miscellaneous</span>
        </div>

        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• PS Category – </span>
          <span class="font-black text-[#184c94]">Software</span>
        </div>

        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• Team ID – </span>
          <span class="font-black text-[#184c94]">Team Rookie</span>
        </div>

        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• Team Name – </span>
          <span class="font-black text-[#184c94]">Team Rookie</span>
        </div>
      </div>

      <!-- Right Graphic -->
      <div class="col-span-4 flex justify-center items-center">
        <img src="/presentation/page_1_img_1.png" alt="Smart India Hackathon Lightbulb" class="max-h-[380px] object-contain drop-shadow-md" />
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 2: Problem & Proposed Solution (Clean 2-Column, No Overcrowding, No Footer) -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-2">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-3">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">VAYUSUCHAK (वायु सूचक)</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">Real-Time Airfare Price Index (APIx) for Augmenting CPI</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <!-- 2-Column Spacious Layout -->
    <div class="grid grid-cols-2 gap-6 flex-1 items-stretch">
      <!-- Col 1: PROBLEM Card -->
      <div class="bg-rose-50/50 border-2 border-rose-300 rounded-2xl p-6 flex flex-col justify-between shadow-sm">
        <div>
          <div class="font-black text-xl text-rose-700 mb-4 flex items-center gap-2">
            <i class="fa-solid fa-triangle-exclamation text-rose-600"></i> CRITICAL PROBLEM IN CURRENT CPI
          </div>
          <ul class="text-sm lg:text-base text-slate-800 space-y-5 leading-relaxed">
            <li class="flex items-start gap-2.5">
              <span class="text-rose-600 font-black text-base shrink-0">✖</span>
              <div><strong class="text-rose-900">Manual Outlet Survey Bottleneck:</strong> MoSPI field staff visit physical ticketing outlets only once a month for single static quotes, causing a critical 15-day policy lag.</div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-rose-600 font-black text-base shrink-0">✖</span>
              <div><strong class="text-rose-900">Blind to Dynamic Online Pricing:</strong> Over 90% of tickets in India are sold online. Algorithmic dynamic pricing shifts fares by 200%–400% based on demand and departure time.</div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-rose-600 font-black text-base shrink-0">✖</span>
              <div><strong class="text-rose-900">Neglect of Advance Booking Curves:</strong> Traditional CPI ignores purchase lead-time horizons, missing the dramatic difference between T+1 emergency surge and T+45 saver fares.</div>
            </li>
          </ul>
        </div>
      </div>

      <!-- Col 2: SOLUTION Card -->
      <div class="bg-emerald-50/50 border-2 border-emerald-300 rounded-2xl p-6 flex flex-col justify-between shadow-sm">
        <div>
          <div class="font-black text-xl text-emerald-800 mb-4 flex items-center gap-2">
            <i class="fa-solid fa-circle-check text-emerald-600"></i> OUR SOVEREIGN SOLUTION (APIx)
          </div>
          <ul class="text-sm lg:text-base text-slate-800 space-y-4 leading-relaxed">
            <li class="flex items-start gap-2.5">
              <span class="text-emerald-600 font-black text-base shrink-0">✔</span>
              <div><strong class="text-emerald-950">Automated Multi-Carrier Harvesting:</strong> Headless crawlers extract live airfares across IndiGo, Air India, Akasa &amp; SpiceJet with strict ethical compliance.</div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-emerald-600 font-black text-base shrink-0">✔</span>
              <div><strong class="text-emerald-950">5 Forward Booking Horizons:</strong> Captures full yield curves across T+1, T+7, T+15, T+30, and T+45 departure windows with automated IQR outlier filtering.</div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-emerald-600 font-black text-base shrink-0">✔</span>
              <div><strong class="text-emerald-950">UN/ILO Jevons Geometric Mean:</strong> Eliminates consumer substitution bias and prevents upward distortion during holiday discounts.</div>
            </li>
            <li class="flex items-start gap-2.5">
              <span class="text-emerald-600 font-black text-base shrink-0">✔</span>
              <div><strong class="text-emerald-950">DGCA Volume-Weighted Aggregator:</strong> Laspeyres index calibrated with official DGCA passenger volume across 12 domestic corridors (81.4% traffic).</div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 3: Technical Approach (Visual Architecture Diagram, No Footer) -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-3">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-2">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">TECHNICAL APPROACH &amp; ARCHITECTURE</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">End-to-End Automated Pipeline from Scrape to Index</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <div class="grid grid-cols-12 gap-6 flex-1 items-stretch">
      <!-- Left Side: System Architecture Diagram (Visual) -->
      <div class="col-span-8 bg-slate-50 rounded-2xl p-2 border border-slate-300 shadow-sm flex items-center justify-center overflow-hidden">
        <img src="/presentation/architecture_diagram.png" alt="VayuSuchak Architecture Diagram" class="w-full max-h-[520px] object-contain rounded-lg" />
      </div>

      <!-- Right Side: Tech Stack Card + Live Platform -->
      <div class="col-span-4 bg-slate-50 border border-slate-300 rounded-2xl p-5 flex flex-col justify-between shadow-sm">
        <div>
          <div class="text-center font-black text-xl text-[#1b365d] mb-4 flex items-center justify-center gap-2">
            <i class="fa-solid fa-layer-group text-indigo-600"></i> CORE TECHNOLOGY STACK
          </div>
          <div class="space-y-2.5 text-xs lg:text-sm font-bold text-slate-800">
            <div>• <span class="text-slate-600 font-semibold">Engine:</span> Python 3.13 &amp; Playwright</div>
            <div>• <span class="text-slate-600 font-semibold">Statistics:</span> UN/ILO Jevons &amp; SciPy</div>
            <div>• <span class="text-slate-600 font-semibold">Database:</span> SQLite &amp; PostgreSQL</div>
            <div>• <span class="text-slate-600 font-semibold">Security:</span> SHA-256 Tamper Vault</div>
            <div>• <span class="text-slate-600 font-semibold">Frontend:</span> React 19 &amp; TypeScript</div>
            <div>• <span class="text-slate-600 font-semibold">Microservices:</span> FastAPI &amp; Uvicorn</div>
            <div>• <span class="text-slate-600 font-semibold">Hosting:</span> Vercel Edge &amp; Cloud Cron</div>
          </div>
        </div>

        <!-- Live Platform Banner -->
        <div class="border-2 border-emerald-400 rounded-xl p-3 bg-white shadow-sm text-center mt-4">
          <div class="flex items-center justify-center space-x-1.5 text-xs font-black text-emerald-800 uppercase tracking-wide mb-1">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
            <span>LIVE PROTOTYPE</span>
          </div>
          <a href="https://sih26056-airfare-cpi.vercel.app/" target="_blank" class="text-xs sm:text-sm font-black text-blue-700 hover:text-blue-900 underline break-all block py-0.5">
            sih26056-airfare-cpi.vercel.app
          </a>
          <p class="text-[10px] text-slate-500 font-medium mt-1">
            Real-time charts, REST API &amp; eSankhyiki CSV export.
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 4: Feasibility and Viability (Clean 3 Columns, No Overcrowding, No Footer) -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-4">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-3">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">FEASIBILITY AND VIABILITY</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">Technical Resilience, Operational Economy &amp; Legal Standards</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <!-- 3 Clean Columns -->
    <div class="grid grid-cols-3 gap-5 flex-1 items-stretch">
      <!-- Col 1: Technical Feasibility -->
      <div class="bg-slate-50 border border-slate-300 rounded-2xl p-5 flex flex-col justify-between shadow-sm">
        <div>
          <div class="font-black text-lg text-blue-900 mb-4 flex items-center gap-1.5">
            <i class="fa-solid fa-code text-blue-600"></i> TECHNICAL FEASIBILITY
          </div>
          <ul class="text-xs lg:text-sm text-slate-800 space-y-4 leading-relaxed">
            <li>• <strong>Automated Harvester Engine:</strong> Python &amp; Playwright framework extracts live quotes from IndiGo, Air India, Akasa &amp; SpiceJet in &lt;10 seconds.</li>
            <li>• <strong>Yield Curve Stratification:</strong> Standardized T+1, T+7, T+15, T+30, T+45 sampling captures full dynamic pricing curves.</li>
            <li>• <strong>Statistically Proven Index:</strong> Complies with UN/ILO Chapter 10 elementary Jevons index and DGCA passenger seat weighting.</li>
          </ul>
        </div>
      </div>

      <!-- Col 2: Risk & Mitigation -->
      <div class="bg-slate-50 border border-slate-300 rounded-2xl p-5 flex flex-col justify-between shadow-sm">
        <div>
          <div class="font-black text-lg text-red-900 mb-4 flex items-center gap-1.5">
            <i class="fa-solid fa-shield-halved text-red-600"></i> RISK &amp; MITIGATION
          </div>
          <ul class="text-xs lg:text-sm text-slate-800 space-y-4 leading-relaxed">
            <li>• <strong>Anti-Scraping / Cloudflare:</strong> Ethical robots.txt compliance, rotating residential proxy pool, and randomized human-like jitter delays.</li>
            <li>• <strong>Airline DOM Layout Shifts:</strong> Semantic ARIA and test-data selector schema with cached baseline fallback layers.</li>
            <li>• <strong>Surge Anomalies &amp; Outliers:</strong> Automated IQR truncation [Q1-1.5*IQR, Q3+2.0*IQR] with Z-score audit tags.</li>
          </ul>
        </div>
      </div>

      <!-- Col 3: Economic Viability -->
      <div class="bg-slate-50 border border-slate-300 rounded-2xl p-5 flex flex-col justify-between shadow-sm">
        <div>
          <div class="font-black text-lg text-emerald-900 mb-4 flex items-center gap-1.5">
            <i class="fa-solid fa-chart-line text-emerald-600"></i> ECONOMIC VIABILITY
          </div>
          <ul class="text-xs lg:text-sm text-slate-800 space-y-4 leading-relaxed">
            <li>• <strong>&gt;95% Cost Reduction:</strong> Replaces recurring physical field surveyor visits across Indian metro airports with automated digital ingestion.</li>
            <li>• <strong>Low Serverless Footprint:</strong> Entire cloud scraping and computation pipeline runs autonomously for &lt; ₹3,500 / month.</li>
            <li>• <strong>Regional Scale at Zero Cost:</strong> Scales seamlessly from 12 core metro routes to 250+ Tier-2/Tier-3 UDAN regional routes with zero extra hardware.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 5: Impact and Benefits (Spacious 2 Columns, No Footers) -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-5">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-3">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">IMPACT AND BENEFITS</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">Transforming Sovereign Economic Governance &amp; Policy Responsiveness</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <!-- 2 Columns -->
    <div class="grid grid-cols-2 gap-6 flex-1 items-stretch">
      <!-- Col 1: Sovereign Impact -->
      <div class="bg-slate-50 border border-slate-300 rounded-2xl p-5 flex flex-col justify-between shadow-sm">
        <div>
          <div class="font-black text-xl text-[#1b365d] mb-4 flex items-center gap-2">
            <i class="fa-solid fa-landmark text-blue-600"></i> SOVEREIGN &amp; INSTITUTIONAL IMPACT
          </div>
          <div class="space-y-4 text-xs lg:text-sm text-slate-800">
            <div>
              <div class="font-bold text-blue-900">🏛️ Macroeconomic Policy (RBI)</div>
              <div class="text-slate-600 mt-0.5">Eliminates the 15-day CPI publication lag, equipping the RBI Monetary Policy Committee with high-frequency leading transport inflation indicators.</div>
            </div>
            <div>
              <div class="font-bold text-blue-900">✈️ Aviation Oversight (DGCA)</div>
              <div class="text-slate-600 mt-0.5">Provides regulatory authorities with real-time surge detection to identify predatory pricing, route monopolies, and festival gouging.</div>
            </div>
            <div>
              <div class="font-bold text-blue-900">📊 Statistical Modernization (MoSPI)</div>
              <div class="text-slate-600 mt-0.5">Replaces manual spot quotes with 10,000+ daily observations, meeting UN/ILO standards and national eSankhyiki data needs.</div>
            </div>
            <div>
              <div class="font-bold text-blue-900">🇮🇳 National Digital Public Infra</div>
              <div class="text-slate-600 mt-0.5">Establishes India's first open sovereign high-frequency price monitoring platform with cryptographic SHA-256 legal auditability.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Col 2: Future Roadmap -->
      <div class="bg-slate-50 border border-slate-300 rounded-2xl p-5 flex flex-col justify-between shadow-sm">
        <div>
          <div class="font-black text-xl text-[#1b365d] mb-4 flex items-center gap-2">
            <i class="fa-solid fa-route text-indigo-600"></i> STRATEGIC FUTURE ROADMAP
          </div>
          <div class="space-y-4 text-xs lg:text-sm text-slate-800">
            <div>
              <div class="font-bold text-indigo-900">🌐 RCS-UDAN Regional Scalability</div>
              <div class="text-slate-600 mt-0.5">Expand crawler coverage from 12 core metro corridors to 250+ Tier-2 &amp; Tier-3 regional airports nationwide with zero extra infrastructure.</div>
            </div>
            <div>
              <div class="font-bold text-indigo-900">💺 Cabin Tier Decomposition</div>
              <div class="text-slate-600 mt-0.5">Segregate economy, premium economy, and business fares into granular sub-indices with separate base fare, fuel, and user fee breakdown.</div>
            </div>
            <div>
              <div class="font-bold text-indigo-900">⏱️ Intraday Time-of-Day Yield</div>
              <div class="text-slate-600 mt-0.5">Model peak departure rush hours (06:00-09:00, 17:00-20:00) vs off-peak red-eye price movements for sub-daily inflation tracking.</div>
            </div>
            <div>
              <div class="font-bold text-indigo-900">🤖 Autonomous AI Inflation Analyst</div>
              <div class="text-slate-600 mt-0.5">Deploy automated LLM agents to draft weekly inflation summary briefs and alert DGCA and MoSPI of sudden price shocks.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 6: Research and References (Original 4-Box Layout, No Footer) -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-6">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-3">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">RESEARCH AND REFERENCES</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">Academic Foundations, Official Data Sources &amp; Technical Documentation</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <!-- 4 Quadrants Grid matching PDF -->
    <div class="grid grid-cols-2 gap-4 flex-1 items-stretch">
      <!-- 1. Top-Left: Light Blue Card (SUPPORTING RESEARCH PAPERS) -->
      <div class="bg-[#bae6fd] p-5 rounded-2xl flex flex-col justify-between shadow-sm">
        <div>
          <div class="text-center font-black text-lg text-slate-900 mb-3">SUPPORTING RESEARCH PAPERS</div>
          <ul class="text-xs lg:text-sm text-slate-900 space-y-3 leading-relaxed">
            <li>• <strong>Cavallo, A., &amp; Rigobon, R. (2016).</strong> 'The Billion Prices Project: Using Online Data for Measurement and Research.' <em>Journal of Economic Perspectives</em>, 30(2), 151-178.</li>
            <li>• <strong>UN, ILO, IMF, OECD, Eurostat, World Bank (2020).</strong> <em>Consumer Price Index Manual: Concepts and Methods</em>, Chapter 10 (Elementary Indices).</li>
          </ul>
        </div>
      </div>

      <!-- 2. Top-Right: Deep Navy Card (DATA SOURCES) -->
      <div class="bg-[#0a1931] p-5 rounded-2xl flex flex-col justify-between text-white shadow-sm">
        <div>
          <div class="text-center font-black text-lg text-white mb-3">OFFICIAL DATA SOURCES</div>
          <ul class="text-xs lg:text-sm space-y-2 text-blue-100">
            <li>• <strong>DGCA India:</strong> Monthly Scheduled Domestic Passenger Traffic (dgca.gov.in)</li>
            <li>• <strong>MoSPI NSO:</strong> Consumer Price Index Concepts &amp; Guidelines (mospi.gov.in)</li>
            <li>• <strong>Direct Airline Portals:</strong> Air India, IndiGo, Akasa, SpiceJet</li>
            <li>• <strong>Online Travel Aggregators:</strong> MakeMyTrip, EaseMyTrip Non-Stop Rates</li>
          </ul>
        </div>
      </div>

      <!-- 3. Bottom-Left: Dark Navy Card (MARKET RESEARCH) -->
      <div class="bg-[#0f172a] p-5 rounded-2xl flex flex-col justify-between text-white shadow-sm">
        <div>
          <div class="text-center font-black text-lg text-indigo-200 mb-3">MARKET RESEARCH</div>
          <ul class="text-xs lg:text-sm text-slate-200 space-y-2 leading-relaxed">
            <li>• Indian domestic passenger traffic projected to grow at &gt;15% CAGR (2024–2030).</li>
            <li>• Algorithmic dynamic pricing creates massive 200–400% intraday fare dispersion.</li>
            <li>• Zero automated tools previously existed in India for daily airfare CPI tracking.</li>
            <li>• VayuSuchak eliminates the critical 15-day MoSPI manual survey lag with zero latency.</li>
          </ul>
        </div>
      </div>

      <!-- 4. Bottom-Right: Sky Blue Card (TECHNICAL DOCUMENTATION) -->
      <div class="bg-[#7dd3fc] p-5 rounded-2xl flex flex-col justify-between shadow-sm">
        <div>
          <div class="text-center font-black text-lg text-slate-900 mb-3">TECHNICAL DOCUMENTATION</div>
          <ul class="text-xs lg:text-sm text-slate-900 space-y-2 leading-relaxed font-semibold">
            <li>• <strong>Index Formulations:</strong> UN/ILO Jevons Geometric Mean vs Dutot Arithmetic Comparison.</li>
            <li>• <strong>Scraper Framework:</strong> Playwright Chromium Headless with Random UA &amp; Stealth Evasion.</li>
            <li>• <strong>Provenance Architecture:</strong> SHA-256 Hash Manifest conforming to NDSAP open standards.</li>
            <li>• <strong>Deployment:</strong> Dockerized serverless cron (02:00 AM) + Vercel Edge Web Portal.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

</div>

<!-- Navigation Controls (Bottom Bar) -->
<div class="controls fixed bottom-3 left-1/2 -translate-x-1/2 flex items-center gap-3 bg-slate-900/90 border border-slate-700/80 px-4 py-1.5 rounded-full backdrop-blur-md shadow-2xl z-50">
  <button onclick="prevSlide()" class="p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition" title="Previous Slide (Left Arrow)">
    <i class="fa-solid fa-chevron-left"></i>
  </button>
  
  <div class="flex items-center gap-1.5 px-2" id="nav-dots">
    <!-- Dots dynamically rendered -->
  </div>

  <span class="text-xs font-mono text-slate-300 px-2" id="slide-num">1 / 6</span>

  <button onclick="nextSlide()" class="p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition" title="Next Slide (Right Arrow or Space)">
    <i class="fa-solid fa-chevron-right"></i>
  </button>

  <div class="h-4 w-px bg-slate-700 mx-1"></div>

  <a href="/AirIntel_India_SIH26056_Presentation.pptx" download class="p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition flex items-center gap-1.5 text-xs font-bold text-amber-400" title="Download PPTX">
    <i class="fa-solid fa-file-powerpoint"></i>
    <span class="hidden sm:inline">Download PPTX</span>
  </a>

  <button onclick="toggleFullScreen()" class="p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition" title="Fullscreen (F)">
    <i class="fa-solid fa-expand"></i>
  </button>

  <button onclick="window.print()" class="p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition" title="Print to PDF (P)">
    <i class="fa-solid fa-print"></i>
  </button>
</div>

<script>
  let currentSlide = 1;
  const totalSlides = 6;

  function showSlide(n) {
    if (n < 1) n = 1;
    if (n > totalSlides) n = totalSlides;
    currentSlide = n;

    document.querySelectorAll('.slide-frame').forEach((el, idx) => {
      el.classList.toggle('active', idx + 1 === currentSlide);
    });

    document.getElementById('slide-num').innerText = `${currentSlide} / ${totalSlides}`;

    const dotsContainer = document.getElementById('nav-dots');
    dotsContainer.innerHTML = '';
    for (let i = 1; i <= totalSlides; i++) {
      const dot = document.createElement('button');
      dot.className = `h-2 rounded-full transition-all ${i === currentSlide ? 'w-6 bg-blue-500' : 'w-2 bg-slate-600 hover:bg-slate-500'}`;
      dot.onclick = () => showSlide(i);
      dotsContainer.appendChild(dot);
    }
  }

  function nextSlide() {
    if (currentSlide < totalSlides) showSlide(currentSlide + 1);
  }

  function prevSlide() {
    if (currentSlide > 1) showSlide(currentSlide - 1);
  }

  function toggleFullScreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
    } else if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      prevSlide();
    } else if (e.key === 'f' || e.key === 'F') {
      toggleFullScreen();
    } else if (e.key === 'p' || e.key === 'P') {
      window.print();
    }
  });

  showSlide(1);
</script>

</body>
</html>
'''

workspace_dir = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi"
artifact_dir = r"C:\Users\oshsh\.gemini\antigravity\brain\ecf1b4ae-25a8-466d-bbc7-4c515cbd4d24"

targets = [
    os.path.join(workspace_dir, "slides.html"),
    os.path.join(workspace_dir, "public", "slides.html"),
    os.path.join(workspace_dir, "dist", "slides.html"),
    os.path.join(artifact_dir, "slides.html")
]

for t in targets:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    with open(t, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Wrote {len(html_content)} bytes to {t}")
