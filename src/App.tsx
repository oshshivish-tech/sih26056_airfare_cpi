import React, { useState, useEffect } from 'react';
import { Header } from './components/Header';
import { CPIMetricsOverview } from './components/CPIMetricsOverview';
import { IndexChart } from './components/IndexChart';
import { RouteHeatmap } from './components/RouteHeatmap';
import { LiveScraperMonitor } from './components/LiveScraperMonitor';
import { MethodologyDoc } from './components/MethodologyDoc';
import { OutlierAnalysisModal } from './components/OutlierAnalysisModal';
import { ExportModal } from './components/ExportModal';
import { ProvenanceVaultModal } from './components/ProvenanceVaultModal';

import { IndiaFlightMap } from './components/IndiaFlightMap';
import { TransmissionChain } from './components/TransmissionChain';
import { FuelPriceSimulator } from './components/FuelPriceSimulator';
import { DailyCPIChart } from './components/DailyCPIChart';
import { CorridorAvgTable } from './components/CorridorAvgTable';

import { MOCK_CPI_HISTORICAL, MOCK_OUTLIERS, MOCK_ROUTE_WEIGHTS, generateLiveScrapedFares } from './data/mockData';
import { MoSPICPIEngine } from './services/cpiEngine';
import { scraperOrchestrator, ScrapingLogEntry } from './services/scraperEngine';
import { FlightFare, CPIIndexPoint, LeadTimeHorizon, OutlierRecord } from './types';

export const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'overview' | 'corridors' | 'scraper' | 'methodology'>('overview');
  const [selectedLeadTime, setSelectedLeadTime] = useState<LeadTimeHorizon | 'ALL'>('ALL');
  
  const [historicalData, setHistoricalData] = useState<CPIIndexPoint[]>(MOCK_CPI_HISTORICAL);
  const [outliers, setOutliers] = useState<OutlierRecord[]>(MOCK_OUTLIERS);
  const [logs, setLogs] = useState<ScrapingLogEntry[]>([]);
  const [isScraping, setIsScraping] = useState(false);

  const [isOutlierModalOpen, setIsOutlierModalOpen] = useState(false);
  const [isExportModalOpen, setIsExportModalOpen] = useState(false);
  const [isProvenanceModalOpen, setIsProvenanceModalOpen] = useState(false);

  const latestPoint = historicalData.find(p => p.periodLabel.includes('Live')) || historicalData[11] || historicalData[historicalData.length - 1];

  // Calculate live breakdown metrics from baseline fare dataset
  const [liveFares, setLiveFares] = useState<FlightFare[]>(() => generateLiveScrapedFares());
  const currentEngineResult = MoSPICPIEngine.calculateIndex(liveFares, MOCK_ROUTE_WEIGHTS, selectedLeadTime);

  // Subscribe to live scraping log events
  useEffect(() => {
    const unsubscribe = scraperOrchestrator.subscribe((log, newFares) => {
      setLogs(prev => [...prev, log]);

      if (newFares && newFares.length > 0) {
        // Compute updated CPI point from live scraped data
        const result = MoSPICPIEngine.calculateIndex(newFares, MOCK_ROUTE_WEIGHTS, selectedLeadTime);
        const { outliers: newOutliers } = MoSPICPIEngine.filterOutliers(newFares);

        setLiveFares(newFares);
        setOutliers(prev => [...newOutliers, ...prev]);

        // Update live point in index series with EMA exponential smoothing
        setHistoricalData(prev => {
          const updated = [...prev];
          const liveIdx = updated.findIndex(p => p.periodLabel.includes('Live'));
          const targetIdx = liveIdx !== -1 ? liveIdx : 11;
          const currentPoint = updated[targetIdx];
          
          // 85% established index weight + 15% new live batch weight for statistical stability
          const smoothedJevons = Number(((currentPoint.jevonsIndex * 0.85) + (result.jevonsIndex * 0.15)).toFixed(1));
          const smoothedDutot = Number(((currentPoint.dutotIndex * 0.85) + (result.dutotIndex * 0.15)).toFixed(1));
          const smoothedLaspeyres = Number(((currentPoint.weightedLaspeyresIndex * 0.85) + (result.weightedLaspeyresIndex * 0.15)).toFixed(1));

          updated[targetIdx] = {
            ...currentPoint,
            jevonsIndex: smoothedJevons,
            dutotIndex: smoothedDutot,
            weightedLaspeyresIndex: smoothedLaspeyres,
            sampleCount: currentPoint.sampleCount + newFares.length
          };
          return updated;
        });
      }
    });

    return () => unsubscribe();
  }, [selectedLeadTime]);

  const handleRunScrape = async () => {
    try {
      setIsScraping(true);
      await scraperOrchestrator.executeLiveScrapeJob();
    } catch (err) {
      console.error(err);
    } finally {
      setIsScraping(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-sky-500 selection:text-white">
      {/* Top Sticky Header */}
      <Header
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        onRunScrape={handleRunScrape}
        onOpenExport={() => setIsExportModalOpen(true)}
        onOpenProvenance={() => setIsProvenanceModalOpen(true)}
        isScraping={isScraping}
        latestIndex={latestPoint.jevonsIndex}
        yoyInflation={latestPoint.yoyInflationRate}
      />

      {/* Main Page Body */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Top Key Metrics Overview */}
        <CPIMetricsOverview
          currentPoint={latestPoint}
          totalDataPoints={latestPoint.sampleCount}
          outlierCount={outliers.length}
          onOpenOutlierModal={() => setIsOutlierModalOpen(true)}
        />

        {/* Tab 1: Overview */}
        {activeTab === 'overview' && (
          <div className="space-y-6">
            <TransmissionChain currentAirfareSurgePct={latestPoint.momInflationRate || 11.4} />

            <IndexChart
              data={historicalData}
              selectedLeadTime={selectedLeadTime}
              onSelectLeadTime={setSelectedLeadTime}
            />

            <DailyCPIChart />

            <FuelPriceSimulator baseJevonsIndex={latestPoint.jevonsIndex} />

            <IndiaFlightMap corridorBreakdown={currentEngineResult.corridorBreakdown} />

            <CorridorAvgTable corridorBreakdown={currentEngineResult.corridorBreakdown} />

            <RouteHeatmap corridorBreakdown={currentEngineResult.corridorBreakdown} />
          </div>
        )}

        {/* Tab 2: Flight Corridors */}
        {activeTab === 'corridors' && (
          <RouteHeatmap corridorBreakdown={currentEngineResult.corridorBreakdown} />
        )}

        {/* Tab 3: Scraper Monitor */}
        {activeTab === 'scraper' && (
          <LiveScraperMonitor
            sources={scraperOrchestrator.getSourceStatuses()}
            logs={logs}
            isScraping={isScraping}
            onRunScrape={handleRunScrape}
          />
        )}

        {/* Tab 4: UN/ILO Methodology */}
        {activeTab === 'methodology' && <MethodologyDoc />}
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-800 bg-slate-950 py-6 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <div>
            <strong>AirIntel India</strong> • Team Rookie • SIH 2026 Problem Statement 26056
          </div>
          <div className="text-slate-400 font-mono">
            National Statistical Office (NSO) Augmentation Framework
          </div>
        </div>
      </footer>

      {/* Modals */}
      <OutlierAnalysisModal
        isOpen={isOutlierModalOpen}
        onClose={() => setIsOutlierModalOpen(false)}
        outliers={outliers}
      />

      <ExportModal
        isOpen={isExportModalOpen}
        onClose={() => setIsExportModalOpen(false)}
        historicalData={historicalData}
        currentPoint={latestPoint}
      />

      <ProvenanceVaultModal
        isOpen={isProvenanceModalOpen}
        onClose={() => setIsProvenanceModalOpen(false)}
        currentPoint={latestPoint}
      />
    </div>
  );
};
export default App;
