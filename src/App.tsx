import React, { useState, useEffect } from 'react';
import { Header } from './components/Header';
import { CPIMetricsOverview } from './components/CPIMetricsOverview';
import { IndexChart } from './components/IndexChart';
import { RouteHeatmap } from './components/RouteHeatmap';
import { LiveScraperMonitor } from './components/LiveScraperMonitor';
import { MethodologyDoc } from './components/MethodologyDoc';
import { OutlierAnalysisModal } from './components/OutlierAnalysisModal';
import { ExportModal } from './components/ExportModal';

import { MOCK_CPI_HISTORICAL, MOCK_OUTLIERS, MOCK_ROUTE_WEIGHTS } from './data/mockData';
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

  const latestPoint = historicalData[historicalData.length - 1];

  // Calculate live breakdown metrics from current data
  const currentEngineResult = MoSPICPIEngine.calculateIndex([], MOCK_ROUTE_WEIGHTS, selectedLeadTime);

  // Subscribe to live scraping log events
  useEffect(() => {
    const unsubscribe = scraperOrchestrator.subscribe((log, newFares) => {
      setLogs(prev => [...prev, log]);

      if (newFares && newFares.length > 0) {
        // Compute updated CPI point from live scraped data
        const result = MoSPICPIEngine.calculateIndex(newFares, MOCK_ROUTE_WEIGHTS, selectedLeadTime);
        const { outliers: newOutliers } = MoSPICPIEngine.filterOutliers(newFares);

        setOutliers(prev => [...newOutliers, ...prev]);

        // Update latest point in index series
        setHistoricalData(prev => {
          const updated = [...prev];
          const lastIdx = updated.length - 1;
          updated[lastIdx] = {
            ...updated[lastIdx],
            jevonsIndex: result.jevonsIndex,
            dutotIndex: result.dutotIndex,
            weightedLaspeyresIndex: result.weightedLaspeyresIndex,
            sampleCount: updated[lastIdx].sampleCount + newFares.length
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
            <IndexChart
              data={historicalData}
              selectedLeadTime={selectedLeadTime}
              onSelectLeadTime={setSelectedLeadTime}
            />

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
            <strong>MoSPI Airfare CPI Engine</strong> • Smart India Hackathon (SIH) 2026 Problem Statement 26056
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
    </div>
  );
};
export default App;
