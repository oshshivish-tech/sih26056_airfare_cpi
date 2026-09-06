import React from 'react';
import { OutlierRecord } from '../types';
import { X, Filter, AlertTriangle, ShieldCheck, Check } from 'lucide-react';

interface OutlierAnalysisModalProps {
  isOpen: boolean;
  onClose: () => void;
  outliers: OutlierRecord[];
}

export const OutlierAnalysisModal: React.FC<OutlierAnalysisModalProps> = ({
  isOpen,
  onClose,
  outliers
}) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-fadeIn">
      <div className="glass-panel w-full max-w-4xl rounded-2xl border border-slate-700 shadow-2xl overflow-hidden max-h-[90vh] flex flex-col">
        {/* Modal Header */}
        <div className="px-6 py-4 bg-slate-900/90 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/30">
              <Filter className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white tracking-tight">
                Statistical Outlier & Anomaly Pruning Log
              </h3>
              <p className="text-xs text-slate-400">
                Automated IQR (Interquartile Range) & Z-Score Noise Filter for MoSPI CPI Calculations
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Content */}
        <div className="p-6 overflow-y-auto space-y-4 text-xs">
          <div className="p-4 bg-slate-900/80 rounded-xl border border-slate-800 flex items-start space-x-3">
            <ShieldCheck className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
            <div className="text-slate-300">
              <strong className="text-white">Why Outlier Pruning Matters for MoSPI: </strong>
              Dynamic airline pricing algorithms occasionally list emergency last-minute scalping fares (e.g. ₹38,900 for a ₹5,400 economy ticket). If uncorrected, these extreme spikes corrupt the Consumer Price Index. Our engine computes route-specific IQR upper bounds ($Q3 + 2.0 \times IQR$) and automatically excludes or adjusts anomalous quotes.
            </div>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b border-slate-800 text-slate-400 uppercase text-[10px] font-semibold bg-slate-900/50">
                  <th className="py-2.5 px-3">Flight / Airline</th>
                  <th className="py-2.5 px-3">Corridor</th>
                  <th className="py-2.5 px-3">Observed Fare</th>
                  <th className="py-2.5 px-3">Route Median</th>
                  <th className="py-2.5 px-3">Z-Score</th>
                  <th className="py-2.5 px-3">Anomaly Reason</th>
                  <th className="py-2.5 px-3 text-right">Action Taken</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60 font-mono">
                {outliers.map(out => (
                  <tr key={out.id} className="hover:bg-slate-900/40">
                    <td className="py-2.5 px-3 font-semibold text-white">
                      {out.flightNumber}
                      <span className="block text-[10px] text-slate-400 font-sans font-normal">{out.airline}</span>
                    </td>
                    <td className="py-2.5 px-3 text-slate-300">{out.corridor}</td>
                    <td className="py-2.5 px-3 font-bold text-rose-400">₹{out.observedFare.toLocaleString()}</td>
                    <td className="py-2.5 px-3 text-slate-300">₹{out.expectedRouteMedianFare.toLocaleString()}</td>
                    <td className="py-2.5 px-3 text-amber-400">{out.zScore} σ</td>
                    <td className="py-2.5 px-3">
                      <span className="px-2 py-0.5 text-[10px] font-sans font-semibold rounded bg-amber-500/10 text-amber-300 border border-amber-500/30">
                        {out.reason.replace(/_/g, ' ')}
                      </span>
                    </td>
                    <td className="py-2.5 px-3 text-right font-sans">
                      <span className={`px-2 py-0.5 text-[10px] font-bold rounded ${
                        out.action === 'EXCLUDED_FROM_INDEX'
                          ? 'bg-rose-500/20 text-rose-300 border border-rose-500/40'
                          : 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
                      }`}>
                        {out.action.replace(/_/g, ' ')}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Modal Footer */}
        <div className="px-6 py-3 bg-slate-900/90 border-t border-slate-800 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg text-xs font-semibold bg-sky-600 hover:bg-sky-500 text-white transition-all shadow"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
};
