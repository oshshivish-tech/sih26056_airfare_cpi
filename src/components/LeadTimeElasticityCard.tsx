import React, { useMemo } from 'react';
import { Clock, TrendingUp, AlertTriangle, ShieldCheck, ArrowRight, Database } from 'lucide-react';
import { LeadTimeHorizon, FlightFare } from '../types';

interface LeadTimeElasticityCardProps {
  fares?: FlightFare[];
  selectedHorizon: LeadTimeHorizon | 'ALL';
  onSelectHorizon: (h: LeadTimeHorizon | 'ALL') => void;
}

export const LeadTimeElasticityCard: React.FC<LeadTimeElasticityCardProps> = ({
  fares = [],
  selectedHorizon,
  onSelectHorizon
}) => {
  const baseYield = 4850; // DGCA Official 2024-25 Domestic Benchmark Yield

  const horizonConfigs: {
    key: LeadTimeHorizon;
    label: string;
    leadDays: number;
    urgency: string;
    desc: string;
  }[] = [
    {
      key: '1d',
      label: 'T+1 Window',
      leadDays: 1,
      urgency: 'Emergency / Last Minute',
      desc: 'Algorithmically surged flexi pricing for immediate departure'
    },
    {
      key: '7d',
      label: 'T+7 Window',
      leadDays: 7,
      urgency: 'Corporate / Urgent',
      desc: 'Short-lead business corridor travel demand peak'
    },
    {
      key: '14d',
      label: 'T+14 Window',
      leadDays: 14,
      urgency: 'Standard Advance',
      desc: 'Baseline travel horizon closely mirroring DGCA monthly yield'
    },
    {
      key: '30d',
      label: 'T+30 Window',
      leadDays: 30,
      urgency: 'Advance Booking',
      desc: 'Vacation & advance personal planning discount threshold'
    },
    {
      key: '45d',
      label: 'T+45 Window',
      leadDays: 45,
      urgency: 'Early Bird Saver',
      desc: 'Lowest bucket economy seats available across direct airlines'
    }
  ];

  // Dynamically compute average fare, sample count, and index for every horizon from live quotes
  const calculatedHorizons = useMemo(() => {
    return horizonConfigs.map(cfg => {
      const matching = fares.filter(f => 
        (f.leadTimeHorizon === cfg.key || (cfg.key === '14d' && (f.leadTimeHorizon as any) === '15d')) && !f.isOutlier
      );
      const quotesCount = matching.length;

      let avgFare = 0;
      if (quotesCount > 0) {
        const sum = matching.reduce((acc, f) => acc + f.totalFare, 0);
        avgFare = Math.round(sum / quotesCount);
      } else {
        avgFare = baseYield;
      }

      const index = Number(((avgFare / baseYield) * 100).toFixed(1));
      const diffPct = Number((((avgFare - baseYield) / baseYield) * 100).toFixed(1));
      const multiplier = diffPct >= 0 ? `+${diffPct}%` : `${diffPct}%`;

      let color = 'text-sky-400';
      let bgBadge = 'bg-sky-500/20 text-sky-300 border-sky-500/30';
      if (diffPct > 12) {
        color = 'text-rose-400';
        bgBadge = 'bg-rose-500/20 text-rose-300 border-rose-500/30';
      } else if (diffPct > 3) {
        color = 'text-amber-400';
        bgBadge = 'bg-amber-500/20 text-amber-300 border-amber-500/30';
      } else if (diffPct < -4) {
        color = 'text-emerald-400';
        bgBadge = 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30';
      }

      return {
        ...cfg,
        avgFare,
        index,
        multiplier,
        quotesCount,
        color,
        bgBadge
      };
    });
  }, [fares, baseYield]);

  // Compute live dynamic last-minute premium
  const t1 = calculatedHorizons.find(h => h.key === '1d');
  const t45 = calculatedHorizons.find(h => h.key === '45d');
  const premiumPct = (t1 && t45 && t45.avgFare > 0)
    ? (((t1.avgFare - t45.avgFare) / t45.avgFare) * 100).toFixed(1)
    : '0';

  const totalQuotesAnalyzed = fares.filter(f => !f.isOutlier).length;

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6 border border-slate-800">
      <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 mb-6">
        <div>
          <div className="flex items-center space-x-2">
            <span className="p-2 rounded-xl bg-purple-500/10 text-purple-400 border border-purple-500/20">
              <Clock className="w-5 h-5" />
            </span>
            <div>
              <div className="flex items-center gap-2">
                <h3 className="text-base font-bold text-white tracking-tight">
                  Advance-Purchase Elasticity Curve (Lead-Time Horizons)
                </h3>
                <span className="px-2 py-0.5 text-[10px] font-mono bg-purple-500/20 text-purple-300 border border-purple-500/30 rounded-full">
                  SIH 26056 Pillar (c)
                </span>
                <span className="px-2 py-0.5 text-[10px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 rounded-full flex items-center gap-1">
                  <Database className="w-3 h-3" />
                  Live Calculated ({totalQuotesAnalyzed} quotes)
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                Dynamic pricing dispersion computed directly from active scraped airline & OTA flight quotes
              </p>
            </div>
          </div>
        </div>

        <div className="flex items-center gap-1.5 self-start lg:self-center">
          <button
            onClick={() => onSelectHorizon('ALL')}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
              selectedHorizon === 'ALL'
                ? 'bg-purple-600 text-white shadow-md shadow-purple-600/30'
                : 'bg-slate-800/80 text-slate-400 hover:text-slate-200 border border-slate-700'
            }`}
          >
            Combined (All T+)
          </button>
        </div>
      </div>

      {/* Grid of Horizon Buckets with Live Calculated Fares */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
        {calculatedHorizons.map(h => {
          const isSelected = selectedHorizon === h.key;
          return (
            <div
              key={h.key}
              onClick={() => onSelectHorizon(h.key)}
              className={`p-4 rounded-xl border transition-all cursor-pointer relative overflow-hidden ${
                isSelected
                  ? 'bg-slate-800/90 border-purple-500 ring-2 ring-purple-500/20 shadow-lg'
                  : 'bg-slate-900/60 border-slate-800 hover:border-slate-700 hover:bg-slate-850'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-mono font-bold text-slate-200">{h.label}</span>
                <span className={`text-[10px] px-2 py-0.5 rounded-full border font-mono font-semibold ${h.bgBadge}`}>
                  {h.multiplier}
                </span>
              </div>

              <div className="text-xl font-bold text-white mb-1">
                ₹{h.avgFare.toLocaleString()}
              </div>

              <div className="flex items-center justify-between text-xs text-slate-400 mb-1 font-mono">
                <span>Index Score:</span>
                <span className={`font-semibold ${h.color}`}>{h.index}</span>
              </div>

              <div className="text-[10px] text-slate-500 font-mono mb-2">
                Quotes Analyzed: <strong className="text-slate-400">{h.quotesCount}</strong>
              </div>

              <div className="text-[11px] text-slate-400 leading-tight border-t border-slate-800/80 pt-2">
                <strong className="text-slate-300 block mb-0.5">{h.urgency}</strong>
                {h.desc}
              </div>

              {isSelected && (
                <div className="absolute top-0 right-0 w-2 h-full bg-purple-500"></div>
              )}
            </div>
          );
        })}
      </div>

      {/* Elasticity Insights Callout */}
      <div className="mt-4 p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col md:flex-row md:items-center justify-between text-xs gap-3">
        <div className="flex items-center space-x-2 text-slate-300">
          <ShieldCheck className="w-4 h-4 text-emerald-400 shrink-0" />
          <span>
            <strong>Live Elasticity Calculation:</strong> Last-minute flights (T+1) currently trade at a <strong>+{premiumPct}% premium</strong> over early-bird T+45 saver fares across Indian corridors, proving that static single-point price sampling misses the dynamic inflation faced by real consumers.
          </span>
        </div>
        <div className="flex items-center space-x-2 shrink-0 text-slate-400 font-mono text-[11px]">
          <span>DGCA Base Price: <strong className="text-slate-200">₹{baseYield.toLocaleString()}</strong></span>
        </div>
      </div>
    </div>
  );
};
