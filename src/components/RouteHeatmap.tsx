import React, { useState } from 'react';
import { RouteWeight } from '../types';
import { MOCK_ROUTE_WEIGHTS } from '../data/mockData';
import { MapPin, ArrowUpDown, Filter, ShieldAlert } from 'lucide-react';

interface RouteHeatmapProps {
  corridorBreakdown: Record<string, { avgFare: number; priceRelative: number; weight: number }>;
}

export const RouteHeatmap: React.FC<RouteHeatmapProps> = ({ corridorBreakdown }) => {
  const [filterCategory, setFilterCategory] = useState<'ALL' | 'METRO_METRO' | 'METRO_TIER2' | 'UDAN_REGIONAL'>('ALL');
  const [sortBy, setSortBy] = useState<'weight' | 'fare' | 'change'>('weight');

  const filteredRoutes = MOCK_ROUTE_WEIGHTS.filter(r => {
    if (filterCategory === 'ALL') return true;
    return r.tierCategory === filterCategory;
  });

  const sortedRoutes = [...filteredRoutes].sort((a, b) => {
    const fareA = corridorBreakdown[a.corridorId]?.avgFare || a.baseYearPrice;
    const fareB = corridorBreakdown[b.corridorId]?.avgFare || b.baseYearPrice;
    const relA = corridorBreakdown[a.corridorId]?.priceRelative || 1.0;
    const relB = corridorBreakdown[b.corridorId]?.priceRelative || 1.0;

    if (sortBy === 'weight') return b.weightPercentage - a.weightPercentage;
    if (sortBy === 'fare') return fareB - fareA;
    return relB - relA;
  });

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6">
      {/* Header & Controls */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
        <div>
          <h2 className="text-lg font-bold text-white tracking-tight flex items-center">
            <MapPin className="w-5 h-5 text-sky-400 mr-2" />
            Domestic Air Corridor Price Index Matrix
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            DGCA Passenger Volume Weighted Corridors & Real-Time Scraped Average Fares
          </p>
        </div>

        <div className="flex items-center gap-3">
          {/* Category Filter */}
          <select
            value={filterCategory}
            onChange={(e: any) => setFilterCategory(e.target.value)}
            className="bg-slate-900 text-xs text-slate-200 border border-slate-700 rounded-lg px-3 py-1.5 focus:outline-none focus:border-sky-500"
          >
            <option value="ALL">All Categories (50 Corridors)</option>
            <option value="METRO_METRO">Metro ↔ Metro Corridors</option>
            <option value="METRO_TIER2">Metro ↔ Tier 2 Corridors</option>
            <option value="UDAN_REGIONAL">UDAN Regional Routes</option>
          </select>

          {/* Sort By */}
          <select
            value={sortBy}
            onChange={(e: any) => setSortBy(e.target.value)}
            className="bg-slate-900 text-xs text-slate-200 border border-slate-700 rounded-lg px-3 py-1.5 focus:outline-none focus:border-sky-500"
          >
            <option value="weight">Sort by DGCA Weight %</option>
            <option value="fare">Sort by Highest Fare</option>
            <option value="change">Sort by Highest Inflation</option>
          </select>
        </div>
      </div>

      {/* Grid Matrix */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {sortedRoutes.map(route => {
          const stats = corridorBreakdown[route.corridorId] || {
            avgFare: Math.round(route.baseYearPrice * 1.12),
            priceRelative: 1.12,
            weight: route.weightPercentage
          };

          const pctChange = Number(((stats.priceRelative - 1.0) * 100).toFixed(1));
          const isHighSurge = pctChange > 10.0;

          return (
            <div
              key={route.corridorId}
              className={`p-4 rounded-xl border transition-all ${
                isHighSurge
                  ? 'bg-rose-950/20 border-rose-900/40 hover:border-rose-500/50'
                  : 'bg-slate-900/70 border-slate-800 hover:border-sky-500/40'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <span className="font-mono font-bold text-sm text-white">
                  {route.corridorId}
                </span>
                <span className={`text-[10px] font-semibold px-2 py-0.5 rounded-full border ${
                  route.tierCategory === 'METRO_METRO'
                    ? 'bg-sky-500/10 text-sky-300 border-sky-500/30'
                    : route.tierCategory === 'METRO_TIER2'
                    ? 'bg-amber-500/10 text-amber-300 border-amber-500/30'
                    : 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30'
                }`}>
                  {route.tierCategory.replace('_', ' ')}
                </span>
              </div>

              <div className="text-xs text-slate-300 mb-3 truncate">
                {route.corridorName}
              </div>

              <div className="flex items-baseline justify-between pt-2 border-t border-slate-800/80">
                <div>
                  <div className="text-[10px] text-slate-400 uppercase font-semibold">Average Fare</div>
                  <div className="text-lg font-bold text-white font-mono">
                    ₹{stats.avgFare.toLocaleString()}
                  </div>
                </div>

                <div className="text-right">
                  <div className="text-[10px] text-slate-400 uppercase font-semibold">DGCA Weight</div>
                  <div className="text-sm font-semibold text-sky-400 font-mono">
                    {route.weightPercentage}%
                  </div>
                </div>

                <div className="text-right">
                  <div className="text-[10px] text-slate-400 uppercase font-semibold">Rel Index</div>
                  <div className={`text-sm font-bold font-mono ${pctChange >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {pctChange >= 0 ? `+${pctChange}%` : `${pctChange}%`}
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
