import React, { useState } from 'react';
import { X, Download, FileText, CheckCircle2, Copy } from 'lucide-react';
import { CPIIndexPoint } from '../types';

interface ExportModalProps {
  isOpen: boolean;
  onClose: () => void;
  historicalData: CPIIndexPoint[];
  currentPoint: CPIIndexPoint;
}

export const ExportModal: React.FC<ExportModalProps> = ({
  isOpen,
  onClose,
  historicalData,
  currentPoint
}) => {
  const [copied, setCopied] = useState(false);
  const [exportFormat, setExportFormat] = useState<'CSV' | 'JSON' | 'MOSPI_FORM'>('CSV');

  if (!isOpen) return null;

  const handleDownloadCSV = () => {
    const headers = "Period,Jevons_Index_Geometric,Dutot_Index,Weighted_Laspeyres_Index,MoSPI_Manual_Baseline,Sample_Count,YoY_Inflation_Rate\n";
    const rows = historicalData.map(d => 
      `"${d.periodLabel}",${d.jevonsIndex},${d.dutotIndex},${d.weightedLaspeyresIndex},${d.officialMoSPICPIBaseline},${d.sampleCount},${d.yoyInflationRate}%`
    ).join("\n");

    const blob = new Blob([headers + rows], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `MoSPI_Airfare_CPI_Report_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleDownloadJSON = () => {
    const jsonString = JSON.stringify({
      title: "MoSPI Airfare Consumer Price Index (CPI) Report - SIH 26056",
      generatedAt: new Date().toISOString(),
      baseYear: 2024,
      currentPeriod: currentPoint,
      seriesData: historicalData
    }, null, 2);

    const blob = new Blob([jsonString], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `MoSPI_Airfare_CPI_Data_${new Date().toISOString().split('T')[0]}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const copyDataToClipboard = () => {
    const summaryText = `MoSPI Airfare CPI Report (SIH 26056)\nGenerated: ${new Date().toLocaleString()}\nCurrent Index: ${currentPoint.jevonsIndex.toFixed(1)} (Base = 100)\nYoY Inflation: +${currentPoint.yoyInflationRate}%\nScraped Quotes Verified: ${currentPoint.sampleCount.toLocaleString()}`;
    navigator.clipboard.writeText(summaryText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-fadeIn">
      <div className="glass-panel w-full max-w-xl rounded-2xl border border-slate-700 shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-900/90 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="p-2 rounded-lg bg-sky-500/10 text-sky-400 border border-sky-500/30">
              <Download className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white tracking-tight">
                Export MoSPI Official Airfare CPI Report
              </h3>
              <p className="text-xs text-slate-400">
                Formatted data export for National Statistical Office (NSO) ingestion
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
        <div className="p-6 space-y-4 text-xs">
          <div className="space-y-2">
            <label className="text-slate-300 font-semibold block">Select Format:</label>
            <div className="grid grid-cols-3 gap-3">
              <button
                onClick={() => setExportFormat('CSV')}
                className={`p-3 rounded-xl border text-center transition-all ${
                  exportFormat === 'CSV'
                    ? 'bg-sky-500/20 text-sky-300 border-sky-500 shadow'
                    : 'bg-slate-900 text-slate-400 border-slate-800 hover:bg-slate-850'
                }`}
              >
                <FileText className="w-5 h-5 mx-auto mb-1 text-sky-400" />
                <span className="font-bold block">CSV Format</span>
                <span className="text-[10px] text-slate-400">Excel / MoSPI NSO</span>
              </button>

              <button
                onClick={() => setExportFormat('JSON')}
                className={`p-3 rounded-xl border text-center transition-all ${
                  exportFormat === 'JSON'
                    ? 'bg-sky-500/20 text-sky-300 border-sky-500 shadow'
                    : 'bg-slate-900 text-slate-400 border-slate-800 hover:bg-slate-850'
                }`}
              >
                <FileText className="w-5 h-5 mx-auto mb-1 text-emerald-400" />
                <span className="font-bold block">JSON Stream</span>
                <span className="text-[10px] text-slate-400">API Endpoint Payload</span>
              </button>

              <button
                onClick={() => setExportFormat('MOSPI_FORM')}
                className={`p-3 rounded-xl border text-center transition-all ${
                  exportFormat === 'MOSPI_FORM'
                    ? 'bg-sky-500/20 text-sky-300 border-sky-500 shadow'
                    : 'bg-slate-900 text-slate-400 border-slate-800 hover:bg-slate-850'
                }`}
              >
                <FileText className="w-5 h-5 mx-auto mb-1 text-purple-400" />
                <span className="font-bold block">Summary Text</span>
                <span className="text-[10px] text-slate-400">Quick Clipboard</span>
              </button>
            </div>
          </div>

          <div className="p-4 bg-slate-950/80 rounded-xl border border-slate-800 font-mono text-[11px] text-slate-300 space-y-1">
            <div className="text-sky-400 font-bold"># Preview Summary (MoSPI Airfare Sub-Index)</div>
            <div>Base Year: 2025 = 100.0</div>
            <div>Current Index (Sep 2026): {currentPoint.jevonsIndex.toFixed(1)}</div>
            <div>YoY Airfare Inflation: +{currentPoint.yoyInflationRate}%</div>
            <div>Total Quotes Verified: {currentPoint.sampleCount.toLocaleString()}</div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-4 bg-slate-900/90 border-t border-slate-800 flex items-center justify-between">
          <button
            onClick={copyDataToClipboard}
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition-all"
          >
            {copied ? <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5 text-slate-400" />}
            <span>{copied ? 'Copied Summary!' : 'Copy Summary'}</span>
          </button>

          <div className="flex items-center space-x-2">
            <button
              onClick={onClose}
              className="px-3.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white transition-all"
            >
              Cancel
            </button>
            <button
              onClick={exportFormat === 'CSV' ? handleDownloadCSV : handleDownloadJSON}
              className="flex items-center space-x-2 px-4 py-1.5 rounded-lg text-xs font-semibold bg-sky-600 hover:bg-sky-500 text-white transition-all shadow-md shadow-sky-600/30"
            >
              <Download className="w-3.5 h-3.5" />
              <span>Download File</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
