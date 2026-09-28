import React, { useState } from 'react';
import { X, Play, Clock, CheckCircle2, Copy, Video, ChevronRight, Sparkles, ExternalLink, Volume2 } from 'lucide-react';

interface VideoDemoGuideModalProps {
  isOpen: boolean;
  onClose: () => void;
  onOpenProvenance: () => void;
  onOpenRestApi: () => void;
  onOpenExport: () => void;
  onOpenOutlierModal: () => void;
  setActiveTab: (tab: 'overview' | 'corridors' | 'scraper' | 'methodology') => void;
}

interface Scene {
  id: number;
  time: string;
  actTitle: string;
  componentTitle: string;
  targetElementId?: string;
  actionText: string;
  script: string;
  evaluatorTakeaway: string;
  interactiveAction?: () => void;
  interactiveLabel?: string;
}

export const VideoDemoGuideModal: React.FC<VideoDemoGuideModalProps> = ({
  isOpen,
  onClose,
  onOpenProvenance,
  onOpenRestApi,
  onOpenExport,
  onOpenOutlierModal,
  setActiveTab,
}) => {
  const [activeSceneIndex, setActiveSceneIndex] = useState(0);
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);

  if (!isOpen) return null;

  const scrollToComponent = (elementId?: string) => {
    if (!elementId) return;
    setActiveTab('overview');
    setTimeout(() => {
      const el = document.getElementById(elementId);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.classList.add('ring-4', 'ring-sky-500', 'transition-all', 'duration-500');
        setTimeout(() => {
          el.classList.remove('ring-4', 'ring-sky-500');
        }, 2000);
      }
    }, 100);
  };

  const scenes: Scene[] = [
    {
      id: 1,
      time: "0:00 - 0:35",
      actTitle: "Act 1: Executive Hook & The MoSPI Crisis",
      componentTitle: "Header Ribbon & Problem Framing",
      targetElementId: "cpi-metrics-overview",
      actionText: "Start at top ticker ribbon. Point to 'APIx • VayuSuchak | SIH 26056 | Team Roorkies (168405)'.",
      script:
        "Respected jury members and evaluators from MoSPI. We are Team Roorkies, presenting our solution for SIH26056: VayuSuchak (वायु सूचक) — a sovereign, real-time Airfare Price Index for India.\n\nToday, India's CPI Transport Sub-Index relies on manual field surveyors visiting airline counters once a month. This introduces a 15-day reporting lag, collects only 1 static quote per route, and applies the Dutot arithmetic mean formula that structurally overstates inflation by 20 to 30 basis points due to substitution bias.\n\nVayuSuchak replaces manual paper surveys with an automated, tamper-proof, high-frequency intelligence platform. Let's walk through the live architecture.",
      evaluatorTakeaway: "Clear problem framing: 15-day lag + 1-quote snapshot + Dutot upward bias.",
    },
    {
      id: 2,
      time: "0:35 - 1:15",
      actTitle: "Act 2: Real-Time Index & Macro Impact",
      componentTitle: "KPI Overview & Transmission Chain",
      targetElementId: "cpi-metrics-overview",
      actionText: "Hover over the 4 top KPI cards (Jevons Index, Dutot Bias, Today's Avg Fare, Outlier Count), then scroll to Macroeconomic Transmission Chain.",
      script:
        "At the top of our dashboard, evaluators can inspect our real-time core metrics. Unlike monthly snapshots, our system calculates the Jevons Geometric Mean Index continuously with base 2024=100.\n\nNotice Card 2: our engine explicitly isolates the Dutot Arithmetic Distortion (+25 bps). Because arithmetic averages fail the axiomatic time-reversal and substitution tests, legacy surveys overstate airfare inflation. Our Jevons engine mathematically eliminates this bias.\n\nDirectly below, our Macroeconomic Transmission Chain visualizes how an 11.4% surge in airfare transmits directly through the transport basket into headline CPI, ultimately influencing RBI's repo rate decisions.",
      evaluatorTakeaway: "Demonstrates axiomatic bias elimination and monetary policy relevance for RBI/MoSPI.",
      interactiveAction: () => {
        scrollToComponent('cpi-metrics-overview');
      },
      interactiveLabel: "Scroll to KPI Overview",
    },
    {
      id: 3,
      time: "1:15 - 2:05",
      actTitle: "Act 3: Advance Booking Dynamic Yield ($T+1..T+45$)",
      componentTitle: "Lead Time Elasticity & Monthly Index",
      targetElementId: "lead-time-elasticity-card",
      actionText: "Click the horizon buttons (1d, 7d, 15d, 45d, ALL) to show live elasticity recalculation, then scroll to IndexChart.tsx.",
      script:
        "Here is our core innovation: Dynamic Yield Horizon Sensitivity.\n\nA legacy monthly survey only captures tickets booked on the day of the visit. But airfare is not a single price — it is an elasticity curve!\n\nWatch what happens when I toggle advance booking horizons: clicking 1-Day Urgent captures high-yield business travelers paying premium surge fares at index 157.8. Toggling to 45-Day Advance captures early leisure savers at 124.6.\n\nOur engine weights these 5 distinct booking horizons using official DGCA passenger volume distribution. In the historical comparison chart below, you can see how our Jevons index tracks DGCA benchmarks with a 0.984 correlation and zero upward bias.",
      evaluatorTakeaway: "Proves that manual surveys miss intraday surge curves that dynamic airline algorithms exploit.",
      interactiveAction: () => {
        scrollToComponent('lead-time-elasticity-card');
      },
      interactiveLabel: "Scroll to Yield Elasticity Curve",
    },
    {
      id: 4,
      time: "2:05 - 2:55",
      actTitle: "Act 4: High-Frequency Shocks, Fuel Sim & Network",
      componentTitle: "Daily CPI, ATF Simulator & Flight Map",
      targetElementId: "fuel-price-simulator",
      actionText: "Hover over Daily CPI tooltips, drag the ATF Fuel slider to +25%, then hover over the SVG flight network map routes.",
      script:
        "In our Daily High-Frequency CPI Chart, MoSPI officers can track day-to-day volatility — detecting festival price spikes around Diwali and Durga Puja 30 days before legacy CPI bulletins are even drafted.\n\nFurthermore, policy analysts can use our interactive ATF Jet Fuel Simulator. Jet Fuel constitutes 40% of airline operating costs. By sliding fuel prices up by 25%, our model calculates the exact inflationary pass-through into transport CPI.\n\nOur Interactive Flight Network Map covers India's top 12 high-density metro corridors, accounting for over 70% of domestic passenger volume — including Delhi-Mumbai, Bengaluru-Delhi, and Kolkata-Delhi — with expenditure weights mapped to DGCA seat statistics.",
      evaluatorTakeaway: "Interactive policy simulation tool + full coverage of 70%+ domestic air passenger traffic.",
      interactiveAction: () => {
        scrollToComponent('fuel-price-simulator');
      },
      interactiveLabel: "Scroll to ATF Fuel Simulator",
    },
    {
      id: 5,
      time: "2:55 - 3:45",
      actTitle: "Act 5: Sovereign Provenance & Open REST APIs",
      componentTitle: "SHA-256 Vault, REST API & eSankhyiki Export",
      actionText: "Click 'Provenance Vault' in header, show SHA-256 Merkle root. Open 'NSO & RBI API', run GET request (<10ms). Open 'Export', show eSankhyiki CSV.",
      script:
        "For a national economic indicator, data integrity is paramount.\n\nOpening our Sovereign Provenance Vault: every single web scraping batch is hashed into an immutable SHA-256 Merkle tree. Each quote's carrier, timestamp, route, and base fare is cryptographically signed. If any tariff is questioned in parliament or court, MoSPI has cryptographic mathematical proof that the data was not tampered with.\n\nNext, opening our NSO & RBI Open REST API Explorer: with sub-10 millisecond latency, our platform exposes standardized JSON and CSV endpoints. RBI monetary policy analysts and MoSPI data scientists can pipe our index directly into their macro-forecasting models with zero manual data entry.\n\nWith one click on Export, officers can download datasets formatted precisely for the official MoSPI eSankhyiki portal.",
      evaluatorTakeaway: "Tamper-proof legal validity (NDSAP compliant) + sub-10ms open machine-to-machine API feeds.",
      interactiveAction: () => {
        onClose();
        onOpenProvenance();
      },
      interactiveLabel: "Open Provenance Vault Modal",
    },
    {
      id: 6,
      time: "3:45 - 4:15",
      actTitle: "Act 6: Live Crawler, UN/ILO Math & Conclusion",
      componentTitle: "Scraper Monitor, UN/ILO Specs & Closing",
      actionText: "Switch to 'Live Extraction Monitor' tab, show Playwright logs. Switch to 'UN/ILO Methodology' tab. End with a confident closing.",
      script:
        "Under the Live Extraction Monitor, our distributed Playwright cluster harvests quotes from IndiGo, Air India, SpiceJet, and Akasa daily at 02:00 AM IST with stealth proxy rotation. When I trigger a live scrape, the system normalizes the fares, purges outliers, and updates all charts dynamically.\n\nUnder UN/ILO Methodology, our mathematics strictly follows Chapter 10 of the United Nations Consumer Price Index Manual.\n\nIn summary, VayuSuchak replaces multi-crore manual airport surveys with a zero-marginal-cost, real-time, mathematically bias-free, and cryptographically auditable index.\n\nOur solution is fully built, containerized, and ready for pilot deployment inside MoSPI's Data Informatics and Innovation Division today. Thank you!",
      evaluatorTakeaway: "Production-ready automated scraper + international compliance (UN/ILO Ch. 10) + ready for immediate MoSPI pilot.",
      interactiveAction: () => {
        setActiveTab('scraper');
        onClose();
      },
      interactiveLabel: "Switch to Scraper Monitor Tab",
    },
  ];

  const currentScene = scenes[activeSceneIndex];

  const handleCopyScript = (text: string, idx: number) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(idx);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="relative w-full max-w-4xl bg-slate-900 border border-slate-700/80 rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-800 bg-slate-950/70 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-xl bg-gradient-to-tr from-sky-600 to-indigo-600 text-white shadow-md shadow-sky-600/30">
              <Video className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-base font-bold text-white flex items-center gap-2">
                <span>SIH Video Demonstration Master Script</span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-300 border border-sky-500/30 font-mono">
                  4:00 Min Storyboard
                </span>
              </h2>
              <p className="text-xs text-slate-400">
                Word-for-word voiceover script, on-screen action cues, and component navigation for SIH26056 evaluation
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 transition-all"
            title="Close Guide"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Scene Selector Pills */}
        <div className="px-6 py-3 bg-slate-900/90 border-b border-slate-800 flex items-center gap-2 overflow-x-auto no-scrollbar">
          {scenes.map((sc, idx) => (
            <button
              key={sc.id}
              onClick={() => setActiveSceneIndex(idx)}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all flex items-center gap-1.5 ${
                activeSceneIndex === idx
                  ? 'bg-sky-600 text-white shadow-md shadow-sky-600/30 ring-1 ring-sky-400/50'
                  : 'bg-slate-800/80 text-slate-400 hover:text-slate-200 hover:bg-slate-800'
              }`}
            >
              <Clock className="w-3 h-3 text-sky-300" />
              <span>{sc.time}</span>
              <span className="text-[11px] opacity-75">({sc.componentTitle.split('&')[0].trim()})</span>
            </button>
          ))}
        </div>

        {/* Body Content */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {/* Active Scene Card */}
          <div className="bg-slate-950/60 border border-slate-800 rounded-xl p-5 space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
              <div>
                <span className="text-xs font-mono font-bold text-sky-400 uppercase tracking-wider">
                  {currentScene.actTitle}
                </span>
                <h3 className="text-lg font-bold text-white mt-0.5">
                  {currentScene.componentTitle}
                </h3>
              </div>
              <div className="flex items-center gap-2">
                <span className="px-2.5 py-1 text-xs font-mono font-semibold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 rounded-md">
                  ⏱️ {currentScene.time}
                </span>
                {currentScene.interactiveAction && (
                  <button
                    onClick={currentScene.interactiveAction}
                    className="flex items-center gap-1.5 px-3 py-1 text-xs font-semibold bg-sky-600/30 hover:bg-sky-600/50 text-sky-200 border border-sky-500/40 rounded-md transition-all shadow-sm"
                  >
                    <span>{currentScene.interactiveLabel || 'Navigate to Component'}</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </button>
                )}
              </div>
            </div>

            {/* Action Cue */}
            <div className="bg-amber-500/10 border border-amber-500/30 rounded-lg p-3 text-xs text-amber-200 flex items-start gap-2.5">
              <Play className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
              <div>
                <strong className="text-amber-300">On-Screen Action / Visuals: </strong>
                <span>{currentScene.actionText}</span>
              </div>
            </div>

            {/* Voiceover Script */}
            <div className="space-y-2">
              <div className="flex items-center justify-between text-xs text-slate-400">
                <span className="flex items-center gap-1.5 text-slate-300 font-semibold">
                  <Volume2 className="w-3.5 h-3.5 text-sky-400" />
                  <span>Verbatim Spoken Voiceover Script:</span>
                </span>
                <button
                  onClick={() => handleCopyScript(currentScene.script, currentScene.id)}
                  className="flex items-center gap-1 text-[11px] text-sky-400 hover:text-sky-300 transition-colors"
                >
                  {copiedIndex === currentScene.id ? (
                    <>
                      <CheckCircle2 className="w-3 h-3 text-emerald-400" />
                      <span className="text-emerald-400">Copied!</span>
                    </>
                  ) : (
                    <>
                      <Copy className="w-3 h-3" />
                      <span>Copy Text</span>
                    </>
                  )}
                </button>
              </div>
              <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 text-sm text-slate-200 leading-relaxed font-sans whitespace-pre-line shadow-inner">
                {currentScene.script}
              </div>
            </div>

            {/* Key Evaluator Takeaway */}
            <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-3 text-xs text-emerald-300 flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-emerald-400 shrink-0" />
              <div>
                <strong className="text-emerald-200">Key SIH Jury Takeaway: </strong>
                <span>{currentScene.evaluatorTakeaway}</span>
              </div>
            </div>
          </div>
        </div>

        {/* Footer Navigation */}
        <div className="px-6 py-3.5 border-t border-slate-800 bg-slate-950/80 flex items-center justify-between">
          <div className="text-xs text-slate-400">
            Scene <strong>{activeSceneIndex + 1}</strong> of <strong>{scenes.length}</strong>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={() => setActiveSceneIndex(prev => Math.max(0, prev - 1))}
              disabled={activeSceneIndex === 0}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                activeSceneIndex === 0
                  ? 'bg-slate-800/40 text-slate-600 cursor-not-allowed'
                  : 'bg-slate-800 text-slate-200 hover:bg-slate-700'
              }`}
            >
              Previous Scene
            </button>
            <button
              onClick={() => setActiveSceneIndex(prev => Math.min(scenes.length - 1, prev + 1))}
              disabled={activeSceneIndex === scenes.length - 1}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                activeSceneIndex === scenes.length - 1
                  ? 'bg-slate-800/40 text-slate-600 cursor-not-allowed'
                  : 'bg-sky-600 text-white hover:bg-sky-500 shadow-md shadow-sky-600/30'
              }`}
            >
              Next Scene ➔
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
