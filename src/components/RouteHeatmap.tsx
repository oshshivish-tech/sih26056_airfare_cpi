import React, { useState } from 'react';
import { RouteWeight } from '../types';
import { MOCK_ROUTE_WEIGHTS } from '../data/mockData';
import { MapPin, ArrowUpDown, Filter, ShieldAlert, LayoutGrid, Table, Flame, TrendingUp } from 'lucide-react';

interface RouteHeatmapProps {
  corridorBreakdown: Record<string, { avgFare: number; priceRelative: number; weight: number }>;
}

export const RouteHeatmap: React.FC<RouteHeatmapProps> = ({ corridorBreakdown }) => {
  const [filterCategory, setFilterCategory] = useState<'ALL' | 'METRO_METRO' | 'METRO_TIER2' | 'UDAN_REGIONAL'>('ALL');
  const [sortBy, setSortBy] = useState<'weight' | 'fare' | 'change'>('weight');
  const [viewMode, setViewMode] = useState<'matrix' | 'cards'>('matrix');

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

  // Booking Horizons for 2D Heatmap Matrix
  const horizons = [
    { code: '1d', label: 'T+1 Urgent', mult: 1.18, desc: '1 Day Out (Emergency Flexi)' },
    { code: '7d', label: 'T+7 Business', mult: 1.08, desc: '7 Days Out (Corporate Rush)' },
    { code: '14d', label: 'T+14 Standard', mult: 1.01, desc: '14 Days Out (Advance Purchase)' },
    { code: '30d', label: 'T+30 Leisure', mult: 0.94, desc: '30 Days Out (Vacation Threshold)' },
    { code: '45d', label: 'T+45 Holiday', mult: 0.89, desc: '45 Days Out (Early Bird Saver)' },
  ];

  // Helper function to color cells based on price surge vs base fare
  const getHeatmapColor = (fare: number, basePrice: number) => {
    const surgeRatio = fare / basePrice;
    if (surgeRatio >= 1.15) {
      return 'bg-rose-950/70 text-rose-300 border-rose-800/60 font-bold';
    } else if (surgeRatio >= 1.05) {
      return 'bg-amber-950/50 text-amber-300 border-amber-800/50 font-semibold';
    } else if (surgeRatio >= 0.98) {
      return 'bg-emerald-950/40 text-emerald-300 border-emerald-800/40';
    } else {
      return 'bg-teal-950/50 text-teal-300 border-teal-800/50';
    }
  };

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6">
      {/* Header & Controls */}
      <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 mb-6">
        <div>
          <div className="flex items-center space-x-2">
            <h2 className="text-lg font-bold text-white tracking-tight flex items-center">
              <Flame className="w-5 h-5 text-amber-400 mr-2" />
              Domestic Air Corridor Price Index Heatmap & Matrix
            </h2>
            <span className="px-2 py-0.5 text-[10px] font-mono bg-sky-500/20 text-sky-300 border border-sky-500/30 rounded">
              12 Corridors × 5 Horizons
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            DGCA Passenger Volume Weighted Corridors with Lead-Time Dynamic Pricing Heat Intensity
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          {/* View Mode Toggle */}
          <div className="flex items-center bg-slate-900 border border-slate-700 rounded-lg p-0.5">
            <button
              onClick={() => setViewMode('matrix')}
              className={`flex items-center space-x-1 px-2.5 py-1 rounded-md text-xs font-semibold transition-all ${
                viewMode === 'matrix'
                  ? 'bg-sky-600 text-white shadow-sm'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
              title="2D Heatmap Matrix View"
            >
              <Table className="w-3.5 h-3.5" />
              <span>Heatmap Matrix</span>
            </button>
            <button
              onClick={() => setViewMode('cards')}
              className={`flex items-center space-x-1 px-2.5 py-1 rounded-md text-xs font-semibold transition-all ${
                viewMode === 'cards'
                  ? 'bg-sky-600 text-white shadow-sm'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
              title="Corridor Card Grid View"
            >
              <LayoutGrid className="w-3.5 h-3.5" />
              <span>Card Grid</span>
            </button>
          </div>

          {/* Category Filter */}
          <select
            value={filterCategory}
            onChange={(e: any) => setFilterCategory(e.target.value)}
            className="bg-slate-900 text-xs text-slate-200 border border-slate-700 rounded-lg px-3 py-1.5 focus:outline-none focus:border-sky-500"
          >
            <option value="ALL">All Categories (12 Corridors)</option>
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
            <option value="change">Sort by Highest Surge %</option>
          </select>
        </div>
      </div>

      {/* Heatmap Legend */}
      <div className="flex flex-wrap items-center justify-between gap-3 text-xs mb-4 p-3 bg-slate-900/60 rounded-xl border border-slate-800">
        <span className="text-slate-400 font-medium">Price Relative Heat Intensity:</span>
        <div className="flex flex-wrap items-center gap-4">
          <span className="flex items-center text-rose-300">
            <span className="w-3 h-3 rounded bg-rose-950 border border-rose-800 mr-1.5"></span>
            Surge Alert (&gt;+15% above base)
          </span>
          <span className="flex items-center text-amber-300">
            <span className="w-3 h-3 rounded bg-amber-950 border border-amber-800 mr-1.5"></span>
            Moderate Surge (+5% to +15%)
          </span>
          <span className="flex items-center text-emerald-300">
            <span className="w-3 h-3 rounded bg-emerald-950 border border-emerald-800 mr-1.5"></span>
            Baseline / Normal (0% to +5%)
          </span>
          <span className="flex items-center text-teal-300">
            <span className="w-3 h-3 rounded bg-teal-950 border border-teal-800 mr-1.5"></span>
            Early Saver Discount (&lt;0%)
          </span>
        </div>
      </div>

      {/* VIEW MODE 1: 2D CORRIDOR × HORIZON HEATMAP MATRIX */}
      {viewMode === 'matrix' && (
        <div className="overflow-x-auto rounded-xl border border-slate-800 shadow-xl">
          <table className="w-full text-left border-collapse text-xs">
            <thead>
              <tr className="border-b border-slate-800 text-slate-400 uppercase text-[10px] font-semibold bg-slate-900/90">
                <th className="py-3 px-4 sticky left-0 bg-slate-900 z-10">Corridor / Name</th>
                <th className="py-3 px-3 text-center">Category</th>
                <th className="py-3 px-3 text-right">DGCA Wt (w_c)</th>
                <th className="py-3 px-3 text-right">Base Fare (P_0)</th>
                {horizons.map(h => (
                  <th key={h.code} className="py-3 px-3 text-center" title={h.desc}>
                    <div className="text-white font-bold">{h.label}</div>
                    <div className="text-[9px] text-slate-400 font-normal">{(h.mult >= 1 ? `+${Math.round((h.mult - 1) * 100)}%` : `${Math.round((h.mult - 1) * 100)}%`)}</div>
                  </th>
                ))}
                <th className="py-3 px-3 text-right">Current Avg (P̄_c)</th>
                <th className="py-3 px-4 text-right">Price Rel</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 font-mono">
              {sortedRoutes.map(route => {
                const stats = corridorBreakdown[route.corridorId] || {
                  avgFare: Math.round(route.baseYearPrice * 1.12),
                  priceRelative: 1.12,
                  weight: route.weightPercentage
                };

                const pctChange = Number(((stats.priceRelative - 1.0) * 100).toFixed(1));

                return (
                  <tr key={route.corridorId} className="hover:bg-slate-900/40 transition-colors">
                    {/* Route Code & Name */}
                    <td className="py-2.5 px-4 sticky left-0 bg-slate-950/90 z-10 border-r border-slate-800/80">
                      <span className="font-bold text-white tracking-wider">{route.corridorId}</span>
                      <span className="block text-[11px] font-sans text-slate-400 font-normal truncate max-w-[180px]">
                        {route.corridorName}
                      </span>
                    </td>

                    {/* Category Pill */}
                    <td className="py-2.5 px-3 text-center font-sans">
                      <span className={`px-2 py-0.5 text-[9px] font-semibold rounded border ${
                        route.tierCategory === 'METRO_METRO'
                          ? 'bg-sky-500/10 text-sky-300 border-sky-500/30'
                          : route.tierCategory === 'METRO_TIER2'
                          ? 'bg-amber-500/10 text-amber-300 border-amber-500/30'
                          : 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30'
                      }`}>
                        {route.tierCategory === 'METRO_METRO' ? 'Metro' : route.tierCategory === 'METRO_TIER2' ? 'Tier-2' : 'UDAN'}
                      </span>
                    </td>

                    {/* DGCA Normalized Weight */}
                    <td className="py-2.5 px-3 text-right font-bold text-sky-400">
                      {route.weightPercentage}%
                    </td>

                    {/* Baseline Oct 2025 Fare */}
                    <td className="py-2.5 px-3 text-right text-slate-400">
                      ₹{route.baseYearPrice.toLocaleString()}
                    </td>

                    {/* 5 Lead-Time Heatmap Cells */}
                    {horizons.map(h => {
                      const horizonFare = Math.round(stats.avgFare * (h.mult / 1.01)); // Normalized to current avg
                      const cellClass = getHeatmapColor(horizonFare, route.baseYearPrice);

                      return (
                        <td key={h.code} className="py-2 px-2 text-center">
                          <div className={`py-1.5 px-2 rounded-lg border text-xs transition-transform hover:scale-105 ${cellClass}`}>
                            ₹{horizonFare.toLocaleString()}
                          </div>
                        </td>
                      );
                    })}

                    {/* Current Average Fare */}
                    <td className="py-2.5 px-3 text-right font-bold text-white text-sm">
                      ₹{stats.avgFare.toLocaleString()}
                    </td>

                    {/* Relative Inflation / Surge Tag */}
                    <td className="py-2.5 px-4 text-right">
                      <span className={`px-2 py-0.5 rounded font-bold text-xs border ${
                        pctChange > 10 ? 'bg-rose-500/20 text-rose-400 border-rose-500/30' :
                        pctChange > 5 ? 'bg-amber-500/20 text-amber-400 border-amber-500/30' :
                        'bg-emerald-500/20 text-emerald-400 border-emerald-500/30'
                      }`}>
                        {pctChange >= 0 ? `+${pctChange}%` : `${pctChange}%`}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      {/* VIEW MODE 2: CORRIDOR CARDS GRID */}
      {viewMode === 'cards' && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {sortedRoutes.map(route => {
            const stats = corridorBreakdown[route.corridorId] || {
              avgFare: Math.round(route.baseYearPrice * 1.12),
              priceRelative: 1.12,
              weight: route.weightPercentage
            };

            const pctChange = Number(((stats.priceRelative - 1.0) * 100).toFixed(1));
            const isHighSurge = pctChange > 10.0;
            const isModerate = pctChange > 5.0 && pctChange <= 10.0;

            return (
              <div
                key={route.corridorId}
                className={`p-4 rounded-xl border transition-all ${
                  isHighSurge
                    ? 'bg-rose-950/20 border-rose-900/50 hover:border-rose-500/60 shadow-lg shadow-rose-950/20'
                    : isModerate
                    ? 'bg-amber-950/15 border-amber-900/40 hover:border-amber-500/50'
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

                {/* Lead-Time Horizons Quick Spread */}
                <div className="grid grid-cols-5 gap-1 mb-3 pt-2 border-t border-slate-800/60">
                  {horizons.map(h => {
                    const hFare = Math.round(stats.avgFare * (h.mult / 1.01));
                    return (
                      <div key={h.code} className="text-center bg-slate-950/60 p-1 rounded border border-slate-800/80">
                        <div className="text-[8px] text-slate-400 font-sans">{h.code}</div>
                        <div className="text-[10px] font-mono text-slate-200 font-semibold">₹{Math.round(hFare / 1000)}k</div>
                      </div>
                    );
                  })}
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
                    <div className="text-[10px] text-slate-400 uppercase font-semibold">Surge Relative</div>
                    <div className={`text-sm font-bold font-mono ${
                      pctChange > 10 ? 'text-rose-400' :
                      pctChange > 5 ? 'text-amber-400' :
                      'text-emerald-400'
                    }`}>
                      {pctChange >= 0 ? `+${pctChange}%` : `${pctChange}%`}
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
