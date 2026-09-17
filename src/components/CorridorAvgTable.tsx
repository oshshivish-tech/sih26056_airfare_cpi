import React, { useState } from 'react';
import { MOCK_ROUTE_WEIGHTS } from '../data/mockData';
import { Search, MapPin, ArrowUpDown, Filter, ChevronRight } from 'lucide-react';

interface CorridorAvgTableProps {
  corridorBreakdown: Record<string, { avgFare: number; priceRelative: number; weight: number }>;
}

export const CorridorAvgTable: React.FC<CorridorAvgTableProps> = ({ corridorBreakdown }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [tierFilter, setTierFilter] = useState<'ALL' | 'METRO_METRO' | 'METRO_TIER2' | 'UDAN_REGIONAL'>('ALL');
  const [sortField, setSortField] = useState<'weight' | 'currentFare' | 'changePct'>('weight');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('desc');

  const filteredRoutes = MOCK_ROUTE_WEIGHTS.filter(r => {
    const matchesTier = tierFilter === 'ALL' || r.tierCategory === tierFilter;
    const matchesSearch = r.corridorId.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          r.corridorName.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesTier && matchesSearch;
  });

  const sortedRoutes = [...filteredRoutes].sort((a, b) => {
    const statsA = corridorBreakdown[a.corridorId] || { avgFare: Math.round(a.baseYearPrice * 1.12), priceRelative: 1.12, weight: a.weightPercentage };
    const statsB = corridorBreakdown[b.corridorId] || { avgFare: Math.round(b.baseYearPrice * 1.12), priceRelative: 1.12, weight: b.weightPercentage };

    let valA = 0;
    let valB = 0;

    if (sortField === 'weight') {
      valA = a.weightPercentage;
      valB = b.weightPercentage;
    } else if (sortField === 'currentFare') {
      valA = statsA.avgFare;
      valB = statsB.avgFare;
    } else {
      valA = (statsA.priceRelative - 1.0) * 100;
      valB = (statsB.priceRelative - 1.0) * 100;
    }

    return sortOrder === 'desc' ? valB - valA : valA - valB;
  });

  const handleSort = (field: 'weight' | 'currentFare' | 'changePct') => {
    if (sortField === field) {
      setSortOrder(prev => prev === 'desc' ? 'asc' : 'desc');
    } else {
      setSortField(field);
      setSortOrder('desc');
    }
  };

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6">
      {/* Header & Controls */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
        <div>
          <div className="flex items-center space-x-2">
            <h3 className="text-base font-bold text-white tracking-tight flex items-center">
              <MapPin className="w-5 h-5 text-sky-400 mr-2" />
              Corridor-Wise Average Fare & Weight Table
            </h3>
            <span className="px-2 py-0.5 text-[10px] font-mono bg-sky-500/20 text-sky-300 border border-sky-500/30 rounded">
              {sortedRoutes.length} Corridors Listed
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Individual route average fares (P̄_c), base year benchmarks (P_c,0), and DGCA passenger volume weights (w_c)
          </p>
        </div>

        {/* Controls */}
        <div className="flex flex-wrap items-center gap-3">
          {/* Search Input */}
          <div className="relative min-w-[200px]">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search route (DEL, BOM...)"
              value={searchTerm}
              onChange={e => setSearchTerm(e.target.value)}
              className="w-full bg-slate-900 text-xs text-slate-200 border border-slate-700 rounded-lg pl-9 pr-3 py-1.5 focus:outline-none focus:border-sky-500"
            />
          </div>

          {/* Tier Category Dropdown */}
          <select
            value={tierFilter}
            onChange={(e: any) => setTierFilter(e.target.value)}
            className="bg-slate-900 text-xs text-slate-200 border border-slate-700 rounded-lg px-3 py-1.5 focus:outline-none focus:border-sky-500"
          >
            <option value="ALL">All Route Categories</option>
            <option value="METRO_METRO">Metro ↔ Metro</option>
            <option value="METRO_TIER2">Metro ↔ Tier 2</option>
            <option value="UDAN_REGIONAL">UDAN Regional</option>
          </select>
        </div>
      </div>

      {/* Table Matrix */}
      <div className="overflow-x-auto rounded-xl border border-slate-800">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="border-b border-slate-800 text-slate-400 uppercase text-[10px] font-semibold bg-slate-900/80">
              <th className="py-3 px-4">Corridor Code / Name</th>
              <th className="py-3 px-4">Category</th>
              <th className="py-3 px-4 text-right cursor-pointer hover:text-white" onClick={() => handleSort('weight')}>
                DGCA Weight % {sortField === 'weight' && (sortOrder === 'desc' ? '↓' : '↑')}
              </th>
              <th className="py-3 px-4 text-right">Base Fare (2025)</th>
              <th className="py-3 px-4 text-right cursor-pointer hover:text-white" onClick={() => handleSort('currentFare')}>
                Current Avg Fare (P̄_c) {sortField === 'currentFare' && (sortOrder === 'desc' ? '↓' : '↑')}
              </th>
              <th className="py-3 px-4 text-right cursor-pointer hover:text-white" onClick={() => handleSort('changePct')}>
                Inflation Change {sortField === 'changePct' && (sortOrder === 'desc' ? '↓' : '↑')}
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60 font-mono">
            {sortedRoutes.map(route => {
              // Generate route-specific realistic baseline multiplier based on tier category and corridor ID
              const defaultMultiplier = 
                route.corridorId === 'DEL-BOM' ? 1.141 :
                route.corridorId === 'BLR-DEL' ? 1.120 :
                route.corridorId === 'BOM-BLR' ? 1.106 :
                route.corridorId === 'CCU-DEL' ? 1.135 :
                route.corridorId === 'HYD-DEL' ? 1.118 :
                route.corridorId === 'MAA-DEL' ? 1.122 :
                route.corridorId === 'BOM-GOI' ? 1.152 :
                route.tierCategory === 'METRO_METRO' ? 1.125 :
                route.tierCategory === 'METRO_TIER2' ? 1.098 : 1.062;

              const stats = corridorBreakdown[route.corridorId] || {
                avgFare: Math.round(route.baseYearPrice * defaultMultiplier),
                priceRelative: defaultMultiplier,
                weight: route.weightPercentage
              };

              const changePct = Number(((stats.priceRelative - 1.0) * 100).toFixed(1));

              return (
                <tr key={route.corridorId} className="hover:bg-slate-900/50 transition-colors">
                  <td className="py-3 px-4">
                    <span className="font-bold text-white">{route.corridorId}</span>
                    <span className="block text-[11px] font-sans text-slate-400 font-normal">{route.corridorName}</span>
                  </td>

                  <td className="py-3 px-4 font-sans">
                    <span className={`px-2 py-0.5 text-[10px] font-semibold rounded border ${
                      route.tierCategory === 'METRO_METRO'
                        ? 'bg-sky-500/10 text-sky-300 border-sky-500/30'
                        : route.tierCategory === 'METRO_TIER2'
                        ? 'bg-amber-500/10 text-amber-300 border-amber-500/30'
                        : 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30'
                    }`}>
                      {route.tierCategory.replace('_', ' ')}
                    </span>
                  </td>

                  <td className="py-3 px-4 text-right font-bold text-sky-400">
                    {route.weightPercentage}%
                  </td>

                  <td className="py-3 px-4 text-right text-slate-400">
                    ₹{route.baseYearPrice.toLocaleString()}
                  </td>

                  <td className="py-3 px-4 text-right font-bold text-white text-sm">
                    ₹{stats.avgFare.toLocaleString()}
                  </td>

                  <td className="py-3 px-4 text-right">
                    <span className={`px-2 py-0.5 rounded font-bold ${
                      changePct > 10 ? 'bg-rose-500/20 text-rose-400 border border-rose-500/30' :
                      changePct > 5 ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30' :
                      'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
                    }`}>
                      {changePct >= 0 ? `+${changePct}%` : `${changePct}%`}
                    </span>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
