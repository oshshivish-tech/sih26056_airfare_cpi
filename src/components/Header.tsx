import React from 'react';
import { Activity, Plane, Download, RefreshCw, Layers, ShieldCheck, BarChart3, Database } from 'lucide-react';

interface HeaderProps {
  activeTab: 'overview' | 'corridors' | 'scraper' | 'methodology';
  setActiveTab: (tab: 'overview' | 'corridors' | 'scraper' | 'methodology') => void;
  onRunScrape: () => void;
  onOpenExport: () => void;
  isScraping: boolean;
  latestIndex: number;
  yoyInflation: number;
}

export const Header: React.FC<HeaderProps> = ({
  activeTab,
  setActiveTab,
  onRunScrape,
  onOpenExport,
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
            LIVE MOSPI AIRFARE CPI: <strong className="ml-1 text-white">{latestIndex.toFixed(1)}</strong> (Base=100)
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
          <span>DGCA Corridor Weights: <strong className="text-sky-300">50 Top Indian Corridors Monitored</strong></span>
        </div>
      </div>

      {/* Main Header Container */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Brand Logo & Title */}
          <div className="flex items-center space-x-3">
            <div className="p-2.5 rounded-xl bg-gradient-to-tr from-teal-600 to-sky-600 text-white shadow-lg shadow-teal-500/20 ring-1 ring-white/20">
              <Plane className="w-6 h-6 transform -rotate-12" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h1 className="text-lg font-bold tracking-tight text-white flex items-center">
                  AirIntel India
                </h1>
                <span className="px-2 py-0.5 text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30 rounded-full font-mono">
                  Team Rookie
                </span>
                <span className="px-2 py-0.5 text-[10px] font-semibold bg-sky-500/20 text-sky-300 border border-sky-500/30 rounded-full font-mono">
                  SIH 26056
                </span>
              </div>
              <p className="text-xs text-slate-400">
                MoSPI Airfare Intelligence & CPI Command Center • National Statistical Office
              </p>
            </div>
          </div>

          {/* Navigation Tabs */}
          <nav className="hidden md:flex items-center space-x-1 bg-slate-900/80 p-1 rounded-xl border border-slate-800">
            <button
              onClick={() => setActiveTab('overview')}
              className={`flex items-center space-x-2 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
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
              className={`flex items-center space-x-2 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
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
              className={`flex items-center space-x-2 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
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
              className={`flex items-center space-x-2 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
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
          <div className="flex items-center space-x-3">
            <button
              onClick={onRunScrape}
              disabled={isScraping}
              className={`flex items-center space-x-2 px-3.5 py-1.5 rounded-lg text-xs font-semibold text-white transition-all shadow-md ${
                isScraping
                  ? 'bg-slate-700 cursor-not-allowed opacity-75'
                  : 'bg-emerald-600 hover:bg-emerald-500 shadow-emerald-600/20 active:scale-95'
              }`}
            >
              <RefreshCw className={`w-3.5 h-3.5 ${isScraping ? 'animate-spin' : ''}`} />
              <span>{isScraping ? 'Scraping Live...' : 'Trigger Live Scrape'}</span>
            </button>

            <button
              onClick={onOpenExport}
              className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium text-slate-200 bg-slate-800/80 hover:bg-slate-700 border border-slate-700 transition-all hover:border-slate-600"
            >
              <Download className="w-3.5 h-3.5 text-sky-400" />
              <span>Export Report</span>
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};
