import React from 'react';
import { Activity, Plane, Download, RefreshCw, Layers, ShieldCheck, BarChart3, Database, Lock, Presentation, Key, Server } from 'lucide-react';

interface HeaderProps {
  activeTab: 'overview' | 'corridors' | 'scraper' | 'methodology';
  setActiveTab: (tab: 'overview' | 'corridors' | 'scraper' | 'methodology') => void;
  onRunScrape: () => void;
  onOpenExport: () => void;
  onOpenProvenance: () => void;
  onOpenLiveAPI: () => void;
  onOpenRestApi: () => void;
  isLiveAPIConnected: boolean;
  isScraping: boolean;
  latestIndex: number;
  yoyInflation: number;
}

export const Header: React.FC<HeaderProps> = ({
  activeTab,
  setActiveTab,
  onRunScrape,
  onOpenExport,
  onOpenProvenance,
  onOpenLiveAPI,
  onOpenRestApi,
  isLiveAPIConnected,
  isScraping,
  latestIndex,
  yoyInflation,
}) => {
  return (
    <header className="sticky top-0 z-40 border-b border-slate-800 bg-slate-950/90 backdrop-blur-md">
      {/* Top Ticker Ribbon */}
      <div className="bg-slate-900/90 border-b border-slate-800/60 py-1.5 px-4 overflow-hidden text-xs">
        <div className="flex items-center space-x-6 animate-ticker whitespace-nowrap text-slate-300">
          <span className="flex items-center text-sky-400 font-medium">
            <span className="relative flex h-2 w-2 mr-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-sky-500"></span>
            </span>
            LIVE MOSPI AIRFARE CPI: <strong className="ml-1 text-white">{latestIndex.toFixed(1)}</strong> (Sep MTD Composite)
          </span>
          <span className="text-slate-400">|</span>
          <span className="text-slate-300">
            YoY Inflation: <strong className={yoyInflation >= 0 ? "text-emerald-400 ml-1" : "text-rose-400 ml-1"}>+{yoyInflation}%</strong>
          </span>
          <span className="text-slate-400">|</span>
          <span>Top Corridor: <strong className="text-slate-100">DEL ↔ BOM (₹5,420, +2.4%)</strong></span>
          <span className="text-slate-400">|</span>
          <span>Methodology: <strong className="text-amber-400 font-mono">UN/ILO Jevons Geometric Index</strong></span>
          <span className="text-slate-400">|</span>
          <span>Target Coverage: <strong className="text-emerald-400">IndiGo, Air India, Akasa, MMT, EaseMyTrip</strong></span>
          <span className="text-slate-400">|</span>
          <span>DGCA Corridor Weights: <strong className="text-sky-300">12 Benchmark Corridors Monitored</strong></span>
          <span className="text-slate-400">|</span>
          <span>Official Benchmark: <a href="https://esankhyiki.mospi.gov.in/" target="_blank" rel="noopener noreferrer" className="text-purple-300 hover:text-purple-200 underline font-mono">MoSPI eSankhyiki Portal</a></span>
        </div>
      </div>

      {/* Main Header Container */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-wrap items-center justify-between py-2.5 gap-3 min-h-[4rem]">
          {/* Brand Logo & Title */}
          <div className="flex items-center space-x-3 shrink-0">
            <div className="p-2 sm:p-2.5 rounded-xl bg-gradient-to-tr from-teal-600 to-sky-600 text-white shadow-lg shadow-teal-500/20 ring-1 ring-white/20">
              <Plane className="w-5 h-5 sm:w-6 sm:h-6 transform -rotate-12" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h1 className="text-base sm:text-lg font-bold tracking-tight text-white flex items-center gap-1.5">
                  <span className="text-sky-400 font-mono font-black">APIx</span>
                  <span>•</span>
                  <span>VayuSuchak</span>
                  <span className="text-xs font-normal text-slate-400 font-sans hidden sm:inline">(वायु सूचक)</span>
                </h1>
                <span className="px-2 py-0.5 text-[10px] font-semibold bg-purple-500/20 text-purple-300 border border-purple-500/30 rounded-full font-mono">
                  SIH 26056
                </span>
                <span className="hidden sm:inline-flex items-center px-2 py-0.5 text-[10px] font-semibold bg-sky-500/20 text-sky-300 border border-sky-500/30 rounded-full font-mono">
                  Team Roorkies (168405)
                </span>
              </div>
              <p className="text-[11px] text-slate-400">
                Real-Time Airfare Price Index (APIx) for India • MoSPI NSO & RBI Monetary Policy Augmentation
              </p>
            </div>
          </div>

          {/* Navigation Tabs (Desktop) */}
          <nav className="hidden lg:flex items-center space-x-1 bg-slate-900/80 p-1 rounded-xl border border-slate-800 shrink-0">
            <button
              onClick={() => setActiveTab('overview')}
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                activeTab === 'overview'
                  ? 'bg-sky-600 text-white shadow-md shadow-sky-600/30'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
              }`}
            >
              <BarChart3 className="w-3.5 h-3.5" />
              <span>CPI Analytics</span>
            </button>

            <button
              onClick={() => setActiveTab('corridors')}
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                activeTab === 'corridors'
                  ? 'bg-sky-600 text-white shadow-md shadow-sky-600/30'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span>Flight Corridors</span>
            </button>

            <button
              onClick={() => setActiveTab('scraper')}
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                activeTab === 'scraper'
                  ? 'bg-sky-600 text-white shadow-md shadow-sky-600/30'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
              }`}
            >
              <Database className="w-3.5 h-3.5" />
              <span>Live Extraction Monitor</span>
            </button>

            <button
              onClick={() => setActiveTab('methodology')}
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                activeTab === 'methodology'
                  ? 'bg-sky-600 text-white shadow-md shadow-sky-600/30'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
              }`}
            >
              <ShieldCheck className="w-3.5 h-3.5" />
              <span>UN/ILO Methodology</span>
            </button>
          </nav>

          {/* Action Buttons */}
          <div className="flex items-center flex-wrap gap-2 shrink-0">
            <a
              href="/slides.html"
              target="_blank"
              rel="noreferrer"
              className="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold text-blue-300 bg-blue-500/10 hover:bg-blue-500/20 border border-blue-500/30 transition-all shadow-sm"
              title="Open Official Pitch Deck"
            >
              <Presentation className="w-3.5 h-3.5 text-blue-400" />
              <span>Pitch Deck</span>
            </a>

            <a
              href="/AirIntel_India_SIH26056_Presentation.pptx"
              download="AirIntel_India_SIH26056_Presentation.pptx"
              className="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold text-amber-300 bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 transition-all shadow-sm"
              title="Download Official PowerPoint Presentation (.pptx)"
            >
              <Download className="w-3.5 h-3.5 text-amber-400" />
              <span>Download PPT</span>
            </a>

            <button
              onClick={onOpenRestApi}
              className="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold text-purple-300 bg-purple-500/10 hover:bg-purple-500/20 border border-purple-500/30 transition-all shadow-sm"
              title="Inspect MoSPI NSO & RBI Open REST API Endpoints"
            >
              <Server className="w-3.5 h-3.5 text-purple-400" />
              <span>NSO & RBI API</span>
            </button>

            <button
              onClick={onOpenProvenance}
              className="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold text-teal-300 bg-teal-500/10 hover:bg-teal-500/20 border border-teal-500/30 transition-all"
              title="View SHA-256 Cryptographic Audit Trail"
            >
              <Lock className="w-3.5 h-3.5 text-teal-400" />
              <span className="hidden sm:inline">Provenance Vault</span>
            </button>

            <button
              onClick={onOpenLiveAPI}
              className={`flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold border transition-all ${
                isLiveAPIConnected
                  ? 'bg-emerald-500/15 text-emerald-300 border-emerald-500/40 shadow-sm shadow-emerald-500/20'
                  : 'bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-300 border-indigo-500/30'
              }`}
              title="Connect Amadeus Live GDS API for Real Live Flight Fares"
            >
              <Key className="w-3.5 h-3.5 text-indigo-400" />
              <span className="hidden sm:inline">{isLiveAPIConnected ? 'Live GDS Active' : 'Live Flight API'}</span>
            </button>

            <button
              onClick={onRunScrape}
              disabled={isScraping}
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold text-white transition-all shadow-md ${
                isScraping
                  ? 'bg-slate-700 cursor-not-allowed opacity-75'
                  : 'bg-emerald-600 hover:bg-emerald-500 shadow-emerald-600/20 active:scale-95'
              }`}
            >
              <RefreshCw className={`w-3.5 h-3.5 ${isScraping ? 'animate-spin' : ''}`} />
              <span>{isScraping ? 'Scraping...' : 'Trigger Live Scrape'}</span>
            </button>

            <button
              onClick={onOpenExport}
              className="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-medium text-slate-200 bg-slate-800/80 hover:bg-slate-700 border border-slate-700 transition-all hover:border-slate-600"
            >
              <Download className="w-3.5 h-3.5 text-sky-400" />
              <span className="hidden sm:inline">Export</span>
            </button>
          </div>
        </div>

        {/* Mobile Navigation Strip */}
        <div className="lg:hidden flex items-center justify-between overflow-x-auto py-2 border-t border-slate-800/80 gap-1">
          <button
            onClick={() => setActiveTab('overview')}
            className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
              activeTab === 'overview'
                ? 'bg-sky-600 text-white'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <BarChart3 className="w-3 h-3" />
            <span>CPI Analytics</span>
          </button>
          <button
            onClick={() => setActiveTab('corridors')}
            className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
              activeTab === 'corridors'
                ? 'bg-sky-600 text-white'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Layers className="w-3 h-3" />
            <span>Flight Corridors</span>
          </button>
          <button
            onClick={() => setActiveTab('scraper')}
            className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
              activeTab === 'scraper'
                ? 'bg-sky-600 text-white'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Database className="w-3 h-3" />
            <span>Live Monitor</span>
          </button>
          <button
            onClick={() => setActiveTab('methodology')}
            className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
              activeTab === 'methodology'
                ? 'bg-sky-600 text-white'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <ShieldCheck className="w-3 h-3" />
            <span>Methodology</span>
          </button>
        </div>
      </div>
    </header>
  );
};
