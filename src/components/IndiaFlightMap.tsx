import React, { useState } from 'react';
import { Plane, Navigation, Info } from 'lucide-react';
import { MOCK_ROUTE_WEIGHTS } from '../data/mockData';

interface CityNode {
  id: string;
  name: string;
  x: number; // SVG percentage x
  y: number; // SVG percentage y
}

const CITIES: Record<string, CityNode> = {
  DEL: { id: 'DEL', name: 'Delhi', x: 42, y: 30 },
  BOM: { id: 'BOM', name: 'Mumbai', x: 28, y: 62 },
  BLR: { id: 'BLR', name: 'Bengaluru', x: 40, y: 80 },
  CCU: { id: 'CCU', name: 'Kolkata', x: 78, y: 48 },
  MAA: { id: 'MAA', name: 'Chennai', x: 48, y: 84 },
  HYD: { id: 'HYD', name: 'Hyderabad', x: 44, y: 66 },
  PNQ: { id: 'PNQ', name: 'Pune', x: 31, y: 64 },
  AMD: { id: 'AMD', name: 'Ahmedabad', x: 26, y: 48 },
  GAU: { id: 'GAU', name: 'Guwahati', x: 86, y: 38 },
  GOI: { id: 'GOI', name: 'Goa', x: 29, y: 74 },
};

interface IndiaFlightMapProps {
  corridorBreakdown: Record<string, { avgFare: number; priceRelative: number; weight: number }>;
}

export const IndiaFlightMap: React.FC<IndiaFlightMapProps> = ({ corridorBreakdown }) => {
  const [hoveredRoute, setHoveredRoute] = useState<string | null>(null);
  const [selectedCity, setSelectedCity] = useState<string | null>(null);

  return (
    <div className="glass-panel p-6 rounded-2xl mb-6 relative overflow-hidden">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4">
        <div>
          <div className="flex items-center space-x-2">
            <h3 className="text-base font-bold text-white tracking-tight flex items-center">
              <Navigation className="w-5 h-5 text-sky-400 mr-2" />
              AirIntel India — Domestic Flight Network & Fare Heatmap
            </h3>
            <span className="px-2 py-0.5 text-[10px] font-mono bg-teal-500/20 text-teal-300 border border-teal-500/30 rounded">
              50 Corridors
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Geographic corridor pricing dynamics and DGCA passenger volume arcs across India
          </p>
        </div>

        <div className="flex items-center space-x-3 text-xs">
          <span className="flex items-center text-slate-300">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 mr-1.5"></span>
            Normal Fare (&lt;+5%)
          </span>
          <span className="flex items-center text-slate-300">
            <span className="w-2.5 h-2.5 rounded-full bg-amber-400 mr-1.5"></span>
            Moderate (+5% to +10%)
          </span>
          <span className="flex items-center text-slate-300">
            <span className="w-2.5 h-2.5 rounded-full bg-rose-400 mr-1.5"></span>
            High Surge (&gt;+10%)
          </span>
        </div>
      </div>

      {/* SVG Map Container */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-center">
        <div className="lg:col-span-2 relative bg-slate-950/80 rounded-xl border border-slate-800 p-4 h-[380px] flex items-center justify-center overflow-hidden">
          {/* Subtle India Contour Graphic Background */}
          <svg className="w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid meet">
            <defs>
              <linearGradient id="arcGradSky" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stopColor="#38bdf8" stopOpacity="0.8" />
                <stop offset="100%" stopColor="#818cf8" stopOpacity="0.3" />
              </linearGradient>
              <filter id="glow">
                <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
                <feMerge>
                  <feMergeNode in="coloredBlur"/>
                  <feMergeNode in="SourceGraphic"/>
                </feMerge>
              </filter>
            </defs>

            {/* Flight Arcs */}
            {MOCK_ROUTE_WEIGHTS.slice(0, 8).map(route => {
              const c1 = CITIES[route.origin];
              const c2 = CITIES[route.destination];
              if (!c1 || !c2) return null;

              const isHovered = hoveredRoute === route.corridorId;
              const stats = corridorBreakdown[route.corridorId] || { avgFare: route.baseYearPrice, priceRelative: 1.0 };
              const pctChange = (stats.priceRelative - 1.0) * 100;

              const strokeColor = pctChange > 10 ? '#fb7185' : pctChange > 5 ? '#fbbf24' : '#34d399';

              // Calculate curve control point
              const midX = (c1.x + c2.x) / 2;
              const midY = (c1.y + c2.y) / 2 - 12;

              return (
                <g key={route.corridorId} onMouseEnter={() => setHoveredRoute(route.corridorId)} onMouseLeave={() => setHoveredRoute(null)}>
                  <path
                    d={`M ${c1.x} ${c1.y} Q ${midX} ${midY} ${c2.x} ${c2.y}`}
                    fill="none"
                    stroke={strokeColor}
                    strokeWidth={isHovered ? 2.5 : 1.2}
                    strokeDasharray={isHovered ? 'none' : '4 2'}
                    opacity={isHovered ? 1.0 : 0.6}
                    className="transition-all cursor-pointer"
                  />
                  {/* Moving pulse along arc */}
                  <circle r={isHovered ? 2.5 : 1.5} fill="#ffffff" filter="url(#glow)">
                    <animateMotion path={`M ${c1.x} ${c1.y} Q ${midX} ${midY} ${c2.x} ${c2.y}`} dur={`${4 - (route.weightPercentage / 5)}s`} repeatCount="indefinite" />
                  </circle>
                </g>
              );
            })}

            {/* City Hub Nodes */}
            {Object.values(CITIES).map(city => {
              const isSelected = selectedCity === city.id;

              return (
                <g
                  key={city.id}
                  transform={`translate(${city.x}, ${city.y})`}
                  className="cursor-pointer group"
                  onClick={() => setSelectedCity(city.id)}
                >
                  <circle r="4" fill="#0284c7" className="animate-ping opacity-40" />
                  <circle r="3.5" fill="#38bdf8" stroke="#0f172a" strokeWidth="1" />
                  <text
                    y="-6"
                    textAnchor="middle"
                    fill="#e2e8f0"
                    fontSize="3.2"
                    fontWeight="bold"
                    className="font-mono tracking-wider group-hover:fill-sky-400 transition-colors"
                  >
                    {city.id}
                  </text>
                </g>
              );
            })}
          </svg>

          {/* Hover / Selected Corridor Overlay Banner */}
          {hoveredRoute && (
            <div className="absolute bottom-4 left-4 right-4 bg-slate-900/90 backdrop-blur border border-slate-700 p-3 rounded-xl flex items-center justify-between text-xs animate-fadeIn">
              <div className="flex items-center space-x-2">
                <Plane className="w-4 h-4 text-sky-400" />
                <span className="font-mono font-bold text-white">{hoveredRoute}</span>
                <span className="text-slate-400">({MOCK_ROUTE_WEIGHTS.find(r => r.corridorId === hoveredRoute)?.corridorName})</span>
              </div>
              <div className="flex items-center space-x-4">
                <span className="text-slate-300">Avg Fare: <strong className="text-white font-mono">₹{corridorBreakdown[hoveredRoute]?.avgFare || 4800}</strong></span>
                <span className="text-sky-400 font-bold font-mono">DGCA Weight: {MOCK_ROUTE_WEIGHTS.find(r => r.corridorId === hoveredRoute)?.weightPercentage}%</span>
              </div>
            </div>
          )}
        </div>

        {/* Corridor Side Stats */}
        <div className="space-y-3">
          <div className="p-4 bg-slate-900/90 rounded-xl border border-slate-800">
            <div className="text-[10px] font-bold uppercase text-slate-400 tracking-wider">Top Metro Hub Traffic</div>
            <div className="text-sm font-bold text-white mt-1">Delhi (DEL) ↔ Mumbai (BOM)</div>
            <div className="text-xs text-slate-300 mt-2 flex justify-between">
              <span>Annual Passenger Traffic:</span>
              <strong className="text-sky-400 font-mono">7.25 Million</strong>
            </div>
            <div className="text-xs text-slate-300 mt-1 flex justify-between">
              <span>National CPI Weight Share:</span>
              <strong className="text-emerald-400 font-mono">14.8%</strong>
            </div>
          </div>

          <div className="p-4 bg-slate-900/90 rounded-xl border border-slate-800">
            <div className="text-[10px] font-bold uppercase text-slate-400 tracking-wider">UDAN Regional Corridor Highlight</div>
            <div className="text-sm font-bold text-white mt-1">Delhi (DEL) ↔ Ranchi (IXR)</div>
            <div className="text-xs text-slate-300 mt-2 flex justify-between">
              <span>UDAN Subsidy Cap:</span>
              <strong className="text-amber-400 font-mono">₹2,500 Base</strong>
            </div>
            <div className="text-xs text-slate-300 mt-1 flex justify-between">
              <span>Monitored Average Fare:</span>
              <strong className="text-white font-mono">₹4,200</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
