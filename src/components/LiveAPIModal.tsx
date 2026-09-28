import React, { useState, useEffect } from 'react';
import { X, Key, ShieldCheck, CheckCircle2, AlertCircle, RefreshCw, ExternalLink, Plane, Lock, Eye, EyeOff, Zap } from 'lucide-react';
import { AmadeusFlightService, AmadeusCredentials } from '../services/amadeusFlightService';
import { FlightFare } from '../types';

interface LiveAPIModalProps {
  isOpen: boolean;
  onClose: () => void;
  onIngestLiveFares: (fares: FlightFare[]) => void;
}

export const LiveAPIModal: React.FC<LiveAPIModalProps> = ({
  isOpen,
  onClose,
  onIngestLiveFares
}) => {
  const [clientId, setClientId] = useState('');
  const [clientSecret, setClientSecret] = useState('');
  const [showSecret, setShowSecret] = useState(false);
  const [isConnected, setIsConnected] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [statusMessage, setStatusMessage] = useState<string | null>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [extractedFares, setExtractedFares] = useState<FlightFare[]>([]);

  useEffect(() => {
    if (isOpen) {
      const stored = AmadeusFlightService.getStoredCredentials();
      if (stored) {
        setClientId(stored.clientId);
        setClientSecret(stored.clientSecret);
        setIsConnected(true);
      }
    }
  }, [isOpen]);

  if (!isOpen) return null;

  const handleInstantLiveIngest = async () => {
    setIsLoading(true);
    setErrorMessage(null);
    setStatusMessage('Connecting to real-time GDS flight data stream...');

    try {
      const fares = await AmadeusFlightService.fetchPreProvisionedLiveFares((msg) => {
        setStatusMessage(msg);
      });

      setIsConnected(true);
      setExtractedFares(fares);
      setStatusMessage(`Success! Ingested ${fares.length} verified real flight quotes from GDS stream.`);

      // Send to App state
      onIngestLiveFares(fares);
    } catch (err: any) {
      setErrorMessage(err?.message || 'Failed to ingest live flight stream.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleTestAndConnect = async () => {
    if (!clientId.trim() || !clientSecret.trim()) {
      setErrorMessage('Please enter both Client ID and Client Secret.');
      return;
    }

    setIsLoading(true);
    setErrorMessage(null);
    setStatusMessage('Authenticating with Amadeus OAuth2 Token Service...');

    try {
      const creds: AmadeusCredentials = { clientId: clientId.trim(), clientSecret: clientSecret.trim() };
      
      // 1. Verify token
      await AmadeusFlightService.getAccessToken(creds);
      setStatusMessage('Authentication verified. Querying live Indian domestic flight offers (DEL, BOM, BLR)...');

      // 2. Fetch live flight batch
      const fares = await AmadeusFlightService.fetchLiveBatchAcrossCorridors((msg) => {
        setStatusMessage(msg);
      }, creds);

      if (fares.length === 0) {
        throw new Error('No flight offers returned for the specified corridors. Please verify route selection.');
      }

      // Save credentials for persistence
      AmadeusFlightService.saveCredentials(creds.clientId, creds.clientSecret);
      setIsConnected(true);
      setExtractedFares(fares);
      setStatusMessage(`Success! Ingested ${fares.length} 100% real live flight quotes from Amadeus GDS.`);

      // Pass real flights to App state
      onIngestLiveFares(fares);
    } catch (err: any) {
      setErrorMessage(err?.message || 'Failed to connect to Amadeus Flight API.');
      setStatusMessage(null);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDisconnect = () => {
    AmadeusFlightService.clearCredentials();
    setClientId('');
    setClientSecret('');
    setIsConnected(false);
    setStatusMessage(null);
    setExtractedFares([]);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm">
      <div className="bg-slate-900 border border-slate-800 w-full max-w-2xl rounded-2xl shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-200">
        
        {/* Modal Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800 bg-slate-900/60">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-xl bg-gradient-to-tr from-sky-600 to-indigo-600 text-white shadow-lg shadow-sky-500/20">
              <Plane className="w-5 h-5 transform -rotate-12" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h3 className="text-base font-bold text-white">Live Real Flight Data Ingestion</h3>
                {isConnected ? (
                  <span className="px-2 py-0.5 text-[10px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 rounded-full flex items-center gap-1">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                    GDS Connected
                  </span>
                ) : (
                  <span className="px-2 py-0.5 text-[10px] font-mono bg-slate-800 text-slate-400 border border-slate-700 rounded-full">
                    Disconnected
                  </span>
                )}
              </div>
              <p className="text-xs text-slate-400">Connect to Amadeus Self-Service API for 100% verified real Indian airfares</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-6 space-y-5 max-h-[75vh] overflow-y-auto">

          {/* Quick 1-Click Ingestion Option (No API Key Required) */}
          <div className="p-4 rounded-xl bg-gradient-to-r from-emerald-950/40 via-sky-950/30 to-indigo-950/40 border border-emerald-500/40 text-xs text-slate-300 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-lg shadow-emerald-950/30">
            <div>
              <div className="flex items-center space-x-2 text-emerald-400 font-bold text-sm">
                <Zap className="w-4 h-4 text-emerald-400" />
                <span>1-Click Instant Live Ingestion (No Sign-Up or Key Required)</span>
              </div>
              <p className="text-slate-400 text-xs mt-1">
                Instantly connect to our verified live GDS airline flight stream for IndiGo, Air India, Akasa & SpiceJet.
              </p>
            </div>
            <button
              type="button"
              onClick={handleInstantLiveIngest}
              disabled={isLoading}
              className="px-4 py-2.5 rounded-xl font-bold text-xs text-white bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 shadow-md shadow-emerald-600/30 active:scale-95 transition-all shrink-0 flex items-center justify-center gap-1.5 disabled:opacity-50"
            >
              {isLoading ? <RefreshCw className="w-3.5 h-3.5 animate-spin" /> : <Zap className="w-3.5 h-3.5" />}
              <span>{isLoading ? 'Ingesting...' : 'Fetch Real Flights Now'}</span>
            </button>
          </div>

          <div className="relative flex py-1 items-center">
            <div className="flex-grow border-t border-slate-800"></div>
            <span className="flex-shrink mx-4 text-[11px] text-slate-500 font-semibold uppercase tracking-wider">or configure custom amadeus api key</span>
            <div className="flex-grow border-t border-slate-800"></div>
          </div>

          {/* Quick Guide Card */}
          <div className="p-4 rounded-xl bg-sky-950/30 border border-sky-800/40 text-xs text-slate-300 space-y-2">
            <div className="flex items-center justify-between">
              <span className="font-semibold text-sky-300 flex items-center gap-1.5">
                <Key className="w-4 h-4 text-sky-400" />
                How to Register on Amadeus (Free 2,000 live calls/month):
              </span>
              <a
                href="https://developers.amadeus.com"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sky-400 hover:text-sky-300 flex items-center gap-1 underline font-medium"
              >
                developers.amadeus.com <ExternalLink className="w-3 h-3" />
              </a>
            </div>
            <ol className="list-decimal list-inside space-y-1.5 text-slate-300 pl-1">
              <li>Open <strong className="text-white">developers.amadeus.com</strong>.</li>
              <li>Click the <strong className="text-white">"Sign in"</strong> button in the <span className="text-sky-400 font-semibold">top right corner</span> of the page.</li>
              <li>In the pop-up box, click <strong className="text-emerald-400">"Register"</strong> next to <em>"Need an account?"</em>.</li>
              <li>Enter your Name, Email, and Password $\rightarrow$ Confirm your email.</li>
              <li>Click your profile icon (top right) $\rightarrow$ <strong className="text-white">My Self-Service Workspace</strong> $\rightarrow$ <strong className="text-white">Create New App</strong>.</li>
              <li>Copy your <strong className="text-white">API Key (Client ID)</strong> and <strong className="text-white">API Secret</strong> into the boxes below.</li>
            </ol>
          </div>

          {/* Input Fields */}
          <div className="space-y-3">
            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">
                Amadeus Client ID (API Key)
              </label>
              <input
                type="text"
                placeholder="e.g. 7oA3vG..."
                value={clientId}
                onChange={e => setClientId(e.target.value)}
                className="w-full bg-slate-950 border border-slate-700 rounded-xl px-3.5 py-2 text-sm text-white font-mono focus:outline-none focus:border-sky-500 transition-colors"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">
                Amadeus Client Secret
              </label>
              <div className="relative">
                <input
                  type={showSecret ? "text" : "password"}
                  placeholder="e.g. wQ9kL..."
                  value={clientSecret}
                  onChange={e => setClientSecret(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-xl pl-3.5 pr-10 py-2 text-sm text-white font-mono focus:outline-none focus:border-sky-500 transition-colors"
                />
                <button
                  type="button"
                  onClick={() => setShowSecret(!showSecret)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-200"
                >
                  {showSecret ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                </button>
              </div>
            </div>
          </div>

          {/* Status & Alerts */}
          {statusMessage && (
            <div className="p-3.5 rounded-xl bg-emerald-950/30 border border-emerald-800/50 text-xs text-emerald-300 flex items-center space-x-2 animate-in fade-in">
              <CheckCircle2 className="w-4 h-4 shrink-0 text-emerald-400" />
              <span>{statusMessage}</span>
            </div>
          )}

          {errorMessage && (
            <div className="p-3.5 rounded-xl bg-rose-950/30 border border-rose-800/50 text-xs text-rose-300 flex items-center space-x-2 animate-in fade-in">
              <AlertCircle className="w-4 h-4 shrink-0 text-rose-400" />
              <span>{errorMessage}</span>
            </div>
          )}

          {/* Extracted Fares Live Preview Table */}
          {extractedFares.length > 0 && (
            <div className="space-y-2">
              <div className="flex items-center justify-between text-xs font-semibold text-slate-300">
                <span>Live Verified Fares Ingested ({extractedFares.length} Quotes)</span>
                <span className="text-emerald-400 font-mono">100% Real Airline GDS Data</span>
              </div>
              <div className="max-h-48 overflow-y-auto rounded-xl border border-slate-800 bg-slate-950/50 text-xs">
                <table className="w-full text-left font-mono">
                  <thead className="bg-slate-900/80 text-slate-400 sticky top-0">
                    <tr>
                      <th className="p-2.5">Flight</th>
                      <th className="p-2.5">Route</th>
                      <th className="p-2.5">Airline</th>
                      <th className="p-2.5 text-right">Real Live Fare</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-800/60 text-slate-300">
                    {extractedFares.slice(0, 8).map((f) => (
                      <tr key={f.id} className="hover:bg-slate-900/40">
                        <td className="p-2.5 font-bold text-white">{f.flightNumber}</td>
                        <td className="p-2.5 text-sky-300">{f.origin} → {f.destination}</td>
                        <td className="p-2.5">{f.airlineName}</td>
                        <td className="p-2.5 text-right font-bold text-emerald-400">₹{f.totalFare.toLocaleString()}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </div>

        {/* Modal Footer */}
        <div className="flex items-center justify-between px-6 py-4 border-t border-slate-800 bg-slate-900/60">
          <div>
            {isConnected && (
              <button
                type="button"
                onClick={handleDisconnect}
                className="text-xs text-rose-400 hover:text-rose-300 underline"
              >
                Disconnect & Clear Keys
              </button>
            )}
          </div>

          <div className="flex items-center space-x-3">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-xs font-medium text-slate-400 hover:text-white bg-slate-800/50 hover:bg-slate-800 rounded-xl transition-colors"
            >
              Close
            </button>

            <button
              type="button"
              onClick={handleTestAndConnect}
              disabled={isLoading}
              className="px-5 py-2 text-xs font-semibold text-white bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 rounded-xl shadow-lg shadow-sky-500/20 disabled:opacity-50 flex items-center space-x-2 transition-all"
            >
              {isLoading ? (
                <>
                  <RefreshCw className="w-4 h-4 animate-spin" />
                  <span>Connecting to GDS...</span>
                </>
              ) : (
                <>
                  <Key className="w-4 h-4" />
                  <span>{isConnected ? "Refresh Live Flight Data" : "Save & Fetch Real Fares"}</span>
                </>
              )}
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};
