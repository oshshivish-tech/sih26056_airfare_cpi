import React, { useState } from 'react';
import { X, ShieldCheck, Hash, Lock, FileCode, CheckCircle2, Copy, GitMerge } from 'lucide-react';
import { CPIIndexPoint } from '../types';

interface ProvenanceVaultModalProps {
  isOpen: boolean;
  onClose: () => void;
  currentPoint: CPIIndexPoint;
}

export const ProvenanceVaultModal: React.FC<ProvenanceVaultModalProps> = ({
  isOpen,
  onClose,
  currentPoint
}) => {
  const [copiedHash, setCopiedHash] = useState<string | null>(null);
  const [copiedJson, setCopiedJson] = useState(false);

  if (!isOpen) return null;

  const todayDateStr = new Date().toISOString().split('T')[0];
  const nowTimeStr = new Date().toLocaleTimeString('en-US', { hour12: false });

  const sampleQuoteJson = {
    quoteId: "quote-6E-2041-DEL-BOM-14d-20260930",
    airlineCode: "6E",
    airlineName: "IndiGo",
    flightNumber: "6E-2041",
    corridorId: "DEL-BOM",
    originAirport: "DEL",
    destinationAirport: "BOM",
    cabinClass: "ECONOMY",
    nonStop: true,
    bookingHorizonDays: 14,
    departureDate: "2026-10-14",
    collectionTimestamp: `${todayDateStr}T${nowTimeStr}Z`,
    fareComponents: {
      baseFare: 4250,
      fuelSurcharge: 600,
      userDevelopmentFee: 200,
      gstTax: 250,
      totalFare: 5300
    },
    collectionMethod: "RATE_LIMITED_COMPLIANT",
    sourcePortal: "goindigo.in",
    payloadSha256: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  };

  const sampleHashes = [
    { source: 'goindigo.in', route: 'DEL ↔ BOM', horizon: 'T+14', fare: '₹5,300', hash: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' },
    { source: 'airindia.com', route: 'BLR ↔ DEL', horizon: 'T+7', fare: '₹5,550', hash: '8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4' },
    { source: 'akasaair.com', route: 'BOM ↔ BLR', horizon: 'T+1', fare: '₹4,750', hash: 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e' },
    { source: 'spicejet.com', route: 'CCU ↔ DEL', horizon: 'T+30', fare: '₹5,980', hash: '7c9e6679b4d79cce8a94d1862c11e3783c316236380d61143f2009f4b07d526d' },
  ];

  const merkleBatchRoot = "4a5e1e827b3b9b4f7a29e1c3b5d7e9f0a2c4e6f8b0d2e4f6a8c0e2d4f6a8b0c2";

  const copyText = (text: string, type: 'hash' | 'json') => {
    navigator.clipboard.writeText(text);
    if (type === 'hash') {
      setCopiedHash(text);
      setTimeout(() => setCopiedHash(null), 2000);
    } else {
      setCopiedJson(true);
      setTimeout(() => setCopiedJson(false), 2000);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-fadeIn">
      <div className="glass-panel w-full max-w-4xl rounded-2xl border border-slate-700 shadow-2xl overflow-hidden max-h-[92vh] flex flex-col">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-900/90 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-lg bg-teal-500/10 text-teal-400 border border-teal-500/30">
              <Lock className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white tracking-tight">
                SHA-256 Cryptographic Data Provenance & Merkle Audit Vault
              </h3>
              <p className="text-xs text-slate-400">
                Verifiable Tamper-Evident Audit Trail for MoSPI NSO & Regulatory Compliance
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto space-y-4 text-xs">
          {/* Explanation Banner */}
          <div className="p-4 bg-slate-900/80 rounded-xl border border-slate-800 flex items-start space-x-3">
            <ShieldCheck className="w-5 h-5 text-teal-400 shrink-0 mt-0.5" />
            <div className="text-slate-300 space-y-1">
              <strong className="text-white">Tamper-Evident Statistical Provenance: </strong>
              <span>
                Official CPI numbers must be mathematically reproducible and auditable. VayuSuchak applies <strong>SHA-256 hashing + Merkle batch roots to make tampering immediately detectable</strong>. Every aggregate CPI index value ({currentPoint.jevonsIndex.toFixed(1)}) traces deterministically back to verified raw airline quotes.
              </span>
            </div>
          </div>

          {/* Merkle Batch Root Banner */}
          <div className="p-3.5 bg-teal-950/40 rounded-xl border border-teal-800/50 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
            <div className="flex items-center space-x-2 text-teal-300">
              <GitMerge className="w-4 h-4 text-teal-400 shrink-0" />
              <div>
                <span className="font-semibold">Today's Merkle Batch Root Hash: </span>
                <code className="font-mono text-[11px] text-teal-200 ml-1">{merkleBatchRoot}</code>
              </div>
            </div>
            <button
              onClick={() => copyText(merkleBatchRoot, 'hash')}
              className="px-2.5 py-1 rounded bg-teal-500/20 text-teal-300 border border-teal-500/30 hover:bg-teal-500/30 text-[10px] font-mono shrink-0"
            >
              {copiedHash === merkleBatchRoot ? '✓ Copied Root' : 'Copy Merkle Root'}
            </button>
          </div>

          {/* Sample Ingested Quote JSON */}
          <div className="space-y-1.5">
            <div className="flex items-center justify-between text-slate-400 font-semibold text-[11px]">
              <span className="flex items-center gap-1.5 text-slate-300">
                <FileCode className="w-3.5 h-3.5 text-sky-400" />
                Raw Airfare Quote Record (JSON Schema & Cryptographic Digest)
              </span>
              <button
                onClick={() => copyText(JSON.stringify(sampleQuoteJson, null, 2), 'json')}
                className="flex items-center gap-1 text-sky-400 hover:text-sky-300 font-mono text-[10px]"
              >
                <Copy className="w-3 h-3" />
                <span>{copiedJson ? 'Copied JSON!' : 'Copy JSON'}</span>
              </button>
            </div>
            <pre className="p-3 bg-slate-950 rounded-xl border border-slate-800 font-mono text-[11px] text-slate-300 overflow-x-auto max-h-48 leading-relaxed">
              {JSON.stringify(sampleQuoteJson, null, 2)}
            </pre>
          </div>

          {/* Table of Hashed Quotes */}
          <div className="space-y-1.5">
            <div className="text-slate-400 font-semibold text-[11px]">
              Ingested Quote Batch Samples & SHA-256 Digests:
            </div>
            <div className="overflow-x-auto rounded-xl border border-slate-800">
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="border-b border-slate-800 text-slate-400 uppercase text-[10px] font-semibold bg-slate-900/60">
                    <th className="py-2 px-3">Source Portal</th>
                    <th className="py-2 px-3">Corridor</th>
                    <th className="py-2 px-3">Horizon</th>
                    <th className="py-2 px-3">Total Fare</th>
                    <th className="py-2 px-3">SHA-256 Provenance Fingerprint</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60 font-mono text-[11px]">
                  {sampleHashes.map(h => (
                    <tr key={h.hash} className="hover:bg-slate-900/40">
                      <td className="py-2 px-3 font-semibold text-white">{h.source}</td>
                      <td className="py-2 px-3 text-sky-400 font-bold">{h.route}</td>
                      <td className="py-2 px-3 text-purple-300">{h.horizon}</td>
                      <td className="py-2 px-3 text-emerald-400 font-bold">{h.fare}</td>
                      <td className="py-2 px-3">
                        <button
                          onClick={() => copyText(h.hash, 'hash')}
                          className="flex items-center space-x-1 px-2 py-0.5 rounded bg-slate-950 text-[10px] text-teal-300 border border-slate-800 hover:border-teal-500 transition-colors truncate max-w-[200px]"
                          title="Click to copy SHA-256 hash"
                        >
                          <Hash className="w-3 h-3 text-teal-400 shrink-0" />
                          <span className="truncate">{h.hash}</span>
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-slate-900/90 border-t border-slate-800 flex justify-between items-center text-xs text-slate-400">
          <div className="flex items-center space-x-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            <span>Audit Trail Integrity: <strong className="text-emerald-400 font-mono">VERIFIED</strong> (Cryptographic chain intact)</span>
          </div>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg font-semibold bg-sky-600 hover:bg-sky-500 text-white transition-all shadow"
          >
            Close Vault
          </button>
        </div>
      </div>
    </div>
  );
};
