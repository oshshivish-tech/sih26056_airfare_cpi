import React from 'react';
import { TrendingUp, ShieldCheck, Database, Filter, ArrowUpRight, CheckCircle2 } from 'lucide-react';
import { CPIIndexPoint, DailyFarePoint } from '../types';

interface CPIMetricsOverviewProps {
  currentPoint: CPIIndexPoint;
  latestDailyPoint?: DailyFarePoint;
  totalDataPoints: number;
  outlierCount: number;
  onOpenOutlierModal: () => void;
}

export const CPIMetricsOverview: React.FC<CPIMetricsOverviewProps> = ({
  currentPoint,
  latestDailyPoint,
  totalDataPoints,
  outlierCount,
  onOpenOutlierModal
}) => {
  // Dynamically derive current month and YoY comparison period (1 year prior)
  const parsePeriodInfo = () => {
    if (currentPoint.date && currentPoint.date.includes('-')) {
      const [yearStr, monthStr] = currentPoint.date.split('-');
      const year = parseInt(yearStr, 10);
      const monthIdx = parseInt(monthStr, 10) - 1;
      const d = new Date(year, monthIdx, 1);
      const mShort = d.toLocaleString('en-US', { month: 'short' });
      return {
        monthUpper: mShort.toUpperCase(),
        comparisonLabel: `vs ${mShort} ${year - 1}`
      };
    }
    const parts = (currentPoint.periodLabel || '').trim().split(' ');
    const mShort = parts[0] || 'Oct';
    const year = parseInt(parts[1], 10) || 2026;
    return {
      monthUpper: mShort.toUpperCase(),
      comparisonLabel: `vs ${mShort} ${year - 1}`
    };
  };

  const { monthUpper, comparisonLabel } = parsePeriodInfo();

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
      {/* Metric 1: Current CPI Airfare Index */}
      <div className="glass-panel p-5 rounded-2xl relative overflow-hidden group hover:border-sky-500/40 transition-all">
        <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
          <TrendingUp className="w-16 h-16 text-sky-400" />
        </div>
        <div className="flex items-center space-x-2 text-xs font-semibold text-sky-400 mb-1">
          <span className="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
          <span>AIRFARE CPI ({monthUpper} MTD)</span>
        </div>
        <div className="flex items-baseline space-x-2 my-1">
          <span className="text-3xl font-extrabold tracking-tight text-white font-mono">
            {currentPoint.jevonsIndex.toFixed(1)}
          </span>
          <span className="text-xs text-slate-400 font-medium">(Base = 100)</span>
        </div>
        <div className="flex items-center justify-between text-xs mt-3 text-slate-300 font-medium border-t border-slate-800/80 pt-2">
          <span className="flex items-center text-emerald-400">
            <ArrowUpRight className="w-3.5 h-3.5 mr-0.5" />
            +{currentPoint.momInflationRate}% MoM
          </span>
          {latestDailyPoint && (
            <span className="text-[11px] font-mono bg-sky-950/80 text-sky-300 border border-sky-800/50 px-2 py-0.5 rounded-full flex items-center gap-1">
              <span className="w-1.5 h-1.5 rounded-full bg-sky-400 animate-pulse"></span>
              Today ({latestDailyPoint.dayLabel.split('(')[0].trim()}): <strong className="text-white">{latestDailyPoint.dailyJevonsIndex.toFixed(1)}</strong>
            </span>
          )}
        </div>
      </div>

      {/* Metric 2: YoY Inflation Rate */}
      <div className="glass-panel p-5 rounded-2xl relative overflow-hidden group hover:border-sky-500/40 transition-all">
        <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
          <TrendingUp className="w-16 h-16 text-amber-400" />
        </div>
        <div className="flex items-center space-x-2 text-xs font-semibold text-amber-400 mb-1">
          <span className="w-2 h-2 rounded-full bg-amber-400"></span>
          <span>ANNUAL INFLATION (YoY)</span>
        </div>
        <div className="flex items-baseline space-x-2 my-1">
          <span className="text-3xl font-extrabold tracking-tight text-white font-mono">
            +{currentPoint.yoyInflationRate}%
          </span>
          <span className="text-xs text-slate-400 font-medium">{comparisonLabel}</span>
        </div>
        <div className="text-xs text-slate-400 mt-3 flex items-center justify-between">
          <span>eSankhyiki Release Lag: <strong className="text-slate-200">~30 Days</strong></span>
          <span className="text-emerald-400 font-medium">Our Pipeline: Real-Time</span>
        </div>
      </div>

      {/* Metric 3: Scraped Data Volume */}
      <div className="glass-panel p-5 rounded-2xl relative overflow-hidden group hover:border-sky-500/40 transition-all">
        <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
          <Database className="w-16 h-16 text-indigo-400" />
        </div>
        <div className="flex items-center space-x-2 text-xs font-semibold text-indigo-400 mb-1">
          <span className="w-2 h-2 rounded-full bg-indigo-400"></span>
          <span>INGESTED AIRFARE QUOTES</span>
        </div>
        <div className="flex items-baseline space-x-2 my-1">
          <span className="text-3xl font-extrabold tracking-tight text-white font-mono">
            {totalDataPoints.toLocaleString()}
          </span>
          <span className="text-xs text-slate-400 font-medium">Verified Quotes</span>
        </div>
        <div className="text-xs text-slate-400 mt-3 flex items-center justify-between">
          <span>Target Sources: <strong className="text-slate-200">5 Portals</strong></span>
          <span className="text-sky-400 font-medium">12 Corridors</span>
        </div>
      </div>

      {/* Metric 4: Outlier Pruning & Integrity */}
      <div className="glass-panel p-5 rounded-2xl relative overflow-hidden group hover:border-sky-500/40 transition-all">
        <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
          <Filter className="w-16 h-16 text-emerald-400" />
        </div>
        <div className="flex items-center space-x-2 text-xs font-semibold text-emerald-400 mb-1">
          <ShieldCheck className="w-3.5 h-3.5" />
          <span>OUTLIER PRUNING ENGINE</span>
        </div>
        <div className="flex items-baseline space-x-2 my-1">
          <span className="text-3xl font-extrabold tracking-tight text-white font-mono">
            {outlierCount}
          </span>
          <span className="text-xs text-slate-400 font-medium">Anomalies Filtered</span>
        </div>
        <div className="text-xs mt-3 flex items-center justify-between">
          <button
            onClick={onOpenOutlierModal}
            className="text-sky-400 hover:text-sky-300 font-medium underline flex items-center space-x-1"
          >
            <span>View Outlier Logs</span>
            <ArrowUpRight className="w-3 h-3" />
          </button>
          <span className="text-emerald-400 font-medium flex items-center">
            <CheckCircle2 className="w-3 h-3 mr-1" />
            99.8% Integrity
          </span>
        </div>
      </div>
    </div>
  );
};
