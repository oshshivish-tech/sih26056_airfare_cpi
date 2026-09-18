import React from 'react';
import { ShieldCheck, BookOpen, Calculator, Scale, Server } from 'lucide-react';

export const MethodologyDoc: React.FC = () => {
  return (
    <div className="space-y-6 mb-6">
      {/* Header Banner */}
      <div className="glass-panel p-6 rounded-2xl">
        <div className="flex items-center space-x-3 mb-2">
          <div className="p-2 rounded-xl bg-purple-500/10 text-purple-400 border border-purple-500/30">
            <BookOpen className="w-6 h-6" />
          </div>
          <div>
            <h2 className="text-lg font-bold text-white tracking-tight">
              Statistical Methodology & SIH Compliance Architecture
            </h2>
            <p className="text-xs text-slate-400">
              Conforming strictly to the UN / ILO Consumer Price Index (CPI) Manual Guidelines
            </p>
          </div>
        </div>
      </div>

      {/* Grid Section */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Card 1: Jevons Index Formula */}
        <div className="glass-panel p-6 rounded-2xl space-y-3">
          <div className="flex items-center space-x-2 text-sky-400 font-bold text-sm">
            <Calculator className="w-4 h-4" />
            <span>1. Jevons Geometric Mean Index (Elementary Aggregate)</span>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            The UN ILO Manual explicitly recommends the <strong>Jevons Index</strong> when elementary weights are unavailable at the micro-item quote level. It satisfies both the <em>Time Reversal Test</em> and <em>Transitivity Test</em>.
          </p>
          <div className="p-4 bg-slate-950/90 rounded-xl border border-slate-800 font-mono text-xs text-sky-300 text-center">
            {"I_Jevons = exp( (1/N) * ∑ ln(P_i,t / P_i,0) ) * 100"}
          </div>
          <p className="text-[11px] text-slate-400 italic">
            Protects the MoSPI Consumer Price Index from upward substitution bias caused by dynamic airline surge pricing.
          </p>
        </div>

        {/* Card 2: DGCA Route Weighting */}
        <div className="glass-panel p-6 rounded-2xl space-y-3">
          <div className="flex items-center space-x-2 text-emerald-400 font-bold text-sm">
            <Scale className="w-4 h-4" />
            <span>2. DGCA Passenger Traffic Weighting Matrix</span>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            Corridor indices are aggregated into the higher-level Airfare Sub-Index using official passenger traffic data published by the <strong>Directorate General of Civil Aviation (DGCA)</strong>.
          </p>
          <div className="p-4 bg-slate-950/90 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 text-center">
            {"I_Weighted = ∑ (w_c * I_c,t) where ∑ w_c = 1.0"}
          </div>
          <p className="text-[11px] text-slate-400 italic">
            High-density routes like Delhi-Mumbai (14.8% weight) appropriately impact the national airfare index compared to regional routes.
          </p>
        </div>

        {/* Card 3: Anti-Bot & Ethics */}
        <div className="glass-panel p-6 rounded-2xl space-y-3">
          <div className="flex items-center space-x-2 text-amber-400 font-bold text-sm">
            <Server className="w-4 h-4" />
            <span>3. Anti-Bot Stealth & Ethical Compliance</span>
          </div>
          <ul className="space-y-2 text-xs text-slate-300 list-disc list-inside">
            <li><strong>TLS Fingerprint Masking:</strong> Playwright Chromium patches to mimic browser headers.</li>
            <li><strong>API Payload Interception:</strong> Bypassing HTML DOM scraping by extracting raw XHR JSON responses.</li>
            <li><strong>Polite Scraping Policy:</strong> Configurable interval rates (off-peak night scraping) ensuring 0% server disruption to target airlines.</li>
          </ul>
        </div>

        {/* Card 4: Data Normalization */}
        <div className="glass-panel p-6 rounded-2xl space-y-3">
          <div className="flex items-center space-x-2 text-purple-400 font-bold text-sm">
            <ShieldCheck className="w-4 h-4" />
            <span>4. Fixed Lead-Time & Fare Disaggregation</span>
          </div>
          <ul className="space-y-2 text-xs text-slate-300 list-disc list-inside">
            <li><strong>Lead-Time Windows:</strong> Fixed tracking across 1-day, 7-day, 15-day, 30-day, and 45-day booking horizons.</li>
            <li><strong>Tax Decomposition:</strong> Separates base fares from fuel surcharges, UDF (User Development Fees), and 5% GST.</li>
            <li><strong>IQR Anomaly Filter:</strong> Automatically prunes dynamic scalping anomalies (Q3 + 2.0 × IQR).</li>
          </ul>
        </div>
      </div>

      {/* Official MoSPI eSankhyiki Integration Banner */}
      <div className="glass-panel p-6 rounded-2xl border border-purple-500/40 bg-purple-950/20 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-purple-300 font-bold text-sm">
            <BookOpen className="w-4 h-4" />
            <span>5. Official Benchmark Source: MoSPI eSankhyiki Portal</span>
          </div>
          <p className="text-xs text-slate-300 mt-1 max-w-3xl leading-relaxed">
            Our historical baseline series and macro weights are calibrated against the official <strong>Consumer Price Index (CPI Base = 100)</strong> published on the Government of India's statistical data platform <strong>eSankhyiki (<code className="text-purple-300">esankhyiki.mospi.gov.in</code>)</strong>. Our automated web scraping pipeline directly addresses the SIH 26056 mandate by eliminating eSankhyiki's traditional 30-day manual survey lag with daily, automated quote ingestion.
          </p>
        </div>
        <a
          href="https://esankhyiki.mospi.gov.in/"
          target="_blank"
          rel="noopener noreferrer"
          className="shrink-0 px-4 py-2 rounded-xl bg-purple-600/30 hover:bg-purple-600/50 text-purple-200 border border-purple-500/50 text-xs font-semibold font-mono transition-all"
        >
          Visit eSankhyiki Portal ↗
        </a>
      </div>
    </div>
  );
};
