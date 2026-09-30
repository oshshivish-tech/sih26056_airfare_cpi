import React from 'react';
import { Activity, CheckCircle2, AlertTriangle, ShieldCheck, Clock, RefreshCw } from 'lucide-react';
import { TARGET_AIRLINES, DATA_METADATA } from '../config/constants';

interface DataHealthPanelProps {
  onOpenScraperTab?: () => void;
  onRunScrape?: () => void;
  isScraping?: boolean;
}

export const DataHealthPanel: React.FC<DataHealthPanelProps> = ({
  onOpenScraperTab,
  onRunScrape,
  isScraping = false
}) => {
  const airlineHealth = [
    { name: 'IndiGo (6E)', portal: 'goindigo.in', successRate: '99.6%', latency: '340ms', status: 'Optimal' },
    { name: 'Air India (AI)', portal: 'airindia.com', successRate: '98.9%', latency: '410ms', status: 'Optimal' },
    { name: 'SpiceJet (SG)', portal: 'spicejet.com', successRate: '94.2%', latency: '890ms', status: 'Monitored' },
    { name: 'Akasa Air (QP)', portal: 'akasaair.com', successRate: '99.1%', latency: '280ms', status: 'Optimal' }
  ];

  return (
    <div className="glass-panel p-5 rounded-2xl border border-slate-800 bg-slate-900/60 mb-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 mb-4 border-b border-slate-800/80">
        <div className="flex items-center space-x-2.5">
          <div className="p-2 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
            <Activity className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold text-white tracking-tight flex items-center gap-2">
              <span>Collection Engine Health & Feed Quality Monitor</span>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30">
                {DATA_METADATA.dataStatusBadge}
              </span>
            </h3>
            <p className="text-[11px] text-slate-400">
              Rate-limited compliant collection status across 4 target airlines & 12 representative corridors
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {onRunScrape && (
            <button
              onClick={onRunScrape}
              disabled={isScraping}
              className="px-2.5 py-1 text-xs font-semibold rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-200 border border-emerald-500/40 flex items-center gap-1.5 transition-all"
            >
              <RefreshCw className={`w-3 h-3 ${isScraping ? 'animate-spin' : ''}`} />
              <span>{isScraping ? 'Testing Feeds...' : 'Test Feeds'}</span>
            </button>
          )}
          {onOpenScraperTab && (
            <button
              onClick={onOpenScraperTab}
              className="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-all"
            >
              Full Monitor ↗
            </button>
          )}
        </div>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-4">
        <div className="p-3 bg-slate-950/70 rounded-xl border border-slate-800/70">
          <div className="text-[10px] text-slate-400 uppercase font-semibold">Daily Collection Volume</div>
          <div className="text-lg font-bold text-white font-mono mt-0.5">2,400</div>
          <div className="text-[10px] text-slate-500">quotes/day [Sample calibration]</div>
        </div>

        <div className="p-3 bg-slate-950/70 rounded-xl border border-slate-800/70">
          <div className="text-[10px] text-slate-400 uppercase font-semibold">Average Ingestion Success</div>
          <div className="text-lg font-bold text-emerald-400 font-mono mt-0.5">98.4%</div>
          <div className="text-[10px] text-emerald-500/80">Across all scheduled batches</div>
        </div>

        <div className="p-3 bg-slate-950/70 rounded-xl border border-slate-800/70">
          <div className="text-[10px] text-slate-400 uppercase font-semibold">Last Scheduled Batch</div>
          <div className="text-sm font-bold text-slate-200 font-mono mt-1 flex items-center gap-1">
            <Clock className="w-3 h-3 text-sky-400" />
            <span>03:30 AM IST</span>
          </div>
          <div className="text-[10px] text-slate-500">Off-peak night execution</div>
        </div>

        <div className="p-3 bg-slate-950/70 rounded-xl border border-slate-800/70">
          <div className="text-[10px] text-slate-400 uppercase font-semibold">IQR Outlier Rejections</div>
          <div className="text-lg font-bold text-amber-400 font-mono mt-0.5">48 Quotes</div>
          <div className="text-[10px] text-amber-500/80">Filtered & quarantined</div>
        </div>
      </div>

      {/* Airline Status Strip */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2 pt-2 border-t border-slate-800/60">
        {airlineHealth.map(air => (
          <div key={air.name} className="flex items-center justify-between p-2 rounded-lg bg-slate-950/40 text-xs">
            <div>
              <span className="font-semibold text-slate-200">{air.name}</span>
              <span className="block text-[10px] text-slate-500 font-mono">{air.portal}</span>
            </div>
            <div className="text-right">
              <span className="text-emerald-400 font-mono font-bold text-[11px]">{air.successRate}</span>
              <span className="block text-[10px] text-slate-400 font-mono">{air.latency}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
