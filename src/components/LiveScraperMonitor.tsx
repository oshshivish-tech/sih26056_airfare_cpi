import React from 'react';
import { ScraperSourceStatus } from '../types';
import { ScrapingLogEntry } from '../services/scraperEngine';
import { Terminal, Shield, RefreshCw, CheckCircle2, AlertTriangle, Cpu, Globe } from 'lucide-react';

interface LiveScraperMonitorProps {
  sources: ScraperSourceStatus[];
  logs: ScrapingLogEntry[];
  isScraping: boolean;
  onRunScrape: () => void;
}

export const LiveScraperMonitor: React.FC<LiveScraperMonitorProps> = ({
  sources,
  logs,
  isScraping,
  onRunScrape
}) => {
  return (
    <div className="space-y-6 mb-6">
      {/* Top Banner & Control */}
      <div className="glass-panel p-6 rounded-2xl flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-lg font-bold text-white tracking-tight flex items-center">
            <Globe className="w-5 h-5 text-sky-400 mr-2" />
            Automated Web Scraping Extraction Health & Resilience
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Multi-portal headless Playwright cluster & direct API XHR payload interceptors
          </p>
        </div>

        <button
          onClick={onRunScrape}
          disabled={isScraping}
          className={`flex items-center space-x-2 px-4 py-2 rounded-xl text-xs font-bold text-white transition-all shadow-lg ${
            isScraping
              ? 'bg-slate-700 cursor-not-allowed opacity-75'
              : 'bg-gradient-to-r from-sky-600 to-indigo-600 hover:from-sky-500 hover:to-indigo-500 shadow-sky-600/30 active:scale-95'
          }`}
        >
          <RefreshCw className={`w-4 h-4 ${isScraping ? 'animate-spin' : ''}`} />
          <span>{isScraping ? 'Extraction Engine Active...' : 'Run Extraction Job Now'}</span>
        </button>
      </div>

      {/* Target Sources Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {sources.map(src => (
          <div key={src.id} className="glass-panel p-5 rounded-xl border border-slate-800 hover:border-sky-500/40 transition-all">
            <div className="flex items-center justify-between mb-3">
              <span className="font-bold text-sm text-white">{src.displayName}</span>
              <span className={`text-[10px] font-bold px-2.5 py-0.5 rounded-full border ${
                src.status === 'ONLINE'
                  ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30'
                  : 'bg-amber-500/10 text-amber-400 border-amber-500/30'
              }`}>
                {src.status}
              </span>
            </div>

            <div className="space-y-2 text-xs text-slate-300">
              <div className="flex justify-between">
                <span className="text-slate-400">Strategy:</span>
                <span className="font-mono text-sky-300 font-semibold">{src.bypassStrategy}</span>
              </div>

              <div className="flex justify-between">
                <span className="text-slate-400">Response Latency:</span>
                <span className="font-mono text-slate-200">{src.latencyMs} ms</span>
              </div>

              <div className="flex justify-between">
                <span className="text-slate-400">Extraction Success Rate:</span>
                <span className="font-mono text-emerald-400 font-bold">{src.successRate}%</span>
              </div>

              <div className="flex justify-between">
                <span className="text-slate-400">24h Extracted Quotes:</span>
                <span className="font-mono text-slate-200 font-bold">{src.recordsExtracted24h.toLocaleString()}</span>
              </div>

              <div className="flex justify-between pt-2 border-t border-slate-800">
                <span className="text-slate-400">Active Proxy Pool:</span>
                <span className="font-mono text-sky-400">{src.activeProxies} IPs</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Real-time Streaming Terminal Console */}
      <div className="glass-panel rounded-2xl overflow-hidden border border-slate-800">
        <div className="bg-slate-900/90 px-4 py-3 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Terminal className="w-4 h-4 text-emerald-400" />
            <span className="text-xs font-mono font-bold text-slate-200">
              LIVE EXTRACTION TERMINAL LOG STREAM
            </span>
          </div>
          <span className="text-[10px] font-mono text-slate-400">
            Auto-scroll Active
          </span>
        </div>

        <div className="p-4 bg-slate-950/90 font-mono text-xs text-slate-300 h-64 overflow-y-auto space-y-2">
          {logs.length === 0 ? (
            <div className="text-slate-500 italic py-8 text-center">
              Click "Run Extraction Job Now" to trigger live scraping and inspect real-time logs...
            </div>
          ) : (
            logs.map((log) => (
              <div key={log.id} className="flex items-start space-x-3 leading-relaxed">
                <span className="text-slate-500 shrink-0">[{log.timestamp}]</span>
                <span className={`shrink-0 px-1.5 py-0.5 rounded text-[10px] font-bold ${
                  log.level === 'SUCCESS' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' :
                  log.level === 'WARN' ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30' :
                  log.level === 'ERROR' ? 'bg-rose-500/20 text-rose-400 border border-rose-500/30' :
                  'bg-sky-500/20 text-sky-400 border border-sky-500/30'
                }`}>
                  {log.source}
                </span>
                <span className={log.level === 'SUCCESS' ? 'text-slate-100' : 'text-slate-300'}>
                  {log.message}
                </span>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};
