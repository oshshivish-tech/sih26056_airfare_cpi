import React, { useState } from 'react';
import { Plane, Navigation, Info, Eye, RotateCcw } from 'lucide-react';
import { MOCK_ROUTE_WEIGHTS } from '../data/mockData';

interface CityNode {
  id: string;
  name: string;
  x: number; // SVG percentage x
  y: number; // SVG percentage y
}

// 12 Hub Cities covering all 12 DGCA Representative Corridors
const CITIES: Record<string, CityNode> = {
  DEL: { id: 'DEL', name: 'Delhi', x: 42, y: 28 },
  BOM: { id: 'BOM', name: 'Mumbai', x: 28, y: 62 },
  BLR: { id: 'BLR', name: 'Bengaluru', x: 40, y: 80 },
  CCU: { id: 'CCU', name: 'Kolkata', x: 78, y: 48 },
  MAA: { id: 'MAA', name: 'Chennai', x: 48, y: 84 },
  HYD: { id: 'HYD', name: 'Hyderabad', x: 44, y: 66 },
  PNQ: { id: 'PNQ', name: 'Pune', x: 31, y: 64 },
  AMD: { id: 'AMD', name: 'Ahmedabad', x: 26, y: 48 },
  GAU: { id: 'GAU', name: 'Guwahati', x: 86, y: 38 },
  GOI: { id: 'GOI', name: 'Goa', x: 29, y: 74 },
  PAT: { id: 'PAT', name: 'Patna', x: 65, y: 41 },
  IXR: { id: 'IXR', name: 'Ranchi', x: 67, y: 49 },
};

interface IndiaFlightMapProps {
  corridorBreakdown: Record<string, { avgFare: number; priceRelative: number; weight: number }>;
}

export const IndiaFlightMap: React.FC<IndiaFlightMapProps> = ({ corridorBreakdown }) => {
  const [hoveredRoute, setHoveredRoute] = useState<string | null>(null);
  const [selectedCity, setSelectedCity] = useState<string | null>(null);

  // Active route details for sidebar card
  const activeRouteData = hoveredRoute ? MOCK_ROUTE_WEIGHTS.find(r => r.corridorId === hoveredRoute) : null;
  const activeRouteStats = hoveredRoute ? corridorBreakdown[hoveredRoute] : null;

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6 relative overflow-hidden">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4">
        <div>
          <div className="flex items-center space-x-2">
            <h3 className="text-base font-bold text-white tracking-tight flex items-center">
              <Navigation className="w-5 h-5 text-sky-400 mr-2" />
              VayuSuchak (वायु सूचक) — Domestic Flight Network & Fare Heatmap
            </h3>
            <span className="px-2 py-0.5 text-[10px] font-mono bg-teal-500/20 text-teal-300 border border-teal-500/30 rounded">
              All 12 Corridors
            </span>
            {selectedCity && (
              <button
                onClick={() => setSelectedCity(null)}
                className="px-2 py-0.5 text-[10px] font-mono bg-sky-500/20 text-sky-300 border border-sky-500/30 rounded flex items-center gap-1 hover:bg-sky-500/30 transition-colors"
                title="Clear City Filter"
              >
                Filtered: {selectedCity} <RotateCcw className="w-2.5 h-2.5" />
              </button>
            )}
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Geographic corridor pricing dynamics and DGCA passenger volume arcs across India (Click any airport hub or route)
          </p>
        </div>

        <div className="flex items-center space-x-3 text-xs">
          <span className="flex items-center text-slate-300">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 mr-1.5 shadow-sm shadow-emerald-400/50"></span>
            Normal Fare (&lt;+5%)
          </span>
          <span className="flex items-center text-slate-300">
            <span className="w-2.5 h-2.5 rounded-full bg-amber-400 mr-1.5 shadow-sm shadow-amber-400/50"></span>
            Moderate (+5% to +10%)
          </span>
          <span className="flex items-center text-slate-300">
            <span className="w-2.5 h-2.5 rounded-full bg-rose-400 mr-1.5 shadow-sm shadow-rose-400/50"></span>
            High Surge (&gt;+10%)
          </span>
        </div>
      </div>

      {/* SVG Map Container */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-center">
        <div className="lg:col-span-2 relative bg-slate-950/90 rounded-xl border border-slate-800 p-4 h-[420px] flex items-center justify-center overflow-hidden">
          {/* SVG Canvas */}
          <svg className="w-full h-full select-none" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid meet">
            <defs>
              <linearGradient id="arcGradSky" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stopColor="#38bdf8" stopOpacity="0.8" />
                <stop offset="100%" stopColor="#818cf8" stopOpacity="0.3" />
              </linearGradient>
              <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur stdDeviation="1.2" result="coloredBlur"/>
                <feMerge>
                  <feMergeNode in="coloredBlur"/>
                  <feMergeNode in="SourceGraphic"/>
                </feMerge>
              </filter>
            </defs>

            {/* Stylized Geographical Silhouette Contour of India */}
            <path
              d="M 42 10 L 48 13 L 46 20 L 52 26 L 68 32 L 71 30 L 73 34 L 82 32 L 91 33 L 90 40 L 84 46 L 82 52 L 77 53 L 74 48 L 76 46 L 73 50 L 68 59 L 58 70 L 51 78 L 47 85 L 43 92 L 40 96 L 37 92 L 36 84 L 30 75 L 27 65 L 25 58 L 19 54 L 16 48 L 22 44 L 26 36 L 33 26 L 37 20 L 38 14 Z"
              fill="#0f172a"
              stroke="#334155"
              strokeWidth="0.8"
              strokeDasharray="2 2"
              opacity="0.6"
            />

            {/* Flight Arcs (All 12 Corridors) */}
            {MOCK_ROUTE_WEIGHTS.map(route => {
              const c1 = CITIES[route.origin];
              const c2 = CITIES[route.destination];
              if (!c1 || !c2) return null;

              // Connectivity check for selected hub filter
              const isConnected = !selectedCity || route.origin === selectedCity || route.destination === selectedCity;
              const isHovered = hoveredRoute === route.corridorId;

              const stats = corridorBreakdown[route.corridorId] || { avgFare: route.baseYearPrice, priceRelative: 1.0 };
              const pctChange = (stats.priceRelative - 1.0) * 100;

              // Heat color mapping
              const strokeColor = pctChange > 10 ? '#fb7185' : pctChange > 5 ? '#fbbf24' : '#34d399';

              // Adaptive smooth curvature based on distance
              const dx = c2.x - c1.x;
              const dy = c2.y - c1.y;
              const dist = Math.hypot(dx, dy) || 1;
              const perpX = -dy / dist;
              const perpY = dx / dist;
              const curveMagnitude = Math.min(7, Math.max(3, dist * 0.14));

              const midX = (c1.x + c2.x) / 2 + perpX * curveMagnitude;
              const midY = (c1.y + c2.y) / 2 + perpY * curveMagnitude - 3;

              const pathString = `M ${c1.x} ${c1.y} Q ${midX} ${midY} ${c2.x} ${c2.y}`;

              return (
                <g
                  key={route.corridorId}
                  onMouseEnter={() => setHoveredRoute(route.corridorId)}
                  onMouseLeave={() => setHoveredRoute(null)}
                  onClick={() => setHoveredRoute(prev => prev === route.corridorId ? null : route.corridorId)}
                  className="cursor-pointer"
                >
                  {/* Invisible wide stroke for easier mouse hovering */}
                  <path
                    d={pathString}
                    fill="none"
                    stroke="transparent"
                    strokeWidth="8"
                  />
                  {/* Visible Heat Arc */}
                  <path
                    d={pathString}
                    fill="none"
                    stroke={strokeColor}
                    strokeWidth={isHovered ? 2.6 : isConnected ? 1.4 : 0.6}
                    strokeDasharray={isHovered ? 'none' : route.tierCategory === 'UDAN_REGIONAL' ? '2 2' : '4 2'}
                    opacity={!isConnected ? 0.12 : isHovered ? 1.0 : 0.75}
                    className="transition-all duration-200"
                  />
                  {/* Animated pulse packet along the arc */}
                  {isConnected && (
                    <circle r={isHovered ? 2.4 : 1.4} fill="#ffffff" filter="url(#glow)">
                      <animateMotion
                        path={pathString}
                        dur={`${Math.max(2.5, 4.5 - (route.weightPercentage / 4))}s`}
                        repeatCount="indefinite"
                      />
                    </circle>
                  )}
                </g>
              );
            })}

            {/* City Hub Nodes (12 Airports) */}
            {Object.values(CITIES).map(city => {
              const isSelected = selectedCity === city.id;
              const hasConnectedHover = hoveredRoute && (
                MOCK_ROUTE_WEIGHTS.find(r => r.corridorId === hoveredRoute)?.origin === city.id ||
                MOCK_ROUTE_WEIGHTS.find(r => r.corridorId === hoveredRoute)?.destination === city.id
              );

              return (
                <g
                  key={city.id}
                  transform={`translate(${city.x}, ${city.y})`}
                  className="cursor-pointer group"
                  onClick={(e) => {
                    e.stopPropagation();
                    setSelectedCity(prev => prev === city.id ? null : city.id);
                  }}
                >
                  {/* Hub selection pulse indicator */}
                  {(isSelected || hasConnectedHover) && (
                    <circle r="6" fill="#38bdf8" className="animate-ping opacity-60" />
                  )}
                  <circle
                    r={isSelected ? "4.5" : "3.2"}
                    fill={isSelected ? "#38bdf8" : hasConnectedHover ? "#f59e0b" : "#0284c7"}
                    stroke="#0f172a"
                    strokeWidth="1.2"
                    className="transition-all"
                  />
                  <text
                    y="-5.5"
                    textAnchor="middle"
                    fill={isSelected ? "#38bdf8" : "#e2e8f0"}
                    fontSize="3.2"
                    fontWeight="bold"
                    className="font-mono tracking-wider group-hover:fill-sky-400 transition-colors pointer-events-none"
                  >
                    {city.id}
                  </text>
                </g>
              );
            })}
          </svg>

          {/* Hover / Selected Corridor Overlay Banner */}
          {hoveredRoute && (
            <div className="absolute bottom-3 left-3 right-3 bg-slate-900/95 backdrop-blur-md border border-slate-700/80 p-3 rounded-xl flex items-center justify-between text-xs animate-fadeIn shadow-xl shadow-black/40">
              <div className="flex items-center space-x-2">
                <Plane className="w-4 h-4 text-sky-400" />
                <span className="font-mono font-bold text-white">{hoveredRoute}</span>
                <span className="text-slate-400 hidden sm:inline">
                  ({MOCK_ROUTE_WEIGHTS.find(r => r.corridorId === hoveredRoute)?.corridorName})
                </span>
              </div>
              <div className="flex items-center space-x-4">
                <span className="text-slate-300">
                  Avg Fare: <strong className="text-white font-mono">₹{(corridorBreakdown[hoveredRoute]?.avgFare || 4800).toLocaleString()}</strong>
                </span>
                <span className="text-sky-400 font-bold font-mono">
                  Basket Wt: {MOCK_ROUTE_WEIGHTS.find(r => r.corridorId === hoveredRoute)?.weightPercentage}%
                </span>
              </div>
            </div>
          )}
        </div>

        {/* Corridor Side Stats & Dynamic Hub Overview */}
        <div className="space-y-3">
          {activeRouteData ? (
            <div className="p-4 bg-sky-950/30 rounded-xl border border-sky-800/60 shadow-lg">
              <div className="flex items-center justify-between mb-1">
                <div className="text-[10px] font-bold uppercase text-sky-400 tracking-wider">Active Corridor Inspect</div>
                <span className="px-2 py-0.5 text-[9px] font-mono bg-sky-500/20 text-sky-300 rounded border border-sky-500/30">
                  {activeRouteData.tierCategory.replace('_', ' ')}
                </span>
              </div>
              <div className="text-sm font-bold text-white">{activeRouteData.corridorName}</div>
              <div className="text-xs text-slate-300 mt-2 flex justify-between">
                <span>Baseline Fare (2025):</span>
                <strong className="text-slate-300 font-mono">₹{activeRouteData.baseYearPrice.toLocaleString()}</strong>
              </div>
              <div className="text-xs text-slate-300 mt-1 flex justify-between">
                <span>Current Scraped Avg (P̄_c):</span>
                <strong className="text-white font-mono font-bold">
                  ₹{(activeRouteStats?.avgFare || activeRouteData.baseYearPrice).toLocaleString()}
                </strong>
              </div>
              <div className="text-xs text-slate-300 mt-1 flex justify-between">
                <span>DGCA Normalized Weight:</span>
                <strong className="text-sky-400 font-mono font-bold">{activeRouteData.weightPercentage}%</strong>
              </div>
              <div className="text-xs text-slate-300 mt-1 flex justify-between">
                <span>Annual Passenger Volume:</span>
                <strong className="text-emerald-400 font-mono">{activeRouteData.annualPassengersMillions} Million</strong>
              </div>
            </div>
          ) : (
            <div className="p-4 bg-slate-900/90 rounded-xl border border-slate-800">
              <div className="text-[10px] font-bold uppercase text-slate-400 tracking-wider">Top Metro Hub Traffic</div>
              <div className="text-sm font-bold text-white mt-1">Delhi (DEL) ↔ Mumbai (BOM)</div>
              <div className="text-xs text-slate-300 mt-2 flex justify-between">
                <span>Annual Passenger Traffic:</span>
                <strong className="text-sky-400 font-mono">7.25 Million</strong>
              </div>
              <div className="text-xs text-slate-300 mt-1 flex justify-between">
                <span>National Basket Weight (w_c):</span>
                <strong className="text-emerald-400 font-mono">18.2% (14.8% raw)</strong>
              </div>
            </div>
          )}

          <div className="p-4 bg-slate-900/90 rounded-xl border border-slate-800">
            <div className="text-[10px] font-bold uppercase text-slate-400 tracking-wider">UDAN Regional Corridor Highlights</div>
            <div className="text-sm font-bold text-white mt-1">Delhi (DEL) ↔ Ranchi (IXR) & Mumbai ↔ Patna (PAT)</div>
            <div className="text-xs text-slate-300 mt-2 flex justify-between">
              <span>UDAN Subsidy Cap:</span>
              <strong className="text-amber-400 font-mono">₹2,500 Base</strong>
            </div>
            <div className="text-xs text-slate-300 mt-1 flex justify-between">
              <span>Monitored Current Avg:</span>
              <strong className="text-white font-mono">
                ₹{(corridorBreakdown['DEL-IXR']?.avgFare || 4200).toLocaleString()} (IXR) / ₹{(corridorBreakdown['BOM-PAT']?.avgFare || 5800).toLocaleString()} (PAT)
              </strong>
            </div>
            <div className="text-xs text-slate-300 mt-1 flex justify-between">
              <span>Regional Coverage:</span>
              <strong className="text-teal-400 font-mono">100% of Tier-2/3 UDAN Targets Active</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
