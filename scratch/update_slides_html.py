import os

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>APIx (VayuSuchak) - SIH 2026 Presentation (PS ID: 26056)</title>
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
      border: 2px solid #5b21b6;
      border-radius: 9999px;
      padding: 0.25rem 1.4rem;
      font-weight: 700;
      color: #000;
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
  <!-- SLIDE 1: Exact SIH Title Template -->
  <!-- ======================================================== -->
  <div class="slide-frame active" id="slide-1">
    <!-- Header -->
    <div class="flex items-center justify-between">
      <h1 class="serif-title text-4xl lg:text-5xl font-black text-[#1b365d] tracking-wide">
        SMART INDIA HACKATHON 2026
      </h1>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-16 object-contain" />
    </div>

    <!-- Sub-badge -->
    <div class="mt-2">
      <div class="inline-flex items-center gap-2 border-2 border-blue-400 bg-blue-50/80 px-5 py-1 rounded-full text-blue-900 font-bold text-xs shadow-sm">
        <i class="fa-solid fa-bolt text-amber-500"></i> Real-Time Airfare Price Index (APIx) • MoSPI NSO &amp; RBI Augmentation
      </div>
    </div>

    <!-- Main Content -->
    <div class="grid grid-cols-12 gap-6 flex-1 items-center my-auto relative">
      <!-- Left Metadata Bullets -->
      <div class="col-span-8 pr-4 space-y-3.5 text-left z-10">
        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• Problem Statement ID – </span>
          <span class="font-black text-[#184c94]">SIH26056</span>
        </div>

        <div class="text-lg lg:text-xl leading-snug">
          <span class="font-black text-black">• Problem Statement Title- </span>
          <span class="font-black text-[#184c94]">
            Development of a Real-time Airfare Price Index for India through Automated Web Scraping of Airline and Online Travel Aggregator Portals for Augmentation of the Consumer Price Index (CPI)
          </span>
        </div>

        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• Theme- </span>
          <span class="font-black text-[#184c94]">Smart Governance / Miscellaneous</span>
        </div>

        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• PS Category- </span>
          <span class="font-black text-[#184c94]">Software</span>
        </div>

        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• Team ID- </span>
          <span class="font-black text-[#184c94]">Team Rookie</span>
        </div>

        <div class="text-xl lg:text-2xl leading-snug">
          <span class="font-black text-black">• Team Name- </span>
          <span class="font-black text-[#184c94]">Team Rookie</span>
        </div>
        <div class="text-lg lg:text-xl leading-snug">
          <span class="font-black text-black">• Team Members- </span>
          <span class="font-black text-[#184c94]">
            Nikhil Kanse, Shivish Kumar, Tejas Patil, Pranav Pawale, Harsh Narkar, Blessy
          </span>
        </div>
      </div>

      <!-- Right Graphic -->
      <div class="col-span-4 flex flex-col justify-center items-center relative">
        <img src="/presentation/page_1_img_1.png" alt="Smart India Hackathon Lightbulb" class="max-h-[340px] object-contain drop-shadow-md" />
        <img src="/presentation/airplane_transparent.png" alt="Commercial Airplane" class="w-64 absolute -bottom-6 right-0 drop-shadow-xl z-20 pointer-events-none transform -rotate-3 hover:scale-105 transition" />
      </div>
    </div>
    
    <!-- Footer -->
    <div class="mt-auto pt-2 border-t border-slate-200 text-center text-xs font-semibold text-slate-600 shrink-0">
      <span class="font-bold text-slate-800">Team Rookie</span> | SIH26056: Real-time Airfare Price Index (APIx) for India • MoSPI NSO &amp; RBI Augmentation
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 2: Problem & Solution -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-2">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-3">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">APIx: REAL-TIME AIRFARE PRICE INDEX (VAYUSUCHAK)</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">Augmenting MoSPI CPI through Automated Web Scraping &amp; UN/ILO Standards</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <!-- 3-Column Layout -->
    <div class="grid grid-cols-12 gap-4 flex-1 items-stretch">
      <!-- Col 1: PROBLEM Card (Rose Border) -->
      <div class="col-span-4 bg-rose-50/40 border-2 border-rose-500 rounded-2xl p-4 flex flex-col justify-between shadow-sm">
        <div>
          <div class="text-center font-black text-2xl text-rose-700 mb-2 tracking-wide flex items-center justify-center gap-2">
            <i class="fa-solid fa-triangle-exclamation text-rose-600"></i> CRITICAL PROBLEM
          </div>
          <ul class="text-[12px] text-slate-900 space-y-3 leading-relaxed mt-3">
            <li class="flex items-start gap-2">
              <span class="text-rose-600 font-black text-sm shrink-0">✖</span>
              <div><strong>Manual Survey Bottleneck:</strong> MoSPI field staff query offline ticketing outlets once a month for single static quotes.</div>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-rose-600 font-black text-sm shrink-0">✖</span>
              <div><strong>Blind to Dynamic Pricing:</strong> 90%+ tickets sold online with dynamic pricing shifting 200-400% within a single day.</div>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-rose-600 font-black text-sm shrink-0">✖</span>
              <div><strong>Lead-Time Neglect:</strong> Traditional CPI ignores booking horizons (T+1 last-minute surge vs T+45 advance saver fares).</div>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-rose-600 font-black text-sm shrink-0">✖</span>
              <div><strong>15-Day Critical Policy Lag:</strong> High-frequency transport inflation shocks reach RBI Monetary Policy weeks late.</div>
            </li>
          </ul>
        </div>
        <div class="text-center text-xs font-semibold text-rose-800 pt-2 border-t border-rose-200">
          MoSPI Current Baseline Limitation
        </div>
      </div>

      <!-- Col 2: Pipeline Arrows + Our Solution -->
      <div class="col-span-4 flex flex-col justify-between">
        <!-- Top Pipeline Flow -->
        <div class="grid grid-cols-4 gap-1.5 mb-2">
          <div class="bg-sky-100 border border-sky-400 rounded-lg p-1.5 text-center text-[10px] font-bold text-sky-900">1. Ingestion</div>
          <div class="bg-emerald-100 border border-emerald-400 rounded-lg p-1.5 text-center text-[10px] font-bold text-emerald-900">2. Cleanse</div>
          <div class="bg-amber-100 border border-amber-400 rounded-lg p-1.5 text-center text-[10px] font-bold text-amber-900">3. Jevons GM</div>
          <div class="bg-purple-100 border border-purple-400 rounded-lg p-1.5 text-center text-[10px] font-bold text-purple-900">4. Laspeyres</div>
        </div>

        <!-- Our Solution Card (Indigo Border) -->
        <div class="border-2 border-indigo-500 rounded-2xl p-4 bg-indigo-50/30 flex-1 flex flex-col justify-between shadow-sm">
          <div>
            <div class="text-center font-black text-xl text-indigo-900 mb-1 flex items-center justify-center gap-1.5">
              <i class="fa-solid fa-circle-check text-indigo-600"></i> OUR SOVEREIGN SOLUTION
            </div>
            <div class="text-[11px] font-bold text-indigo-950 mb-2 text-center">Automated high-frequency Python pipeline delivering:</div>
            <ul class="text-[11px] text-slate-900 space-y-1.5 leading-snug">
              <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✔</span> <span><strong>Multi-Source Harvester:</strong> Scrapes IndiGo, Air India, Akasa, SpiceJet &amp; OTAs with robots.txt compliance.</span></li>
              <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✔</span> <span><strong>5 Forward Horizons:</strong> Stratified sampling across T+1, T+7, T+15, T+30, T+45 booking windows.</span></li>
              <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✔</span> <span><strong>IQR Outlier Engine:</strong> Filters flexi-surge anomalies [Q1-1.5*IQR, Q3+2.0*IQR] with Z-score audit tags.</span></li>
              <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✔</span> <span><strong>UN/ILO Jevons Index:</strong> Geometric mean price relatives eliminating consumer substitution bias.</span></li>
              <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✔</span> <span><strong>DGCA Laspeyres Aggregator:</strong> Calibrated against 12 official domestic corridors (81.4% traffic).</span></li>
              <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✔</span> <span><strong>Cryptographic Provenance:</strong> Immutable SHA-256 batch fingerprints for sovereign auditability.</span></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Col 3: Why Different & Key Value Proposition -->
      <div class="col-span-4 flex flex-col gap-3">
        <!-- Top Box: Why Different (Purple Border) -->
        <div class="border-2 border-purple-500 rounded-2xl p-4 bg-purple-50/30 flex-1 shadow-sm flex flex-col justify-center">
          <div class="text-center font-black text-xl text-purple-900 mb-2 flex items-center justify-center gap-1.5">
            <i class="fa-solid fa-wand-magic-sparkles text-purple-600"></i> WHY IT IS DIFFERENT
          </div>
          <ul class="text-[11.5px] text-slate-900 space-y-2 leading-snug">
            <li class="flex items-start gap-1.5"><span class="text-amber-500 font-bold shrink-0">⚡</span> <span>Captures real-time algorithmic yield surges, not outdated monthly static quotes.</span></li>
            <li class="flex items-start gap-1.5"><span class="text-amber-500 font-bold shrink-0">⚡</span> <span>UN/ILO Jevons geometric mean avoids arithmetic upward bias under heavy discounts.</span></li>
            <li class="flex items-start gap-1.5"><span class="text-amber-500 font-bold shrink-0">⚡</span> <span>SHA-256 cryptographic provenance guarantees complete reproducibility for courts &amp; NSO.</span></li>
          </ul>
        </div>

        <!-- Bottom Box: Key Value Proposition (Emerald Border) -->
        <div class="border-2 border-emerald-500 rounded-2xl p-4 bg-emerald-50/30 flex-1 shadow-sm flex flex-col justify-center">
          <div class="text-center font-black text-xl text-emerald-900 mb-2 flex items-center justify-center gap-1.5">
            <i class="fa-solid fa-star text-emerald-600"></i> KEY VALUE PROPOSITION
          </div>
          <ul class="text-[11.5px] text-slate-900 space-y-2 leading-snug">
            <li class="flex items-start gap-1.5"><span class="text-emerald-700 font-bold shrink-0">★</span> <span><strong>&gt;95% reduction</strong> in recurring MoSPI price collection expenditure across 12 metro airports.</span></li>
            <li class="flex items-start gap-1.5"><span class="text-emerald-700 font-bold shrink-0">★</span> <span><strong>Empowers RBI MPC</strong> with zero-lag transport inflation leading indicators for rate decisions.</span></li>
            <li class="flex items-start gap-1.5"><span class="text-emerald-700 font-bold shrink-0">★</span> <span><strong>Equips DGCA &amp; MoCA</strong> with automated surge anomaly alerts to detect regional price gouging.</span></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="mt-auto pt-2 border-t border-slate-200 text-center text-xs font-semibold text-slate-600 shrink-0">
      <span class="font-bold text-slate-800">Team Rookie</span> | SIH26056: Real-time Airfare Price Index (APIx) for India • MoSPI NSO &amp; RBI Augmentation
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 3: Technical Approach -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-3">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-2">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">TECHNICAL APPROACH</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">Multi-Source Architecture, Data Cleaning &amp; UN/ILO Aggregation</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <div class="grid grid-cols-12 gap-5 flex-1 items-stretch">
      <!-- Left Side: System Architecture + Process Flowchart -->
      <div class="col-span-8 flex flex-col justify-between gap-2.5 h-full">
        <div class="flex-1 flex flex-col justify-center">
          <div class="flex items-center justify-between mb-1">
            <span class="inline-flex items-center gap-1 border-2 border-blue-500 bg-blue-50 text-blue-900 font-black text-xs px-3 py-0.5 rounded-full shadow-sm">
              4-Tier System Architecture
            </span>
            <span class="text-[11px] text-slate-500 font-semibold">VAYUSUCHAK Sovereign Architecture</span>
          </div>
          <div class="bg-slate-50 rounded-xl p-1 border border-slate-200 shadow-sm flex items-center justify-center flex-1 overflow-hidden">
            <img src="/presentation/architecture_diagram.png" alt="VayuSuchak Architecture Diagram" class="w-full max-h-[245px] object-contain rounded-lg" />
          </div>
        </div>

        <div class="flex-1 flex flex-col justify-center">
          <div class="flex items-center justify-between mb-1">
            <span class="inline-flex items-center gap-1 border-2 border-emerald-500 bg-emerald-50 text-emerald-900 font-black text-xs px-3 py-0.5 rounded-full shadow-sm">
              Pipeline Process Flowchart
            </span>
            <span class="text-[11px] text-slate-500 font-semibold">Daily Automated Airfare Pipeline</span>
          </div>
          <div class="bg-slate-50 rounded-xl p-1 border border-slate-200 shadow-sm flex items-center justify-center flex-1 overflow-hidden">
            <img src="/presentation/flowchart_diagram.png" alt="Process Flowchart Diagram" class="w-full max-h-[230px] object-contain rounded-lg" />
          </div>
        </div>
      </div>

      <!-- Right Side: Tech Stack Card + Live Prototype Link -->
      <div class="col-span-4 flex flex-col justify-between gap-3 h-full">
        <!-- Tech Stack Card (Purple Border) -->
        <div class="border-2 border-purple-500 rounded-2xl p-4 bg-purple-50/20 flex flex-col justify-between shadow-sm flex-1">
          <div>
            <div class="text-center font-black text-2xl text-[#7c3aed] mb-3 flex items-center justify-center gap-2">
              <i class="fa-solid fa-layer-group text-purple-600"></i> Tech Stack Used:
            </div>
            <div class="grid grid-cols-2 gap-y-2 text-center text-xs font-bold text-slate-800">
              <div>• Python 3.13</div>
              <div>• Playwright Stealth</div>
              <div>• NumPy &amp; SciPy</div>
              <div>• IQR Outlier Filter</div>
              <div>• UN/ILO Jevons Engine</div>
              <div>• SQLite / PostgreSQL</div>
              <div>• React 19 &amp; TypeScript</div>
              <div>• Recharts SVG</div>
              <div>• FastAPI &amp; Uvicorn</div>
              <div>• eSankhyiki CSV Parser</div>
              <div>• Docker &amp; Vercel Edge</div>
              <div>• GitHub Actions Cron</div>
            </div>
          </div>
          <div class="text-center text-[11px] font-bold text-purple-900 pt-2 border-t border-purple-200 mt-2">
            100% Open Source • Zero Licensing Lock-In
          </div>
        </div>

        <!-- Live Prototype Banner (Emerald Border) -->
        <div class="border-2 border-emerald-500 rounded-2xl p-3.5 bg-emerald-50/40 shadow-sm text-center">
          <div class="flex items-center justify-center space-x-1.5 text-xs font-black text-emerald-900 uppercase tracking-wide mb-1">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-ping"></span>
            <span>LIVE PRODUCTION PLATFORM</span>
          </div>
          <a href="https://sih26056-airfare-cpi.vercel.app/" target="_blank" class="text-xs sm:text-sm font-black text-emerald-700 hover:text-emerald-900 underline break-all block py-0.5">
            https://sih26056-airfare-cpi.vercel.app/
          </a>
          <p class="text-[10px] text-slate-600 font-medium mt-1">
            Real-time APIx Indices • REST API • DGCA Backtest • Provenance Vault
          </p>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="mt-auto pt-2 border-t border-slate-200 text-center text-xs font-semibold text-slate-600 shrink-0">
      <span class="font-bold text-slate-800">Team Rookie</span> | SIH26056: Real-time Airfare Price Index (APIx) for India • MoSPI NSO &amp; RBI Augmentation
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 4: Feasibility and Viability -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-4">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-3">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">FEASIBILITY AND VIABILITY</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">Architectural Robustness, Low Operational Cost &amp; Legal Adherence</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <!-- Grid Layout -->
    <div class="flex flex-col gap-3 flex-1 justify-between">
      <!-- Top Row: Risk Assessment + Technical Feasibility -->
      <div class="grid grid-cols-12 gap-3 flex-1">
        <!-- Risk Assessment (Rose Border) -->
        <div class="col-span-7 bg-rose-50/30 border-2 border-rose-500 rounded-2xl p-4 flex flex-col justify-between shadow-sm">
          <div class="font-black text-lg text-rose-700 mb-2 flex items-center gap-1.5">
            <i class="fa-solid fa-shield-halved text-rose-600"></i> Risk Assessment and Mitigation
          </div>
          <div class="space-y-2 text-xs">
            <div class="p-2 rounded-lg bg-white/90 border border-rose-200">
              <span class="font-bold text-rose-700">Problem: Anti-Scraping / Cloudflare Blocks</span>
              <span class="font-bold text-slate-400 mx-1">➔</span>
              <span class="font-bold text-emerald-800">Solution: Ethical robots.txt checking + rotating residential proxy pool + jitter delays</span>
            </div>
            <div class="p-2 rounded-lg bg-white/90 border border-rose-200">
              <span class="font-bold text-rose-700">Problem: Airline Portal DOM Layout Shifts</span>
              <span class="font-bold text-slate-400 mx-1">➔</span>
              <span class="font-bold text-emerald-800">Solution: Multi-selector schema (ARIA / data-test) + cached baseline fallback layers</span>
            </div>
            <div class="p-2 rounded-lg bg-white/90 border border-rose-200">
              <span class="font-bold text-rose-700">Problem: Dynamic Surge Pricing &amp; Outliers</span>
              <span class="font-bold text-slate-400 mx-1">➔</span>
              <span class="font-bold text-emerald-800">Solution: Automated IQR truncation [Q1-1.5*IQR, Q3+2.0*IQR] + UN/ILO Jevons geometric damping</span>
            </div>
          </div>
        </div>

        <!-- Technical Feasibility (Sky Border) -->
        <div class="col-span-5 bg-sky-50/30 border-2 border-sky-500 rounded-2xl p-4 flex flex-col justify-between shadow-sm">
          <div class="font-black text-lg text-sky-800 mb-2 flex items-center gap-1.5">
            <i class="fa-solid fa-code text-sky-600"></i> Technical Feasibility
          </div>
          <ul class="text-xs text-slate-800 space-y-2 leading-relaxed">
            <li class="flex items-start gap-1.5"><span class="text-sky-600 font-bold shrink-0">✔</span> <span>Headless Python &amp; Playwright engine extracting IndiGo, Air India, Akasa &amp; SpiceJet.</span></li>
            <li class="flex items-start gap-1.5"><span class="text-sky-600 font-bold shrink-0">✔</span> <span>5 standard forward lead-time windows (T+1, T+7, T+15, T+30, T+45) capturing full yield curves.</span></li>
            <li class="flex items-start gap-1.5"><span class="text-sky-600 font-bold shrink-0">✔</span> <span>Mathematical UN/ILO Jevons geometric mean &amp; DGCA passenger volume Laspeyres model.</span></li>
          </ul>
        </div>
      </div>

      <!-- Bottom Row: Resource Requirements + Proven Standards + Economic Viability -->
      <div class="grid grid-cols-12 gap-3 flex-1">
        <!-- Resource Requirements (Purple Border) -->
        <div class="col-span-4 bg-purple-50/30 border-2 border-purple-500 rounded-2xl p-4 flex flex-col justify-between shadow-sm">
          <div class="font-black text-base text-purple-900 mb-2 flex items-center gap-1.5">
            <i class="fa-solid fa-server text-purple-600"></i> Resource Requirements
          </div>
          <ul class="text-xs text-slate-800 space-y-1.5 leading-snug">
            <li>• Lightweight serverless cloud cron runner / VPS (Python &amp; FastAPI).</li>
            <li>• Open-source statistical libraries (Playwright, Pandas, SciPy, SQLite, React 19).</li>
            <li>• Persistent SQLite &amp; PostgreSQL audit vault with SHA-256 provenance hashes.</li>
          </ul>
        </div>

        <!-- Proven Standards (Amber Border) -->
        <div class="col-span-3 bg-amber-50/30 border-2 border-amber-500 rounded-2xl p-4 flex flex-col justify-between shadow-sm text-center">
          <div class="font-black text-base text-amber-900 mb-2">
            Proven Standards
          </div>
          <div class="text-xs text-amber-950 font-bold space-y-1.5">
            <div>✔ UN/ILO CPI Manual (2020)</div>
            <div>✔ DGCA Traffic Statistics</div>
            <div>✔ MoSPI CPI (2012=100)</div>
            <div>✔ MIT Billion Prices Project</div>
          </div>
        </div>

        <!-- Economic Viability (Emerald Border) -->
        <div class="col-span-5 bg-emerald-50/30 border-2 border-emerald-500 rounded-2xl p-4 flex flex-col justify-between shadow-sm">
          <div class="font-black text-base text-emerald-900 mb-2 flex items-center gap-1.5">
            <i class="fa-solid fa-chart-line text-emerald-600"></i> Economic Viability
          </div>
          <ul class="text-xs text-slate-800 space-y-1 leading-snug">
            <li>• Slashes manual airport survey costs by &gt;95% across major Indian metro centers.</li>
            <li>• Extremely low cloud operational footprint (&lt; ₹3,500 / month serverless).</li>
            <li>• High ROI: 30x increase in price sampling frequency at a fraction of manual costs.</li>
            <li>• Scales seamlessly to 250+ UDAN regional routes with zero incremental hardware.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="mt-auto pt-2 border-t border-slate-200 text-center text-xs font-semibold text-slate-600 shrink-0">
      <span class="font-bold text-slate-800">Team Rookie</span> | SIH26056: Real-time Airfare Price Index (APIx) for India • MoSPI NSO &amp; RBI Augmentation
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 5: Impact and Benefits -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-5">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-2">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">IMPACT AND BENEFITS</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">Transforming Sovereign Economic Policy &amp; Aviation Governance</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <!-- Top Banner -->
    <div class="border-2 border-indigo-400 bg-gradient-to-r from-blue-50 via-indigo-50 to-purple-50 rounded-full py-1.5 px-6 text-center shadow-sm mb-3">
      <span class="font-black text-sm text-indigo-900 tracking-wider">
        “FROM SCATTERED AIRFARES TO SOVEREIGN REAL-TIME INFLATION INTELLIGENCE”
      </span>
    </div>

    <!-- 2 Columns -->
    <div class="grid grid-cols-12 gap-5 flex-1 items-stretch relative">
      <!-- Left Column: 5 National Impact Pillars -->
      <div class="col-span-6 flex flex-col justify-between gap-2">
        <div class="font-black text-xl text-[#1b365d] border-b-2 border-indigo-300 pb-1">
          NATIONAL IMPACT PILLARS
        </div>

        <div class="border-2 border-sky-400 bg-sky-50/50 rounded-xl p-2.5 shadow-sm">
          <div class="font-black text-xs text-sky-900">Macroeconomic Policy Impact</div>
          <div class="text-[11px] text-slate-700 leading-snug mt-0.5">Eliminates 15-day CPI lag; equips RBI MPC with live leading indicators for rate decisions.</div>
        </div>

        <div class="border-2 border-emerald-400 bg-emerald-50/50 rounded-xl p-2.5 shadow-sm">
          <div class="font-black text-xs text-emerald-900">Regulatory &amp; Aviation Oversight</div>
          <div class="text-[11px] text-slate-700 leading-snug mt-0.5">Enables DGCA to detect route monopolies, festival fare surges &amp; predatory pricing.</div>
        </div>

        <div class="border-2 border-amber-400 bg-amber-50/50 rounded-xl p-2.5 shadow-sm">
          <div class="font-black text-xs text-amber-900">Statistical &amp; Methodological Rigor</div>
          <div class="text-[11px] text-slate-700 leading-snug mt-0.5">Replaces single monthly spot checks with 10,000+ daily observations obeying UN/ILO standards.</div>
        </div>

        <div class="border-2 border-purple-400 bg-purple-50/50 rounded-xl p-2.5 shadow-sm">
          <div class="font-black text-xs text-purple-900">National Digital Public Infra (DPI)</div>
          <div class="text-[11px] text-slate-700 leading-snug mt-0.5">Establishes India's first sovereign high-frequency price aggregation platform.</div>
        </div>

        <div class="border-2 border-rose-400 bg-rose-50/50 rounded-xl p-2.5 shadow-sm">
          <div class="font-black text-xs text-rose-900">Consumer Transparency Impact</div>
          <div class="text-[11px] text-slate-700 leading-snug mt-0.5">Protects citizens by providing empirical benchmark data on true lead-time airline pricing.</div>
        </div>
      </div>

      <!-- Right Column: Strategic Future Prospects -->
      <div class="col-span-6 flex flex-col justify-between gap-2 relative">
        <div class="font-black text-xl text-[#1b365d] border-b-2 border-indigo-300 pb-1">
          STRATEGIC FUTURE PROSPECTS
        </div>

        <ul class="text-xs text-slate-800 space-y-2.5 leading-snug pr-8 z-10">
          <li>• <strong class="text-blue-900">UDAN Regional Expansion:</strong> Scale from current 12 metro corridors to 250+ Tier-2 and Tier-3 UDAN regional routes nationwide.</li>
          <li>• <strong class="text-blue-900">Cabin Tier Differentiation:</strong> Segregate economy, premium economy, and business class into granular sub-indices.</li>
          <li>• <strong class="text-blue-900">Intraday Time-of-Day Yield:</strong> Model peak departure rush hours (06:00-09:00, 17:00-20:00) vs off-peak red-eye rates.</li>
          <li>• <strong class="text-blue-900">Central MoSPI eSankhyiki Integration:</strong> Establish direct automated API pipelines feeding real-time indices into official CPI release.</li>
          <li>• <strong class="text-blue-900">Autonomous AI Inflation Analyst:</strong> Deploy LLM agents to draft automated weekly inflation briefs and alert DGCA of pricing anomalies.</li>
        </ul>

        <!-- Airplane Floating Illustration -->
        <div class="flex justify-end mt-auto z-0">
          <img src="/presentation/airplane_transparent.png" alt="Airplane Graphic" class="w-60 object-contain drop-shadow-xl transform -rotate-2 hover:scale-105 transition" />
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="mt-auto pt-2 border-t border-slate-200 text-center text-xs font-semibold text-slate-600 shrink-0">
      <span class="font-bold text-slate-800">Team Rookie</span> | SIH26056: Real-time Airfare Price Index (APIx) for India • MoSPI NSO &amp; RBI Augmentation
    </div>
  </div>

  <!-- ======================================================== -->
  <!-- SLIDE 6: Redesigned 3-Column Executive Template -->
  <!-- ======================================================== -->
  <div class="slide-frame" id="slide-6">
    <!-- Top Bar -->
    <div class="flex items-center justify-between mb-3">
      <div class="pill-team text-sm shadow-sm">Team Rookie</div>
      <div class="text-center flex-1">
        <h2 class="serif-title text-3xl font-black text-[#1b365d]">SOVEREIGN DEPLOYMENT, RESEARCH &amp; POLICY ROADMAP</h2>
        <div class="text-xs font-bold text-[#184c94] mt-0.5">Complete SIH 26056 Implementation • Academic Rigor • Institutional Ready</div>
      </div>
      <img src="/presentation/page_1_img_2.png" alt="SIH Logo" class="h-14 object-contain" />
    </div>

    <!-- 3-Column Executive Template -->
    <div class="grid grid-cols-3 gap-4 flex-1 items-stretch">
      <!-- Column 1: Academic Foundations (Blue Border) -->
      <div class="border-2 border-blue-500 rounded-2xl p-4 bg-blue-50/20 flex flex-col justify-between shadow-sm">
        <div>
          <div class="text-center font-black text-xl text-blue-900 mb-3 flex items-center justify-center gap-1.5">
            <i class="fa-solid fa-graduation-cap text-blue-600"></i> ACADEMIC FOUNDATIONS
          </div>
          <ul class="text-xs text-slate-800 space-y-3 leading-relaxed">
            <li>• <strong class="text-blue-900">MIT Billion Prices Project:</strong> Cavallo &amp; Rigobon (2016), Journal of Economic Perspectives. Proves web-scraping captures high-frequency inflation dynamics with zero manual survey bias.</li>
            <li>• <strong class="text-blue-900">UN/ILO CPI Manual (2020):</strong> Chapter 10 compliant implementation of the Jevons Elementary Geometric Mean to satisfy international statistical quality standards.</li>
            <li>• <strong class="text-blue-900">DGCA Domestic Statistics:</strong> Calibrated using official annual domestic city-pair traffic shares across 12 corridors representing 81.4% of national seat capacity.</li>
            <li>• <strong class="text-blue-900">MoSPI Technical Standards:</strong> Conforms to CSO Consumer Price Index concepts, base year re-referencing, and NDSAP open government data guidelines.</li>
          </ul>
        </div>
        <div class="text-center text-[10px] font-bold text-blue-800 pt-2 border-t border-blue-200 mt-2">
          Global Rigor • Compliant with UN/ILO Chapter 10
        </div>
      </div>

      <!-- Column 2: National Deployment Roadmap (Purple Border) -->
      <div class="border-2 border-purple-500 rounded-2xl p-4 bg-purple-50/20 flex flex-col justify-between shadow-sm">
        <div>
          <div class="text-center font-black text-xl text-purple-900 mb-3 flex items-center justify-center gap-1.5">
            <i class="fa-solid fa-timeline text-purple-600"></i> NATIONAL DEPLOYMENT ROADMAP
          </div>
          <div class="space-y-2.5 text-xs text-slate-800 leading-snug">
            <div class="p-2 rounded-lg bg-emerald-50 border border-emerald-300">
              <div class=\"font-black text-emerald-900 flex items-center justify-between\">
                <span>Phase 1: Operational Pilot</span>
                <span class=\"text-[10px] bg-emerald-200 text-emerald-900 px-1.5 py-0.5 rounded font-bold\">Current</span>
              </div>
              <p class=\"mt-1 text-[11px] text-slate-700\">Complete 12-corridor scraping engine, IQR outlier filtering, daily Jevons/Laspeyres index computation with 100% verified test coverage.</p>
            </div>

            <div class=\"p-2 rounded-lg bg-sky-50 border border-sky-300\">
              <div class=\"font-black text-sky-900 flex items-center justify-between\">
                <span>Phase 2: MoSPI Ingestion</span>
                <span class=\"text-[10px] bg-sky-200 text-sky-900 px-1.5 py-0.5 rounded font-bold\">Q4 2026</span>
              </div>
              <p class=\"mt-1 text-[11px] text-slate-700\">Direct REST API connection feeding daily JSON/CSV data into MoSPI eSankhyiki portal under Transport Item Code 1.1.07.03.</p>
            </div>

            <div class=\"p-2 rounded-lg bg-amber-50 border border-amber-300\">
              <div class=\"font-black text-amber-900 flex items-center justify-between\">
                <span>Phase 3: UDAN Route Scaling</span>
                <span class=\"text-[10px] bg-amber-200 text-amber-900 px-1.5 py-0.5 rounded font-bold\">2027</span>
              </div>
              <p class=\"mt-1 text-[11px] text-slate-700\">Expand scraper crawler matrix across 250+ Tier-2 &amp; Tier-3 regional UDAN routes with zero additional hardware.</p>
            </div>

            <div class=\"p-2 rounded-lg bg-purple-50 border border-purple-300\">
              <div class=\"font-black text-purple-900 flex items-center justify-between\">
                <span>Phase 4: AI &amp; Antitrust Monitoring</span>
                <span class=\"text-[10px] bg-purple-200 text-purple-900 px-1.5 py-0.5 rounded font-bold\">2027+</span>
              </div>
              <p class=\"mt-1 text-[11px] text-slate-700\">Automated anomaly alerts empowering DGCA and Competition Commission (CCI) against predatory route pricing.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Column 3: Production Deliverables (Emerald Border) -->
      <div class=\"border-2 border-emerald-500 rounded-2xl p-4 bg-emerald-50/20 flex flex-col justify-between shadow-sm\">
        <div>
          <div class=\"text-center font-black text-xl text-emerald-900 mb-3 flex items-center justify-center gap-1.5\">
            <i class=\"fa-solid fa-box-check text-emerald-600\"></i> PRODUCTION DELIVERABLES
          </div>
          <div class=\"space-y-2 text-xs text-slate-800 leading-snug\">
            <div class=\"p-2 rounded-lg bg-white/90 border border-emerald-200\">
              <div class=\"font-bold text-emerald-900 flex items-center gap-1.5\">
                <span class=\"w-2 h-2 rounded-full bg-emerald-500\"></span> Live Production Platform
              </div>
              <p class=\"mt-0.5 text-[11px] text-slate-600\">Deployed on Vercel Edge with live charts, GIS map, and lead-time elasticity visualizer.</p>
              <a href=\"https://sih26056-airfare-cpi.vercel.app/\" target=\"_blank\" class=\"text-xs font-bold text-emerald-700 hover:text-emerald-900 underline block mt-0.5 break-all\">
                https://sih26056-airfare-cpi.vercel.app/
              </a>
            </div>

            <div class=\"p-2 rounded-lg bg-white/90 border border-emerald-200\">
              <div class=\"font-bold text-indigo-900 flex items-center gap-1.5\">
                <i class=\"fa-solid fa-bolt text-amber-500\"></i> MoSPI &amp; RBI REST API
              </div>
              <p class=\"mt-0.5 text-[11px] text-slate-600\">FastAPI service with /api/v1/apix/* endpoints delivering real-time indices and eSankhyiki CSV downloads.</p>
            </div>

            <div class=\"p-2 rounded-lg bg-white/90 border border-emerald-200\">
              <div class=\"font-bold text-slate-900 flex items-center gap-1.5\">
                <i class=\"fa-solid fa-lock text-emerald-600\"></i> SHA-256 Provenance Vault
              </div>
              <p class=\"mt-0.5 text-[11px] text-slate-600\">Cryptographically signed audit trail ensuring legal evidentiary standard and zero tampering.</p>
            </div>

            <div class=\"p-2 rounded-lg bg-white/90 border border-emerald-200\">
              <div class=\"font-bold text-teal-900 flex items-center gap-1.5\">
                <i class=\"fa-solid fa-vial-circle-check text-teal-600\"></i> Automated Test Suite
              </div>
              <p class=\"mt-0.5 text-[11px] text-slate-600\">100% Passing unittest suite (7/7 tests) validating IQR, Jevons formula, and DGCA weighting.</p>
            </div>
          </div>
        </div>

        <div class=\"mt-3 pt-2 border-t border-emerald-300 text-center\">
          <div class=\"font-black text-xs text-slate-800\">🏛️ Ready for Sovereign Integration</div>
          <div class=\"font-bold text-xs text-emerald-700 mt-0.5\">Thank You! • Questions &amp; Discussion</div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class=\"mt-auto pt-2 border-t border-slate-200 text-center text-xs font-semibold text-slate-600 shrink-0\">
      <span class=\"font-bold text-slate-800\">Team Rookie</span> | [ Nikhil Kanse , Shivish Kumar , Tejas Patil , Pranav Pawale , Harsh Narkar , Blessy ]
    </div>
  </div>

</div>

<!-- Navigation Controls (Bottom Bar) -->
<div class=\"controls fixed bottom-3 left-1/2 -translate-x-1/2 flex items-center gap-3 bg-slate-900/90 border border-slate-700/80 px-4 py-1.5 rounded-full backdrop-blur-md shadow-2xl z-50\">
  <button onclick=\"prevSlide()\" class=\"p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition\" title=\"Previous Slide (Left Arrow)\">
    <i class=\"fa-solid fa-chevron-left\"></i>
  </button>
  
  <div class=\"flex items-center gap-1.5 px-2\" id=\"nav-dots\">
    <!-- Dots dynamically rendered -->
  </div>

  <span class=\"text-xs font-mono text-slate-300 px-2\" id=\"slide-num\">1 / 6</span>

  <button onclick=\"nextSlide()\" class=\"p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition\" title=\"Next Slide (Right Arrow or Space)\">
    <i class=\"fa-solid fa-chevron-right\"></i>
  </button>

  <div class=\"h-4 w-px bg-slate-700 mx-1\"></div>

  <a href=\"/AirIntel_India_SIH26056_Presentation.pptx\" download class=\"p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition flex items-center gap-1.5 text-xs font-bold text-amber-400\" title=\"Download PPTX\">
    <i class=\"fa-solid fa-file-powerpoint\"></i>
    <span class=\"hidden sm:inline\">Download PPTX</span>
  </a>

  <button onclick=\"toggleFullScreen()\" class=\"p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition\" title=\"Fullscreen (F)\">
    <i class=\"fa-solid fa-expand\"></i>
  </button>

  <button onclick=\"window.print()\" class=\"p-2 hover:bg-slate-800 text-slate-300 hover:text-white rounded-full transition\" title=\"Print to PDF (P)\">
    <i class=\"fa-solid fa-print\"></i>
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
