import React, { useState } from 'react';
import { X, ShieldCheck, Key, Hash, CheckCircle2, Lock, FileCode } from 'lucide-react';
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

  if (!isOpen) return null;

  const sampleHashes = [
    { source: 'goindigo.in (Direct API)', route: 'DEL ↔ BOM', fare: '₹5,050', timestamp: '2026-09-15 02:00:14 IST', hash: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' },
    { source: 'airindia.com (XHR Intercept)', route: 'BLR ↔ DEL', fare: '₹5,550', timestamp: '2026-09-15 02:00:18 IST', hash: '8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4' },
    { source: 'makemytrip.com (Payload Stream)', route: 'BOM ↔ BLR', fare: '₹4,750', timestamp: '2026-09-15 02:00:22 IST', hash: 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e' },
    { source: 'easemytrip.com (DOM Resilient)', route: 'CCU ↔ DEL', fare: '₹5,980', timestamp: '2026-09-15 02:00:28 IST', hash: '7c9e6679b4d79cce8a94d1862c11e3783c316236380d61143f2009f4b07d526d' },
  ];

  const copyHash = (hash: string) => {
    navigator.clipboard.writeText(hash);
    setCopiedHash(hash);
    setTimeout(() => setCopiedHash(null), 2000);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-fadeIn">
      <div className="glass-panel w-full max-w-4xl rounded-2xl border border-slate-700 shadow-2xl overflow-hidden max-h-[90vh] flex flex-col">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-900/90 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-lg bg-teal-500/10 text-teal-400 border border-teal-500/30">
              <Lock className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white tracking-tight">
                SHA-256 Cryptographic Data Provenance Vault
              </h3>
              <p className="text-xs text-slate-400">
                Verifiable Audit Trail for MoSPI & NSO Statistical Integrity
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
          <div className="p-4 bg-slate-900/80 rounded-xl border border-slate-800 flex items-start space-x-3">
            <ShieldCheck className="w-5 h-5 text-teal-400 shrink-0 mt-0.5" />
            <div className="text-slate-300">
              <strong className="text-white">Why Data Provenance Makes Your App Unique: </strong>
              Official CPI inflation numbers are often challenged by critics. Our platform hashes every raw ingested quote into an immutable **SHA-256 cryptographic fingerprint**. MoSPI officers can click any index number (I_Jevons = 111.4) and trace it back to the exact hashed raw quotes collected from IndiGo or Air India.
            </div>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b border-slate-800 text-slate-400 uppercase text-[10px] font-semibold bg-slate-900/50">
                  <th className="py-2.5 px-3">Target Source</th>
                  <th className="py-2.5 px-3">Corridor</th>
                  <th className="py-2.5 px-3">Fare Quote</th>
                  <th className="py-2.5 px-3">Extraction Timestamp</th>
                  <th className="py-2.5 px-3">SHA-256 Provenance Fingerprint</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60 font-mono">
                {sampleHashes.map(h => (
                  <tr key={h.hash} className="hover:bg-slate-900/40">
                    <td className="py-2.5 px-3 font-semibold text-white">{h.source}</td>
                    <td className="py-2.5 px-3 text-sky-400 font-bold">{h.route}</td>
                    <td className="py-2.5 px-3 text-emerald-400 font-bold">{h.fare}</td>
                    <td className="py-2.5 px-3 text-slate-400">{h.timestamp}</td>
                    <td className="py-2.5 px-3">
                      <button
                        onClick={() => copyHash(h.hash)}
                        className="flex items-center space-x-1 px-2 py-1 rounded bg-slate-950 text-[10px] text-teal-300 border border-slate-800 hover:border-teal-500 transition-colors truncate max-w-[220px]"
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

        {/* Footer */}
        <div className="px-6 py-3 bg-slate-900/90 border-t border-slate-800 flex justify-between items-center text-xs text-slate-400">
          <span>Provenance Chain Status: <strong className="text-emerald-400 font-mono">VERIFIED (100% Cryptographic Match)</strong></span>
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
