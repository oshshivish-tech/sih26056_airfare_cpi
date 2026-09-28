import React, { useState } from 'react';
import { X, Code2, Copy, Check, Download, ExternalLink, Terminal, Server, ShieldCheck } from 'lucide-react';

interface RestApiExplorerModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const RestApiExplorerModal: React.FC<RestApiExplorerModalProps> = ({ isOpen, onClose }) => {
  const [activeEndpoint, setActiveEndpoint] = useState<string>('current');
  const [copied, setCopied] = useState(false);

  if (!isOpen) return null;

  const endpoints: Record<string, {
    method: 'GET' | 'POST';
    path: string;
    title: string;
    description: string;
    targetUser: string;
    responseSample: object;
    curlSnippet: string;
    pythonSnippet: string;
  }> = {
    current: {
      method: 'GET',
      path: '/api/v1/apix/current?horizon=ALL',
      title: 'Current Real-Time APIx Index Point',
      description: 'Calculates real-time UN/ILO Jevons, Dutot, and DGCA Weighted Laspeyres index from active scraped flight quotes with IQR outlier filtering.',
      targetUser: 'MoSPI National Statistical Office (NSO) & RBI Monetary Policy Committee',
      responseSample: {
        index_code: "APIX-IND",
        base_period: "2024=100",
        calculation_timestamp: new Date().toISOString(),
        advance_purchase_window: "ALL",
        jevons_elementary_index: 109.19,
        dutot_index: 111.69,
        weighted_laspeyres_index: 110.04,
        headline_cpi_points: 109.19,
        sample_size: 1055,
        outliers_pruned: 34,
        status: "LIVE_DATABASE_AGGREGATED"
      },
      curlSnippet: `curl -X GET "https://sih26056-airfare-cpi.vercel.app/api/v1/apix/current?horizon=ALL" \\\n  -H "Accept: application/json"`,
      pythonSnippet: `import requests\n\nresp = requests.get("https://sih26056-airfare-cpi.vercel.app/api/v1/apix/current")\ndata = resp.json()\nprint(f"Current Jevons CPI: {data['jevons_elementary_index']}")`
    },
    daily: {
      method: 'GET',
      path: '/api/v1/apix/daily',
      title: '30-Day Daily Series & DGCA Back-Testing',
      description: 'Returns 30 days of back-tested daily indices with weekend surge elasticity, day-of-week breakdown, and variance vs DGCA benchmarks.',
      targetUser: 'Macroeconomic Forecasters & Econometricians',
      responseSample: {
        count: 31,
        benchmark_source: "DGCA Official Passenger Yield Statistics",
        base_year: "2024=100",
        series: [
          {
            date: "2026-09-22",
            day_label: "22 Sep (Tue)",
            daily_apix_jevons: 109.19,
            daily_apix_dutot: 111.69,
            daily_apix_laspeyres: 110.04,
            daily_avg_fare: 5296,
            dgca_official_benchmark: 5120.0,
            variance_pct: 3.44,
            scraped_quotes_count: 3650,
            is_weekend: false
          }
        ]
      },
      curlSnippet: `curl -X GET "https://sih26056-airfare-cpi.vercel.app/api/v1/apix/daily" \\\n  -H "Accept: application/json"`,
      pythonSnippet: `import requests\nimport pandas as pd\n\nresp = requests.get("https://sih26056-airfare-cpi.vercel.app/api/v1/apix/daily")\ndf = pd.DataFrame(resp.json()["series"])\nprint(df[["date", "daily_apix_jevons", "variance_pct"]].head())`
    },
    leadTime: {
      method: 'GET',
      path: '/api/v1/apix/lead-time',
      title: 'Advance-Purchase Elasticity Curve (T+1 to T+45)',
      description: 'Yield curves mapping fare surge and discount behavior across T+1 (immediate), T+7, T+15, T+30, and T+45 booking horizons.',
      targetUser: 'Aviation Pricing Analysts & Competition Commission of India (CCI)',
      responseSample: {
        source: "DATABASE_AGGREGATED",
        elasticity_curve: {
          "T+1": { avg_fare: 7644.39, quotes_count: 210, elasticity_multiplier: 1.576 },
          "T+7": { avg_fare: 5591.68, quotes_count: 214, elasticity_multiplier: 1.153 },
          "T+15": { avg_fare: 4930.09, quotes_count: 215, elasticity_multiplier: 1.017 },
          "T+30": { avg_fare: 4375.38, quotes_count: 221, elasticity_multiplier: 0.902 },
          "T+45": { avg_fare: 4105.89, quotes_count: 229, elasticity_multiplier: 0.847 }
        }
      },
      curlSnippet: `curl -X GET "https://sih26056-airfare-cpi.vercel.app/api/v1/apix/lead-time" \\\n  -H "Accept: application/json"`,
      pythonSnippet: `import requests\n\ncurve = requests.get("https://sih26056-airfare-cpi.vercel.app/api/v1/apix/lead-time").json()\nprint(curve["elasticity_curve"]["T+1"])`
    },
    corridors: {
      method: 'GET',
      path: '/api/v1/apix/corridors',
      title: '12 DGCA Representative Corridors Breakdown',
      description: 'Provides official DGCA passenger volume weights, base prices, current average fares, and corridor-level CPI relatives.',
      targetUser: 'Ministry of Civil Aviation (MoCA) & DGCA',
      responseSample: {
        total_corridors: 12,
        corridors: [
          {
            corridor_id: "DEL-BOM",
            corridor_name: "Delhi ↔ Mumbai",
            passenger_weight_pct: 14.8,
            base_year_price_inr: 4850,
            current_avg_fare_inr: 5420.0,
            corridor_cpi_relative: 111.75,
            market_tier: "METRO_METRO",
            sample_quotes: 180
          }
        ]
      },
      curlSnippet: `curl -X GET "https://sih26056-airfare-cpi.vercel.app/api/v1/apix/corridors" \\\n  -H "Accept: application/json"`,
      pythonSnippet: `import requests\n\ncorridors = requests.get("https://sih26056-airfare-cpi.vercel.app/api/v1/apix/corridors").json()\nfor c in corridors["corridors"]:\n    print(f"{c['corridor_id']}: weight {c['passenger_weight_pct']}%, CPI {c['corridor_cpi_relative']}")`
    },
    export: {
      method: 'GET',
      path: '/api/v1/apix/export/mospi?format=csv',
      title: 'MoSPI eSankhyiki Direct Ingestion Export',
      description: 'Official CSV/JSON pipeline format formatted with Item Code 1.1.07.03 for direct ingest into MoSPI National Accounts.',
      targetUser: 'MoSPI Data Dissemination Division & eSankhyiki Portal',
      responseSample: {
        metadata: {
          publisher: "National Statistical Office (NSO), MoSPI",
          sub_group: "Transport and Communication",
          item_name: "Airfare (Domestic Air Travel)",
          base_year: "2024=100",
          item_code: "1.1.07.03"
        },
        records_count: 31,
        download_available: true
      },
      curlSnippet: `curl -X GET "https://sih26056-airfare-cpi.vercel.app/api/v1/apix/export/mospi?format=csv" \\\n  -o APIx_MoSPI_eSankhyiki.csv`,
      pythonSnippet: `import requests\n\nwith open("APIx_MoSPI.csv", "wb") as f:\n    f.write(requests.get("https://sih26056-airfare-cpi.vercel.app/api/v1/apix/export/mospi?format=csv").content)`
    }
  };

  const current = endpoints[activeEndpoint];

  const handleCopy = (text: string) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const downloadCsvSample = () => {
    const csvContent = "data:text/csv;charset=utf-8," + 
      "Reference_Date,Item_Code,Item_Description,Classification,Jevons_Elementary_Index,Dutot_Index,DGCA_Laspeyres_Index,Average_Fare_INR,DGCA_Benchmark_INR,Base_Year\n" +
      "2026-09-22,1.1.07.03,Passenger Transport by Air - Domestic,Transport and Communication,109.19,111.69,110.04,5296,5120,2024=100\n" +
      "2026-09-21,1.1.07.03,Passenger Transport by Air - Domestic,Transport and Communication,108.85,111.10,109.60,5260,5120,2024=100\n" +
      "2026-09-20,1.1.07.03,Passenger Transport by Air - Domestic,Transport and Communication,112.40,114.80,113.10,5450,5120,2024=100\n";
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `APIx_MoSPI_eSankhyiki_Sample.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-fadeIn">
      <div className="glass-panel w-full max-w-5xl rounded-2xl border border-slate-700 bg-slate-900/95 shadow-2xl flex flex-col max-h-[90vh] overflow-hidden">
        {/* Header */}
        <div className="flex items-center justify-between p-5 border-b border-slate-800 bg-slate-950/60">
          <div className="flex items-center space-x-3">
            <div className="p-2.5 rounded-xl bg-purple-500/10 text-purple-400 border border-purple-500/20">
              <Server className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-bold text-white">
                  MoSPI NSO & RBI Open REST API Explorer
                </h2>
                <span className="px-2 py-0.5 text-[10px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 rounded-full flex items-center gap-1">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  OPERATIONAL
                </span>
              </div>
              <p className="text-xs text-slate-400">
                Official SIH 26056 Pillar (d) REST Service for automated MoSPI CPI augmentation and RBI MPC policy models
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-all"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-5 grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Left Column: Endpoints List */}
          <div className="lg:col-span-4 space-y-2">
            <h4 className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Available Endpoints</h4>
            {Object.entries(endpoints).map(([key, ep]) => {
              const isSelected = activeEndpoint === key;
              return (
                <div
                  key={key}
                  onClick={() => setActiveEndpoint(key)}
                  className={`p-3 rounded-xl border transition-all cursor-pointer ${
                    isSelected
                      ? 'bg-purple-600/15 border-purple-500 text-white shadow-sm'
                      : 'bg-slate-800/50 border-slate-700/60 text-slate-300 hover:bg-slate-800 hover:border-slate-600'
                  }`}
                >
                  <div className="flex items-center space-x-2 mb-1">
                    <span className="px-1.5 py-0.5 text-[10px] font-mono font-bold bg-sky-500/20 text-sky-300 rounded">
                      {ep.method}
                    </span>
                    <span className="text-xs font-mono font-semibold truncate">{ep.path.split('?')[0]}</span>
                  </div>
                  <div className="text-xs font-medium text-slate-200">{ep.title}</div>
                  <div className="text-[11px] text-slate-400 truncate mt-0.5">{ep.targetUser}</div>
                </div>
              );
            })}

            <div className="p-3 rounded-xl bg-slate-950/70 border border-slate-800 text-[11px] text-slate-400 space-y-1 mt-4">
              <div className="flex items-center space-x-1.5 text-emerald-400 font-semibold">
                <ShieldCheck className="w-3.5 h-3.5" />
                <span>eSankhyiki Ready</span>
              </div>
              <p>
                Endpoints follow UN/ILO CPI 2020 handbook standards and generate compliant JSON/CSV formats for instant NSO ingestion.
              </p>
            </div>
          </div>

          {/* Right Column: Endpoint Details & Response Playground */}
          <div className="lg:col-span-8 space-y-4">
            <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800">
              <div className="flex items-center justify-between mb-2">
                <span className="text-sm font-bold text-white flex items-center gap-2">
                  <span className="px-2 py-0.5 text-xs font-mono font-bold bg-sky-500/20 text-sky-300 rounded">
                    {current.method}
                  </span>
                  <code className="text-xs font-mono text-purple-300">{current.path}</code>
                </span>
                {activeEndpoint === 'export' && (
                  <button
                    onClick={downloadCsvSample}
                    className="flex items-center space-x-1 px-2.5 py-1 rounded-lg text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition-all shadow-sm"
                  >
                    <Download className="w-3 h-3" />
                    <span>Download MoSPI CSV</span>
                  </button>
                )}
              </div>
              <p className="text-xs text-slate-300 mb-1">{current.description}</p>
              <div className="text-[11px] text-slate-400 font-mono">
                Intended for: <strong className="text-slate-200">{current.targetUser}</strong>
              </div>
            </div>

            {/* Code / cURL Snippet */}
            <div>
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-xs font-bold text-slate-400 flex items-center gap-1.5">
                  <Terminal className="w-3.5 h-3.5 text-sky-400" />
                  Request Snippet (cURL)
                </span>
                <button
                  onClick={() => handleCopy(current.curlSnippet)}
                  className="flex items-center space-x-1 text-[11px] text-slate-400 hover:text-white transition-colors"
                >
                  {copied ? <Check className="w-3 h-3 text-emerald-400" /> : <Copy className="w-3 h-3" />}
                  <span>{copied ? 'Copied' : 'Copy'}</span>
                </button>
              </div>
              <pre className="p-3 rounded-xl bg-slate-950 border border-slate-800 font-mono text-xs text-slate-300 overflow-x-auto whitespace-pre">
                {current.curlSnippet}
              </pre>
            </div>

            {/* Live Response Payload */}
            <div>
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-xs font-bold text-slate-400 flex items-center gap-1.5">
                  <Code2 className="w-3.5 h-3.5 text-emerald-400" />
                  Live API Response Payload (200 OK)
                </span>
                <span className="text-[10px] font-mono text-slate-500">application/json</span>
              </div>
              <pre className="p-3.5 rounded-xl bg-slate-950 border border-slate-800 font-mono text-xs text-emerald-300/90 max-h-[220px] overflow-y-auto leading-relaxed">
                {JSON.stringify(current.responseSample, null, 2)}
              </pre>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-slate-800 bg-slate-950/60 flex items-center justify-between">
          <span className="text-xs text-slate-400">
            FastAPI Backend Service running at <code className="text-sky-300">backend/api_server.py</code>
          </span>
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-xl text-xs font-semibold text-white bg-slate-800 hover:bg-slate-700 transition-all"
          >
            Close Explorer
          </button>
        </div>
      </div>
    </div>
  );
};
