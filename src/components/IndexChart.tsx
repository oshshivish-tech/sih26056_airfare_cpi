import React, { useState } from 'react';
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ReferenceLine
} from 'recharts';
import { CPIIndexPoint, LeadTimeHorizon } from '../types';
import { Info, HelpCircle } from 'lucide-react';

interface IndexChartProps {
  data: CPIIndexPoint[];
  selectedLeadTime: LeadTimeHorizon | 'ALL';
  onSelectLeadTime: (horizon: LeadTimeHorizon | 'ALL') => void;
  isLiveScraped?: boolean;
}

export const IndexChart: React.FC<IndexChartProps> = ({
  data,
  selectedLeadTime,
  onSelectLeadTime,
  isLiveScraped = false
}) => {
  const [visibleSeries, setVisibleSeries] = useState({
    jevons: true,
    weighted: true,
    dutot: false,
    baseline: true
  });

  const toggleSeries = (key: keyof typeof visibleSeries) => {
    setVisibleSeries(prev => ({ ...prev, [key]: !prev[key] }));
  };

  // Lead-Time Index Multipliers (ILO Composition Bias Correction Scaling)
  const leadTimeMultipliers: Record<LeadTimeHorizon | 'ALL', number> = {
    'ALL': 1.0,
    '1d': 1.42,  // Urgent 1-day surge fares (+42% index level)
    '7d': 1.18,  // Business 7-day fares (+18% index level)
    '15d': 1.02, // Standard advance purchase (+2% index level)
    '30d': 0.88, // Leisure 30-day fares (-12% index level)
    '45d': 0.81  // Holiday 45-day far-advance fares (-19% index level)
  };

  const mult = leadTimeMultipliers[selectedLeadTime] || 1.0;

  const chartData = data.map(point => ({
    ...point,
    jevonsIndex: Number((point.jevonsIndex * mult).toFixed(1)),
    dutotIndex: Number((point.dutotIndex * mult).toFixed(1)),
    weightedLaspeyresIndex: Number((point.weightedLaspeyresIndex * mult).toFixed(1)),
  }));

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6">
      {/* Chart Header & Filters */}
      <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 mb-6">
        <div>
          <div className="flex items-center flex-wrap gap-2">
            <h2 className="text-lg font-bold text-white tracking-tight">
              Consumer Price Index (CPI) Airfare Trajectory
            </h2>
            <span className="px-2 py-0.5 text-[10px] font-mono bg-sky-500/20 text-sky-300 border border-sky-500/30 rounded">
              Base Year 2025 = 100
            </span>
            {isLiveScraped && (
              <span className="px-2 py-0.5 text-[10px] font-mono bg-emerald-500/25 text-emerald-300 border border-emerald-500/40 rounded-full flex items-center gap-1.5 animate-pulse">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
                Live Index Ingestion Active (Sep 2026)
              </span>
            )}
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Comparison of Automated Real-Time Index (Jevons/Laspeyres) vs. Manual MoSPI Benchmark
          </p>
        </div>

        {/* Lead Time Horizon Filters */}
        <div className="flex flex-wrap items-center gap-2">
          <span className="text-xs text-slate-400 font-medium mr-1">Booking Window:</span>
          {(['ALL', '1d', '7d', '15d', '30d', '45d'] as const).map(horizon => (
            <button
              key={horizon}
              onClick={() => onSelectLeadTime(horizon)}
              className={`px-3 py-1 text-xs font-semibold rounded-lg border transition-all ${
                selectedLeadTime === horizon
                  ? 'bg-sky-500 text-white border-sky-400 shadow-md shadow-sky-500/20'
                  : 'bg-slate-900/60 text-slate-400 border-slate-800 hover:bg-slate-800 hover:text-slate-200'
              }`}
            >
              {horizon === 'ALL' ? 'All Lead Times' : horizon === '1d' ? '1-Day (Urgent)' : horizon === '7d' ? '7-Day' : horizon === '15d' ? '15-Day' : horizon === '30d' ? '30-Day' : '45-Day (Leisure)'}
            </button>
          ))}
        </div>
      </div>

      {/* Series Toggle Checkboxes */}
      <div className="flex flex-wrap items-center gap-4 mb-4 pb-3 border-b border-slate-800/80 text-xs">
        <span className="text-slate-400 font-medium">Formulas Displayed:</span>
        <button
          onClick={() => toggleSeries('jevons')}
          className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-md transition-all ${
            visibleSeries.jevons
              ? 'bg-sky-500/20 text-sky-300 border border-sky-500/40'
              : 'bg-slate-900 text-slate-500 border border-slate-800'
          }`}
        >
          <span className="w-2.5 h-2.5 rounded-full bg-sky-400"></span>
          <span>Jevons Index (Geometric)</span>
        </button>

        <button
          onClick={() => toggleSeries('weighted')}
          className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-md transition-all ${
            visibleSeries.weighted
              ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
              : 'bg-slate-900 text-slate-500 border border-slate-800'
          }`}
        >
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
          <span>DGCA Weighted Laspeyres</span>
        </button>

        <button
          onClick={() => toggleSeries('baseline')}
          className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-md transition-all ${
            visibleSeries.baseline
              ? 'bg-purple-500/20 text-purple-300 border border-purple-500/40'
              : 'bg-slate-900 text-slate-500 border border-slate-800'
          }`}
        >
          <span className="w-2.5 h-2.5 rounded-full bg-purple-400"></span>
          <span>Manual MoSPI CPI Baseline</span>
        </button>

        <button
          onClick={() => toggleSeries('dutot')}
          className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-md transition-all ${
            visibleSeries.dutot
              ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
              : 'bg-slate-900 text-slate-500 border border-slate-800'
          }`}
        >
          <span className="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
          <span>Dutot Index (Arithmetic)</span>
        </button>
      </div>

      {/* Chart Container */}
      <div className="h-[360px] w-full pt-2">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={chartData} margin={{ top: 10, right: 20, left: -10, bottom: 0 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#334155" opacity={0.5} />
            <XAxis
              dataKey="periodLabel"
              stroke="#94a3b8"
              fontSize={12}
              tickLine={false}
              axisLine={{ stroke: '#475569' }}
            />
            <YAxis
              domain={[75, 170]}
              stroke="#94a3b8"
              fontSize={12}
              tickLine={false}
              axisLine={{ stroke: '#475569' }}
              tickFormatter={val => `${val}`}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: '#0f172a',
                borderColor: '#334155',
                borderRadius: '12px',
                color: '#f8fafc',
                boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.5)'
              }}
              formatter={(value: any, name: string, item: any) => {
                const key = item?.dataKey || name;
                const displayName = 
                  key === 'jevonsIndex' || name.includes('Jevons') ? 'Jevons Index (Geometric)' :
                  key === 'weightedLaspeyresIndex' || name.includes('DGCA') ? 'DGCA Weighted Index' :
                  key === 'officialMoSPICPIBaseline' || name.includes('MoSPI') ? 'Manual MoSPI Baseline' :
                  'Dutot Index (Arithmetic)';
                return [`${Number(value).toFixed(2)} (Base=100)`, displayName];
              }}
            />
            <Legend verticalAlign="top" height={36} wrapperStyle={{ color: '#cbd5e1', fontSize: '12px' }} />
            <ReferenceLine y={100} stroke="#64748b" strokeDasharray="3 3" label={{ value: 'Base Year = 100', fill: '#64748b', fontSize: 10 }} />

            {visibleSeries.jevons && (
              <Line
                type="monotone"
                dataKey="jevonsIndex"
                name="Jevons Index (Geometric)"
                stroke="#38bdf8"
                strokeWidth={3}
                dot={{ r: 4, fill: '#38bdf8' }}
                activeDot={{ r: 7, stroke: '#e0f2fe', strokeWidth: 2 }}
              />
            )}

            {visibleSeries.weighted && (
              <Line
                type="monotone"
                dataKey="weightedLaspeyresIndex"
                name="DGCA Weighted Index"
                stroke="#34d399"
                strokeWidth={2.5}
                strokeDasharray="4 2"
                dot={{ r: 3, fill: '#34d399' }}
              />
            )}

            {visibleSeries.baseline && (
              <Line
                type="monotone"
                dataKey="officialMoSPICPIBaseline"
                name="Manual MoSPI Baseline"
                stroke="#c084fc"
                strokeWidth={2}
                strokeDasharray="6 3"
                dot={{ r: 3, fill: '#c084fc' }}
              />
            )}

            {visibleSeries.dutot && (
              <Line
                type="monotone"
                dataKey="dutotIndex"
                name="Dutot Index (Arithmetic)"
                stroke="#fbbf24"
                strokeWidth={2}
                dot={{ r: 3, fill: '#fbbf24' }}
              />
            )}
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Statistical Insight Footer */}
      <div className="mt-4 p-3.5 bg-slate-900/90 rounded-xl border border-slate-800 text-xs flex items-start space-x-3 text-slate-300">
        <Info className="w-4 h-4 text-sky-400 flex-shrink-0 mt-0.5" />
        <div>
          <strong className="text-white">UN/ILO CPI Guideline Note: </strong>
          The <strong>Jevons Geometric Index</strong> is the international statistical gold standard for unweighted airfare item groups because it satisfies the <em>Time Reversal Test</em> and protects the index from upward substitution bias caused by dynamic airline surge pricing algorithms.
        </div>
      </div>
    </div>
  );
};
