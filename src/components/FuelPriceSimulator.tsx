import React, { useState } from 'react';
import { Sliders, Zap, TrendingUp, AlertTriangle } from 'lucide-react';

interface FuelPriceSimulatorProps {
  baseJevonsIndex: number;
}

export const FuelPriceSimulator: React.FC<FuelPriceSimulatorProps> = ({ baseJevonsIndex }) => {
  const [atfChangePct, setAtfChangePct] = useState<number>(10); // +10% ATF surge
  const [gstChangePct, setGstChangePct] = useState<number>(0);  // 0% GST change

  // Fuel is ~40% of airline operating cost
  const simulatedFareIncreasePct = Number(((atfChangePct * 0.40) + (gstChangePct * 0.8)).toFixed(1));
  const simulatedIndexValue = Number((baseJevonsIndex * (1 + simulatedFareIncreasePct / 100)).toFixed(1));
  const simulatedCPIImpact = Number((simulatedFareIncreasePct * 0.008).toFixed(3));

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6">
      <div className="flex items-center space-x-2 mb-4">
        <div className="p-2 rounded-xl bg-indigo-500/10 text-indigo-400 border border-indigo-500/30">
          <Sliders className="w-5 h-5" />
        </div>
        <div>
          <h3 className="text-base font-bold text-white tracking-tight">
            What-If Policy & ATF Fuel Price Simulator
          </h3>
          <p className="text-xs text-slate-400">
            Simulate macroeconomic shocks (Aviation Turbine Fuel hikes & GST changes) on MoSPI Airfare CPI
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-center">
        {/* Sliders Control */}
        <div className="space-y-4 lg:col-span-2">
          {/* Slider 1: ATF Price Surge */}
          <div>
            <div className="flex justify-between text-xs font-medium text-slate-300 mb-1.5">
              <span>Aviation Turbine Fuel (ATF) Price Change:</span>
              <strong className="font-mono text-amber-400">{atfChangePct >= 0 ? `+${atfChangePct}%` : `${atfChangePct}%`}</strong>
            </div>
            <input
              type="range"
              min="-20"
              max="40"
              step="1"
              value={atfChangePct}
              onChange={(e) => setAtfChangePct(Number(e.target.value))}
              className="w-full h-2 bg-slate-900 rounded-lg appearance-none cursor-pointer accent-amber-400"
            />
            <div className="flex justify-between text-[10px] text-slate-500 mt-1">
              <span>-20% (Fuel Drop)</span>
              <span>Baseline (0%)</span>
              <span>+40% (Global Oil Spike)</span>
            </div>
          </div>

          {/* Slider 2: GST Policy Shift */}
          <div>
            <div className="flex justify-between text-xs font-medium text-slate-300 mb-1.5">
              <span>Economy Airfare GST Tax Change:</span>
              <strong className="font-mono text-purple-400">{gstChangePct >= 0 ? `+${gstChangePct}%` : `${gstChangePct}%`}</strong>
            </div>
            <input
              type="range"
              min="-5"
              max="13"
              step="1"
              value={gstChangePct}
              onChange={(e) => setGstChangePct(Number(e.target.value))}
              className="w-full h-2 bg-slate-900 rounded-lg appearance-none cursor-pointer accent-purple-400"
            />
            <div className="flex justify-between text-[10px] text-slate-500 mt-1">
              <span>-5% Tax Exemption</span>
              <span>Current (5% GST)</span>
              <span>18% Standard GST</span>
            </div>
          </div>
        </div>

        {/* Output Simulator Card */}
        <div className="p-4 bg-slate-900/90 rounded-xl border border-indigo-500/40 text-xs space-y-3">
          <div className="text-[10px] font-extrabold uppercase text-indigo-400 tracking-wider">Simulated Index Outcome</div>
          
          <div className="flex items-baseline justify-between">
            <span className="text-slate-400">Baseline CPI Index:</span>
            <span className="font-mono text-slate-200 font-bold">{baseJevonsIndex.toFixed(1)}</span>
          </div>

          <div className="flex items-baseline justify-between">
            <span className="text-slate-400">Simulated Airfare Surge:</span>
            <span className="font-mono text-amber-400 font-bold">+{simulatedFareIncreasePct}%</span>
          </div>

          <div className="flex items-baseline justify-between pt-2 border-t border-slate-800">
            <span className="text-white font-bold">New Forecast CPI Index:</span>
            <span className="font-mono text-xl font-extrabold text-sky-400">{simulatedIndexValue}</span>
          </div>

          <div className="text-[11px] text-emerald-400 font-medium">
            Impact on Headline CPI: <strong>+{simulatedCPIImpact}% pts</strong>
          </div>
        </div>
      </div>
    </div>
  );
};
