import os
import base64

ARTIFACT_DIR = r"C:\Users\oshsh\.gemini\antigravity\brain\ecf1b4ae-25a8-466d-bbc7-4c515cbd4d24"
SOURCE_DIR = r"C:\Users\oshsh\.gemini\antigravity\scratch\sih26056_airfare_cpi\public\presentation"

files = {
    "comp": os.path.join(SOURCE_DIR, "slide5_all_4_options_comparison.png"),
    "opt1": os.path.join(SOURCE_DIR, "slide5_option1.png"),
    "opt2": os.path.join(SOURCE_DIR, "slide5_option2.png"),
    "opt3": os.path.join(SOURCE_DIR, "slide5_option3.png"),
    "opt4": os.path.join(SOURCE_DIR, "slide5_option4.png"),
}

b64_data = {}
for k, path in files.items():
    with open(path, "rb") as f:
        b64_data[k] = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Slide 5 Layout Options Preview Gallery</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    .tab-btn.active {{
      background-color: #2563eb;
      color: #ffffff;
      border-color: #2563eb;
    }}
  </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen p-4 md:p-8">
  <div class="max-w-6xl mx-auto">
    <!-- Header -->
    <div class="flex flex-col md:flex-row md:items-center justify-between pb-6 border-b border-slate-800 gap-4">
      <div>
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-500/20 text-blue-400 border border-blue-500/30">SIH 2026</span>
          <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">PS ID: SIH26056</span>
          <span class="text-xs text-slate-400">Team Roorkies</span>
        </div>
        <h1 class="text-2xl md:text-3xl font-black text-white mt-1">Slide 5 Layout Preview: Impact & Benefits</h1>
        <p class="text-sm text-slate-400">Compare all 4 layout options side-by-side or inspect Full HD slide views.</p>
      </div>
      <div class="flex items-center gap-3">
        <a href="https://sih26056-airfare-cpi.vercel.app" target="_blank" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs rounded-lg transition-colors shadow">
          🚀 Open Live Prototype
        </a>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="flex flex-wrap gap-2 my-6">
      <button onclick="showTab('comp')" id="tab-comp" class="tab-btn active px-4 py-2 rounded-lg font-bold text-xs bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 transition-all">
        🔲 All 4 Options (Side-by-Side)
      </button>
      <button onclick="showTab('opt1')" id="tab-opt1" class="tab-btn px-4 py-2 rounded-lg font-bold text-xs bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 transition-all">
        1️⃣ Option 1: Split Left & Right Visual (Current)
      </button>
      <button onclick="showTab('opt2')" id="tab-opt2" class="tab-btn px-4 py-2 rounded-lg font-bold text-xs bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 transition-all">
        2️⃣ Option 2: Top 4-Column Benefits Grid
      </button>
      <button onclick="showTab('opt3')" id="tab-opt3" class="tab-btn px-4 py-2 rounded-lg font-bold text-xs bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 transition-all">
        3️⃣ Option 3: Left 2x2 Benefits Matrix
      </button>
      <button onclick="showTab('opt4')" id="tab-opt4" class="tab-btn px-4 py-2 rounded-lg font-bold text-xs bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 transition-all">
        4️⃣ Option 4: Three-Column Analytical Flow
      </button>
    </div>

    <!-- Content Sections -->
    <div id="view-comp" class="tab-view block">
      <div class="bg-slate-800/60 border border-slate-700/60 rounded-xl p-4 shadow-xl mb-4">
        <h3 class="text-sm font-bold text-slate-200 mb-2">Side-by-Side Comparison Matrix</h3>
        <p class="text-xs text-slate-400 mb-4">Click any option tab above to view the full resolution 1920×1080 slide.</p>
        <img src="data:image/png;base64,{b64_data['comp']}" alt="All 4 Options Comparison" class="w-full rounded-lg border border-slate-700 shadow-2xl" />
      </div>
    </div>

    <div id="view-opt1" class="tab-view hidden">
      <div class="bg-slate-800/60 border border-slate-700/60 rounded-xl p-4 shadow-xl mb-4">
        <div class="flex items-center justify-between mb-3">
          <div>
            <h3 class="text-sm font-bold text-blue-400">Option 1: Split Left Cards & Right Hero Chart (Current Master)</h3>
            <p class="text-xs text-slate-400">Prominent "POTENTIAL IMPACT" card at top left, 4 stacked horizontal benefit strips below it, and full-height hero prototype chart on the right.</p>
          </div>
          <span class="px-2 py-1 rounded bg-blue-500/20 text-blue-300 text-xs font-bold">Recommended</span>
        </div>
        <img src="data:image/png;base64,{b64_data['opt1']}" alt="Option 1 HD" class="w-full rounded-lg border border-slate-700 shadow-2xl" />
      </div>
    </div>

    <div id="view-opt2" class="tab-view hidden">
      <div class="bg-slate-800/60 border border-slate-700/60 rounded-xl p-4 shadow-xl mb-4">
        <div class="flex items-center justify-between mb-3">
          <div>
            <h3 class="text-sm font-bold text-emerald-400">Option 2: Top 4-Column Benefits Banner + Bottom Split</h3>
            <p class="text-xs text-slate-400">Full-width top banner with 4 side-by-side benefit pillars (Social, Economic, Environmental, Policy). Bottom split with Potential Impact on left and Prototype Chart on right.</p>
          </div>
        </div>
        <img src="data:image/png;base64,{b64_data['opt2']}" alt="Option 2 HD" class="w-full rounded-lg border border-slate-700 shadow-2xl" />
      </div>
    </div>

    <div id="view-opt3" class="tab-view hidden">
      <div class="bg-slate-800/60 border border-slate-700/60 rounded-xl p-4 shadow-xl mb-4">
        <div class="flex items-center justify-between mb-3">
          <div>
            <h3 class="text-sm font-bold text-purple-400">Option 3: Left 2x2 Benefits Grid + Top Impact Ribbon</h3>
            <p class="text-xs text-slate-400">Left column has a top impact ribbon plus a 2x2 grid of square benefit boxes. Right column preserves the full-height prototype dashboard chart.</p>
          </div>
        </div>
        <img src="data:image/png;base64,{b64_data['opt3']}" alt="Option 3 HD" class="w-full rounded-lg border border-slate-700 shadow-2xl" />
      </div>
    </div>

    <div id="view-opt4" class="tab-view hidden">
      <div class="bg-slate-800/60 border border-slate-700/60 rounded-xl p-4 shadow-xl mb-4">
        <div class="flex items-center justify-between mb-3">
          <div>
            <h3 class="text-sm font-bold text-amber-400">Option 4: Three-Column Analytical Flow</h3>
            <p class="text-xs text-slate-400">Three vertical pillars: Column 1 = Macro Impact (MoSPI/RBI/DGCA), Column 2 = Categorized Benefits (4 Cards), Column 3 = Working Prototype Evidence.</p>
          </div>
        </div>
        <img src="data:image/png;base64,{b64_data['opt4']}" alt="Option 4 HD" class="w-full rounded-lg border border-slate-700 shadow-2xl" />
      </div>
    </div>

    <!-- Benefit Content Summary Table -->
    <div class="mt-8 bg-slate-800/40 border border-slate-700/50 rounded-xl p-5">
      <h3 class="text-sm font-bold text-white mb-3">Mandatory SIH 2026 Benefits Included in All Options:</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
        <div class="p-3 bg-blue-900/20 border border-blue-500/30 rounded-lg">
          <span class="font-bold text-blue-400 block mb-1">👥 SOCIAL</span>
          <p class="text-slate-300">Public measurement: transparent, publicly checkable airfare-inflation data, relevant to UDAN regional travellers.</p>
        </div>
        <div class="p-3 bg-emerald-900/20 border border-emerald-500/30 rounded-lg">
          <span class="font-bold text-emerald-400 block mb-1">📈 ECONOMIC</span>
          <p class="text-slate-300">Monetary policy signals: leading transport-inflation indicator for RBI MPC; less manual field collection (savings under validation).</p>
        </div>
        <div class="p-3 bg-teal-900/20 border border-teal-500/30 rounded-lg">
          <span class="font-bold text-teal-400 block mb-1">🌱 ENVIRONMENTAL</span>
          <p class="text-slate-300">Reduced field commutes: less physical surveyor travel (qualitative only).</p>
        </div>
        <div class="p-3 bg-amber-900/20 border border-amber-500/30 rounded-lg">
          <span class="font-bold text-amber-400 block mb-1">🏛️ POLICY & INSTITUTIONAL</span>
          <p class="text-slate-300">Sovereign NSO feed: automated API ingestion into MoSPI eSankhyiki and NDAP; abnormal fare surges flagged to DGCA for review.</p>
        </div>
      </div>
    </div>
  </div>

  <script>
    function showTab(tabId) {{
      document.querySelectorAll('.tab-view').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.getElementById('view-' + tabId).classList.remove('hidden');
      document.getElementById('tab-' + tabId).classList.add('active');
    }}
  </script>
</body>
</html>
"""

target_path = os.path.join(ARTIFACT_DIR, "slide5_preview_gallery.html")
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated HTML preview gallery at {target_path}")
