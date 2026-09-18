import React from 'react';
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ReferenceLine
} from 'recharts';
import { MOCK_DAILY_CPI } from '../data/mockData';
import { DailyFarePoint } from '../types';
import { Calendar, TrendingUp, DollarSign, Activity } from 'lucide-react';

interface DailyCPIChartProps {
  data?: DailyFarePoint[];
  isLiveScraped?: boolean;
}

export const DailyCPIChart: React.FC<DailyCPIChartProps> = ({
  data = MOCK_DAILY_CPI,
  isLiveScraped = false
}) => {
  const chartData = data && data.length > 0 ? data : MOCK_DAILY_CPI;
  const latestDaily = chartData[chartData.length - 1];
  const todayAvgFare = latestDaily ? `₹${latestDaily.dailyAvgFare.toLocaleString()}` : '₹5,420';
  const movingAvgFare = latestDaily ? `₹${latestDaily.movingAverage7d.toLocaleString()}` : '₹5,520';

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
        <div>
          <div className="flex items-center flex-wrap gap-2">
            <h3 className="text-base font-bold text-white tracking-tight flex items-center">
              <Calendar className="w-5 h-5 text-emerald-400 mr-2" />
              Day-Wise (Daily) Airfare CPI & Average Fare Tracking
            </h3>
            <span className="px-2 py-0.5 text-[10px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 rounded">
              30-Day Daily Series
            </span>
            {isLiveScraped && (
              <span className="px-2 py-0.5 text-[10px] font-mono bg-emerald-500/30 text-emerald-200 border border-emerald-400/60 rounded-full flex items-center gap-1.5 animate-pulse">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
                <Activity className="w-3 h-3 text-emerald-400" />
                Live Scrape Ingested ({latestDaily?.dayLabel})
              </span>
            )}
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Daily price granularity revealing Friday–Sunday weekend surge vs. Tuesday–Wednesday discount cycles
          </p>
        </div>

        <div className="flex items-center space-x-4 text-xs font-mono">
          <div className="text-right">
            <span className="text-slate-400 text-[10px] uppercase block">Today's Avg Fare</span>
            <span className="text-white font-bold text-sm">{todayAvgFare}</span>
          </div>
          <div className="text-right">
            <span className="text-slate-400 text-[10px] uppercase block">7-Day Moving Avg</span>
            <span className="text-sky-400 font-bold text-sm">{movingAvgFare}</span>
          </div>
        </div>
      </div>

      {/* Dual Axis Area/Line Chart */}
      <div className="h-[320px] w-full pt-2">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={chartData} margin={{ top: 10, right: 20, left: -10, bottom: 0 }}>
            <defs>
              <linearGradient id="fareFill" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#10b981" stopOpacity={0.4} />
                <stop offset="95%" stopColor="#10b981" stopOpacity={0.0} />
              </linearGradient>
              <linearGradient id="cpiFill" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#38bdf8" stopOpacity={0.3} />
                <stop offset="95%" stopColor="#38bdf8" stopOpacity={0.0} />
              </linearGradient>
            </defs>

            <CartesianGrid strokeDasharray="3 3" stroke="#334155" opacity={0.5} />
            
            <XAxis
              dataKey="dayLabel"
              stroke="#94a3b8"
              fontSize={11}
              tickLine={false}
              axisLine={{ stroke: '#475569' }}
            />
            
            <YAxis
              yAxisId="cpi"
              domain={[105, 120]}
              stroke="#38bdf8"
              fontSize={11}
              tickLine={false}
              axisLine={{ stroke: '#38bdf8' }}
              tickFormatter={val => `${val}`}
            />
            
            <YAxis
              yAxisId="fare"
              orientation="right"
              domain={[4500, 6500]}
              stroke="#34d399"
              fontSize={11}
              tickLine={false}
              axisLine={{ stroke: '#34d399' }}
              tickFormatter={val => `₹${val}`}
            />

            <Tooltip
              contentStyle={{
                backgroundColor: '#0f172a',
                borderColor: '#334155',
                borderRadius: '12px',
                color: '#f8fafc',
                boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.5)'
              }}
              formatter={(value: any, name: string) => [
                name === 'dailyJevonsIndex' ? `${Number(value).toFixed(1)} (Base=100)` :
                name === 'dailyAvgFare' ? `₹${Number(value).toLocaleString()}` :
                `₹${Number(value).toLocaleString()}`,
                name === 'dailyJevonsIndex' ? 'Daily Jevons Index' :
                name === 'dailyAvgFare' ? 'Daily National Avg Fare' : '7-Day Moving Avg'
              ]}
            />
            
            <Legend verticalAlign="top" height={36} wrapperStyle={{ color: '#cbd5e1', fontSize: '12px' }} />
            
            <Area
              yAxisId="fare"
              type="monotone"
              dataKey="dailyAvgFare"
              name="Daily National Avg Fare (₹)"
              stroke="#34d399"
              strokeWidth={2.5}
              fill="url(#fareFill)"
            />

            <Area
              yAxisId="cpi"
              type="monotone"
              dataKey="dailyJevonsIndex"
              name="Daily Jevons CPI Index"
              stroke="#38bdf8"
              strokeWidth={2.5}
              fill="url(#cpiFill)"
            />

            <Line
              yAxisId="fare"
              type="monotone"
              dataKey="movingAverage7d"
              name="7-Day Moving Average (₹)"
              stroke="#fbbf24"
              strokeWidth={2}
              strokeDasharray="4 2"
              dot={false}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>

      <div className="mt-4 p-3 bg-slate-900/80 rounded-xl border border-slate-800 text-xs flex items-center justify-between text-slate-300">
        <span className="flex items-center text-emerald-400 font-semibold">
          <TrendingUp className="w-4 h-4 mr-1.5" />
          Weekend Surge Finding:
        </span>
        <span>
          Friday–Sunday airfares average <strong className="text-white font-mono">+11.5% higher</strong> than Tuesday–Wednesday mid-week discount fares across all 50 domestic corridors.
        </span>
      </div>
    </div>
  );
};
