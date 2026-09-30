import React from 'react';
import { ShieldCheck, BookOpen, Calculator, Scale, Server, AlertCircle, FileText, CheckCircle2 } from 'lucide-react';
import { REPRESENTATIVE_CORRIDORS, BOOKING_HORIZONS, DATA_METADATA } from '../config/constants';

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
              Statistical Methodology & Regulatory Compliance Framework
            </h2>
            <p className="text-xs text-slate-400">
              Conforming strictly to the UN / ILO Consumer Price Index (CPI) Manual Chapter 10 (Elementary Indices) & MoSPI NSO Standards
            </p>
          </div>
        </div>
      </div>

      {/* Grid Section */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Card 1: Elementary Aggregate & Jevons Formula */}
        <div className="glass-panel p-6 rounded-2xl space-y-3">
          <div className="flex items-center space-x-2 text-sky-400 font-bold text-sm">
            <Calculator className="w-4 h-4" />
            <span>1. Elementary Aggregate Definition & Jevons Formula</span>
          </div>
          <div className="p-3 bg-sky-950/40 rounded-xl border border-sky-800/50 text-xs text-sky-200">
            <strong>Elementary Aggregate Definition:</strong> A strictly defined homogeneous flight cell defined as:
            <code className="block mt-1 p-1.5 bg-slate-950/80 rounded font-mono text-[11px] text-sky-300">
              Elementary Aggregate = same route + same booking-horizon bucket + same cabin + non-stop flight
            </code>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            Per the <strong>UN/ILO CPI Manual (2020) Chapter 10</strong> and <strong>Diewert (2004)</strong>, the <strong>Jevons Geometric Mean Index</strong> is the internationally recommended formula when micro-expenditure weights are unavailable at the elementary quote level:
          </p>
          <div className="p-4 bg-slate-950/90 rounded-xl border border-slate-800 font-mono text-xs text-sky-300 text-center">
            {"I_Jevons(0:t) = ∏ (P_i,t / P_i,0)^(1/N) * 100 = exp( (1/N) * ∑ ln(P_i,t / P_i,0) ) * 100"}
          </div>
          <ul className="space-y-1 text-[11px] text-slate-300 list-disc list-inside">
            <li><strong>Axiomatic Superiority:</strong> Satisfies the <em>Time-Reversal Test</em> ({'I(0:t) × I(t:0) = 1'}) and <em>Transitivity Test</em>.</li>
            <li><strong>Upward Bias Immunity:</strong> Protects the index from the significant upward substitution bias inherent in arithmetic averaging (Dutot index) during dynamic airline fare spikes.</li>
          </ul>
        </div>

        {/* Card 2: DGCA Weighting & Harmonization */}
        <div className="glass-panel p-6 rounded-2xl space-y-3">
          <div className="flex items-center space-x-2 text-emerald-400 font-bold text-sm">
            <Scale className="w-4 h-4" />
            <span>2. DGCA Route Weighting & Harmonized Normalization</span>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            Corridor indices are aggregated into the higher-level Airfare Sub-Index using official scheduled domestic passenger volumes from the <strong>Directorate General of Civil Aviation (DGCA)</strong>.
          </p>
          <div className="p-4 bg-slate-950/90 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 text-center">
            {"I_Weighted(t) = ∑ (w_c * I_c,t) where ∑_{c=1}^{12} w_c = 1.000 (100.0%)"}
          </div>
          <div className="p-3 bg-emerald-950/40 rounded-xl border border-emerald-800/50 text-[11px] text-emerald-200 space-y-1">
            <div className="font-semibold text-emerald-300">Basket Weight Normalization Rule:</div>
            <div>• The 12 representative corridors account for <strong>81.4%</strong> of national domestic passenger volume.</div>
            <div>• <strong>Delhi–Mumbai:</strong> Raw DGCA share = 14.8% → Normalized basket weight <strong>w_c = 18.2%</strong> (14.8 / 81.4).</div>
            <div>• <strong>Bengaluru–Delhi:</strong> Raw DGCA share = 11.0% → Normalized basket weight <strong>w_c = 13.5%</strong> (11.0 / 81.4).</div>
            <div className="text-slate-400 text-[10px] mt-1 italic">Source: {DATA_METADATA.dgcaReportCitation}</div>
          </div>
        </div>

        {/* Card 3: Data Access, Robots.txt & Compliance */}
        <div className="glass-panel p-6 rounded-2xl space-y-3">
          <div className="flex items-center space-x-2 text-amber-400 font-bold text-sm">
            <Server className="w-4 h-4" />
            <span>3. Data Access & Legal/Ethical Compliance</span>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            VayuSuchak operates under strict ethical public data collection principles and maintains a transparent compliance charter:
          </p>
          <ul className="space-y-1.5 text-xs text-slate-300 list-disc list-inside">
            <li><strong>Robots.txt & Terms Adherence:</strong> Respects crawl-delay directives and restricted paths on airline public portals.</li>
            <li><strong>Rate-Limited Polite Queries:</strong> Conservative request throttling (3–5s delays, off-peak night execution) with zero target server burden.</li>
            <li><strong>Descriptive User-Agent:</strong> Identifies as <code className="text-amber-300 font-mono text-[10px]">VayuSuchak-Research-Bot/1.0 (+https://sih26056-airfare-cpi.vercel.app)</code> with university contact details.</li>
            <li><strong>Official Feed Roadmap:</strong> Prototype web collection transitions to official airline NDC / API feeds and MoCA/DGCA institutional data-sharing MoUs in production.</li>
          </ul>
        </div>

        {/* Card 4: Base Period, Horizons & Outlier Rules */}
        <div className="glass-panel p-6 rounded-2xl space-y-3">
          <div className="flex items-center space-x-2 text-purple-400 font-bold text-sm">
            <ShieldCheck className="w-4 h-4" />
            <span>4. Base Period, Horizons & Quality Assurance</span>
          </div>
          <ul className="space-y-2 text-xs text-slate-300">
            <li>
              <strong>Base Period:</strong> <code className="text-purple-300 font-mono">{DATA_METADATA.basePeriod}</code>. New airline carriers and routes enter the index basket via standard <em>chain-linking</em> during annual January rebase cycles.
            </li>
            <li>
              <strong>5 Advance Horizons:</strong> Tracks dynamic airline yield management curves at strictly standardized horizons:
              <span className="block font-mono text-[11px] text-purple-300 mt-1">
                T+1 (15%), T+7 (30%), T+14 (35%), T+30 (15%), T+45 (5%)
              </span>
            </li>
            <li>
              <strong>Dynamic IQR Outlier Filter:</strong> Non-parametric outlier boundaries:
              <code className="block mt-1 font-mono text-[11px] text-purple-300">
                Lower = Q1 - 1.5 × IQR, Upper = Q3 + 1.5 × IQR
              </code>
              Prunes algorithmic scalping spikes and erroneous null quotes while preserving genuine market surges.
            </li>
            <li>
              <strong>Fare Disaggregation:</strong> Isolates base fare from fuel surcharges, airport development fees (UDF/PSF), and statutory taxes (GST).
            </li>
          </ul>
        </div>
      </div>

      {/* Corridor Weights Table */}
      <div className="glass-panel p-6 rounded-2xl">
        <h3 className="text-sm font-bold text-white mb-3 flex items-center gap-2">
          <FileText className="w-4 h-4 text-sky-400" />
          <span>Representative Basket Corridors & Weighting Schedule (DGCA Benchmarked)</span>
        </h3>
        <div className="overflow-x-auto">
          <table className="w-full text-xs text-left">
            <thead className="bg-slate-900/80 text-slate-400 font-semibold border-b border-slate-800">
              <tr>
                <th className="py-2.5 px-3">Corridor</th>
                <th className="py-2.5 px-3">Category</th>
                <th className="py-2.5 px-3">Pax (M/yr)</th>
                <th className="py-2.5 px-3">Raw DGCA Share</th>
                <th className="py-2.5 px-3">Normalized Basket Weight (w_c)</th>
                <th className="py-2.5 px-3">Base Price (INR)</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 text-slate-300">
              {REPRESENTATIVE_CORRIDORS.map(c => (
                <tr key={c.corridorId} className="hover:bg-slate-900/40">
                  <td className="py-2 px-3 font-medium text-white">{c.corridorName}</td>
                  <td className="py-2 px-3">
                    <span className={`px-2 py-0.5 rounded text-[10px] font-mono ${
                      c.tierCategory === 'METRO_METRO' ? 'bg-sky-500/20 text-sky-300' :
                      c.tierCategory === 'METRO_TIER2' ? 'bg-indigo-500/20 text-indigo-300' :
                      'bg-purple-500/20 text-purple-300'
                    }`}>
                      {c.tierCategory}
                    </span>
                  </td>
                  <td className="py-2 px-3 font-mono">{c.annualPassengersMillions.toFixed(2)}</td>
                  <td className="py-2 px-3 font-mono text-slate-400">{c.rawDgcaSharePercentage.toFixed(1)}%</td>
                  <td className="py-2 px-3 font-mono font-bold text-emerald-400">{c.normalizedPercentage.toFixed(1)}%</td>
                  <td className="py-2 px-3 font-mono">₹{c.baseYearPrice.toLocaleString()}</td>
                </tr>
              ))}
              <tr className="bg-slate-900/90 font-bold text-white border-t border-slate-700">
                <td className="py-2 px-3" colSpan={3}>Total Representative Basket Coverage</td>
                <td className="py-2 px-3 font-mono text-slate-300">81.4% (National Domestic)</td>
                <td className="py-2 px-3 font-mono text-emerald-300">100.0% (Basket Sum)</td>
                <td className="py-2 px-3 font-mono">—</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* Limitations & Mitigations */}
      <div className="glass-panel p-6 rounded-2xl">
        <h3 className="text-sm font-bold text-white mb-3 flex items-center gap-2">
          <AlertCircle className="w-4 h-4 text-amber-400" />
          <span>Operational Risks, Limitations & Mitigation Strategies</span>
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
          <div className="p-3 bg-slate-950/60 rounded-xl border border-slate-800 space-y-1">
            <div className="font-semibold text-rose-300">Risk 1: Portal Layout / Schema Changes</div>
            <div className="text-slate-400"><strong>Mitigation:</strong> Modular parser architecture with automated unit-test breakage monitors and fallback DOM extractors.</div>
          </div>
          <div className="p-3 bg-slate-950/60 rounded-xl border border-slate-800 space-y-1">
            <div className="font-semibold text-rose-300">Risk 2: Rate Limiting & Access Throttling</div>
            <div className="text-slate-400"><strong>Mitigation:</strong> Conservative request throttling, randomized polite jitter, and planned migration to official airline NDC / API feeds.</div>
          </div>
          <div className="p-3 bg-slate-950/60 rounded-xl border border-slate-800 space-y-1">
            <div className="font-semibold text-rose-300">Risk 3: Dynamic Outliers & Missing Flight Quotes</div>
            <div className="text-slate-400"><strong>Mitigation:</strong> Non-parametric IQR trimming, automated stale quote purges, and last-valid-quote imputation under strict CPI rules.</div>
          </div>
          <div className="p-3 bg-slate-950/60 rounded-xl border border-slate-800 space-y-1">
            <div className="font-semibold text-rose-300">Risk 4: Geographic Expansion Scalability</div>
            <div className="text-slate-400"><strong>Mitigation:</strong> Phased rollout from 12 pilot corridors to top 50 routes, expanding to regional UDAN connectivity via DGCA volume tiers.</div>
          </div>
        </div>
      </div>

      {/* MoSPI eSankhyiki Integration Banner */}
      <div className="glass-panel p-6 rounded-2xl border border-purple-500/40 bg-purple-950/20 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-purple-300 font-bold text-sm">
            <CheckCircle2 className="w-4 h-4" />
            <span>Official Benchmark Source: MoSPI eSankhyiki Portal</span>
          </div>
          <p className="text-xs text-slate-300 mt-1 max-w-3xl leading-relaxed">
            Our historical baseline series and macro weights are calibrated against the official <strong>Consumer Price Index (CPI Base = 100)</strong> published on the Government of India statistical data platform <strong>eSankhyiki (<code className="text-purple-300">esankhyiki.mospi.gov.in</code>)</strong>. VayuSuchak directly addresses the SIH 26056 mandate by cutting traditional 30-day manual surveyor collection lag down to automated daily updates under 24 hours.
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
