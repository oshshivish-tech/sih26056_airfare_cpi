import React from 'react';
import { ArrowRight, Zap, TrendingUp, AlertCircle, PieChart } from 'lucide-react';

interface TransmissionChainProps {
  currentAirfareSurgePct: number;
}

export const TransmissionChain: React.FC<TransmissionChainProps> = ({ currentAirfareSurgePct }) => {
  const transportSubGroupImpact = Number((currentAirfareSurgePct * 0.042).toFixed(2));
  const miscCategoryImpact = Number((currentAirfareSurgePct * 0.018).toFixed(2));
  const headlineCPIImpact = Number((currentAirfareSurgePct * 0.008).toFixed(3));

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6">
      <div className="flex items-center space-x-2 mb-4">
        <div className="p-2 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/30">
          <Zap className="w-5 h-5" />
        </div>
        <div>
          <h3 className="text-base font-bold text-white tracking-tight">
            Airfare Inflation Transmission Chain
          </h3>
          <p className="text-xs text-slate-400">
            Macroeconomic pass-through from daily airfare movement to MoSPI Headline CPI Inflation
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 items-center">
        {/* Step 1: Scraped Airfare Movement */}
        <div className="p-4 bg-slate-900/90 rounded-xl border border-sky-500/40 relative">
          <div className="text-[10px] font-extrabold uppercase text-sky-400 tracking-wider">Step 1: Scraped Airfares</div>
          <div className="text-xl font-black text-white font-mono mt-1">
            +{currentAirfareSurgePct}%
          </div>
          <div className="text-[11px] text-slate-300 mt-1">
            Jevons Airfare Sub-Index
          </div>
        </div>

        {/* Step 2: Transport & Communication */}
        <div className="p-4 bg-slate-900/90 rounded-xl border border-slate-800 relative">
          <div className="text-[10px] font-extrabold uppercase text-slate-400 tracking-wider">Step 2: Transport Group</div>
          <div className="text-xl font-black text-amber-400 font-mono mt-1">
            +{transportSubGroupImpact}%
          </div>
          <div className="text-[11px] text-slate-300 mt-1">
            MoSPI Transport Sub-Group (4.2% wt)
          </div>
        </div>

        {/* Step 3: Misc Expenditure */}
        <div className="p-4 bg-slate-900/90 rounded-xl border border-slate-800 relative">
          <div className="text-[10px] font-extrabold uppercase text-slate-400 tracking-wider">Step 3: Misc Category</div>
          <div className="text-xl font-black text-purple-400 font-mono mt-1">
            +{miscCategoryImpact}%
          </div>
          <div className="text-[11px] text-slate-300 mt-1">
            Miscellaneous Basket (28.3% wt)
          </div>
        </div>

        {/* Step 4: Headline CPI Impact */}
        <div className="p-4 bg-gradient-to-tr from-sky-950/80 to-indigo-950/80 rounded-xl border border-sky-500/60 relative shadow-lg shadow-sky-500/10">
          <div className="text-[10px] font-extrabold uppercase text-emerald-400 tracking-wider">Step 4: Headline CPI</div>
          <div className="text-xl font-black text-emerald-300 font-mono mt-1">
            +{headlineCPIImpact}%
          </div>
          <div className="text-[11px] text-slate-200 mt-1">
            National Inflation Impact
          </div>
        </div>
      </div>
    </div>
  );
};
