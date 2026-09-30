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
import { LiveAPIModal } from './components/LiveAPIModal';

import { IndiaFlightMap } from './components/IndiaFlightMap';
import { TransmissionChain } from './components/TransmissionChain';
import { FuelPriceSimulator } from './components/FuelPriceSimulator';
import { DailyCPIChart } from './components/DailyCPIChart';
import { CorridorAvgTable } from './components/CorridorAvgTable';
import { LeadTimeElasticityCard } from './components/LeadTimeElasticityCard';
import { DgcaBacktestComparison } from './components/DgcaBacktestComparison';
import { RestApiExplorerModal } from './components/RestApiExplorerModal';
import { DataHealthPanel } from './components/DataHealthPanel';

import { MOCK_CPI_HISTORICAL, MOCK_DAILY_CPI, MOCK_OUTLIERS, MOCK_ROUTE_WEIGHTS, generateLiveScrapedFares } from './data/mockData';
import { MoSPICPIEngine } from './services/cpiEngine';
import { scraperOrchestrator, ScrapingLogEntry } from './services/scraperEngine';
import { AmadeusFlightService } from './services/amadeusFlightService';
import { FlightFare, CPIIndexPoint, LeadTimeHorizon, OutlierRecord, DailyFarePoint } from './types';

export const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'overview' | 'corridors' | 'scraper' | 'methodology'>('overview');
  const [selectedLeadTime, setSelectedLeadTime] = useState<LeadTimeHorizon | 'ALL'>('ALL');
  
  const [historicalData, setHistoricalData] = useState<CPIIndexPoint[]>(MOCK_CPI_HISTORICAL);
  const [dailyData, setDailyData] = useState<DailyFarePoint[]>(MOCK_DAILY_CPI);
  const [hasLiveScraped, setHasLiveScraped] = useState(false);
  const [scrapeNotification, setScrapeNotification] = useState<string | null>(null);
  const [outliers, setOutliers] = useState<OutlierRecord[]>(MOCK_OUTLIERS);
  const [logs, setLogs] = useState<ScrapingLogEntry[]>([]);
  const [isScraping, setIsScraping] = useState(false);

  const [isOutlierModalOpen, setIsOutlierModalOpen] = useState(false);
  const [isExportModalOpen, setIsExportModalOpen] = useState(false);
  const [isProvenanceModalOpen, setIsProvenanceModalOpen] = useState(false);
  const [isLiveAPIModalOpen, setIsLiveAPIModalOpen] = useState(false);
  const [isRestApiModalOpen, setIsRestApiModalOpen] = useState(false);
  const [isLiveAPIConnected, setIsLiveAPIConnected] = useState(() => Boolean(AmadeusFlightService.getStoredCredentials()));

  const baseLatestPoint = historicalData.find(p => p.periodLabel.includes('Live')) || historicalData[11] || historicalData[historicalData.length - 1];

  const leadTimeMultipliers: Record<LeadTimeHorizon | 'ALL', number> = {
    'ALL': 1.0,
    '1d': 1.14,
    '7d': 1.07,
    '14d': 1.01,
    '15d': 1.01,
    '30d': 0.94,
    '45d': 0.90
  };
  const horizonMult = leadTimeMultipliers[selectedLeadTime] || 1.0;

  const latestPoint = {
    ...baseLatestPoint,
    jevonsIndex: Number((baseLatestPoint.jevonsIndex * horizonMult).toFixed(1)),
    dutotIndex: Number((baseLatestPoint.dutotIndex * horizonMult).toFixed(1)),
    weightedLaspeyresIndex: Number((baseLatestPoint.weightedLaspeyresIndex * horizonMult).toFixed(1)),
    periodLabel: selectedLeadTime === 'ALL'
      ? baseLatestPoint.periodLabel
      : `${baseLatestPoint.periodLabel.split('(')[0].trim()} (${selectedLeadTime === '1d' ? '1-Day Urgent' : selectedLeadTime === '45d' ? '45-Day Leisure' : selectedLeadTime})`
  };

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
        setHasLiveScraped(true);

        const activeFares = newFares.filter(f => selectedLeadTime === 'ALL' || f.leadTimeHorizon === selectedLeadTime);
        const faresToUse = activeFares.length > 0 ? activeFares : newFares;
        const batchAvgFare = Math.round(faresToUse.reduce((sum, f) => sum + f.totalFare, 0) / faresToUse.length);
        const batchJevons = Number(result.jevonsIndex.toFixed(1));

        setScrapeNotification(
          `Live Scrape Ingested: +${newFares.length} verified quotes across 12 corridors. Real-time Jevons Index updated to ${batchJevons} (Avg Fare ₹${batchAvgFare.toLocaleString()})`
        );

        // Update Day-Wise Daily Series
        setDailyData(prev => {
          const updated = [...prev];
          const targetIdx = updated.length - 1;
          const oldPoint = updated[targetIdx];
          const todayStr = oldPoint.date;
          
          const rawLabel = oldPoint.dayLabel.replace(' - Today)', '').replace(' - Live)', '').replace(')', '');
          const liveDayLabel = `${rawLabel} - Live)`;
          const shortDate = rawLabel.split('(')[0].trim();

          const last6 = updated.slice(Math.max(0, targetIdx - 6), targetIdx);
          const moving7d = Math.round((last6.reduce((acc, p) => acc + p.dailyAvgFare, 0) + batchAvgFare) / (last6.length + 1));

          updated[targetIdx] = {
            ...oldPoint,
            date: todayStr,
            dayLabel: liveDayLabel,
            dailyAvgFare: batchAvgFare,
            dailyJevonsIndex: batchJevons,
            movingAverage7d: moving7d,
            scrapedQuotesCount: (oldPoint?.scrapedQuotesCount || 3650) + newFares.length
          };
          return updated;
        });

        // Update Monthly Index Series
        setHistoricalData(prev => {
          const updated = [...prev];
          const liveIdx = updated.findIndex(p => p.periodLabel.includes('Live'));
          const targetIdx = liveIdx !== -1 ? liveIdx : 11;
          const currentPoint = updated[targetIdx];

          const shortDate = new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short' });
          const livePeriodLabel = `Sep 2026 (Live - ${shortDate})`;

          updated[targetIdx] = {
            ...currentPoint,
            periodLabel: livePeriodLabel,
            jevonsIndex: batchJevons,
            dutotIndex: Number(result.dutotIndex.toFixed(1)),
            weightedLaspeyresIndex: Number(result.weightedLaspeyresIndex.toFixed(1)),
            sampleCount: currentPoint.sampleCount + newFares.length
          };
          return updated;
        });
      }
    });

    return () => unsubscribe();
  }, [selectedLeadTime]);

  const handleIngestLiveFares = (newRealFares: FlightFare[]) => {
    const result = MoSPICPIEngine.calculateIndex(newRealFares, MOCK_ROUTE_WEIGHTS, selectedLeadTime);
    const { outliers: newOutliers } = MoSPICPIEngine.filterOutliers(newRealFares);

    setLiveFares(newRealFares);
    setOutliers(prev => [...newOutliers, ...prev]);
    setHasLiveScraped(true);
    setIsLiveAPIConnected(true);

    const batchAvgFare = Math.round(newRealFares.reduce((sum, f) => sum + f.totalFare, 0) / newRealFares.length);
    const batchJevons = Number(result.jevonsIndex.toFixed(1));

    setScrapeNotification(
      `100% Real Live Flight Data Ingested: +${newRealFares.length} verified quotes from Amadeus GDS. Live Jevons Index updated to ${batchJevons} (Avg Fare ₹${batchAvgFare.toLocaleString()})`
    );

    // Update Day-Wise Series
    setDailyData(prev => {
      const updated = [...prev];
      const targetIdx = updated.length - 1;
      const oldPoint = updated[targetIdx];
      const last6 = updated.slice(Math.max(0, targetIdx - 6), targetIdx);
      const moving7d = Math.round((last6.reduce((acc, p) => acc + p.dailyAvgFare, 0) + batchAvgFare) / (last6.length + 1));

      updated[targetIdx] = {
        ...oldPoint,
        dayLabel: `${oldPoint.dayLabel.replace(' - Live)', '').replace(' - Live GDS)', '').replace(')', '')} - Live GDS)`,
        dailyAvgFare: batchAvgFare,
        dailyJevonsIndex: batchJevons,
        movingAverage7d: moving7d,
        scrapedQuotesCount: (oldPoint?.scrapedQuotesCount || 3720) + newRealFares.length
      };
      return updated;
    });

    // Update Monthly Index Series
    setHistoricalData(prev => {
      const updated = [...prev];
      const liveIdx = updated.findIndex(p => p.periodLabel.includes('Live'));
      const targetIdx = liveIdx !== -1 ? liveIdx : updated.length - 1;
      const currentP = updated[targetIdx];

      updated[targetIdx] = {
        ...currentP,
        periodLabel: `Sep 2026 (Live GDS - 22 Sep)`,
        jevonsIndex: batchJevons,
        dutotIndex: Number(result.dutotIndex.toFixed(1)),
        weightedLaspeyresIndex: Number(result.weightedLaspeyresIndex.toFixed(1)),
        sampleCount: currentP.sampleCount + newRealFares.length
      };
      return updated;
    });
  };

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
        onOpenLiveAPI={() => setIsLiveAPIModalOpen(true)}
        onOpenRestApi={() => setIsRestApiModalOpen(true)}
        isLiveAPIConnected={isLiveAPIConnected}
        isScraping={isScraping}
        latestIndex={latestPoint.jevonsIndex}
        yoyInflation={latestPoint.yoyInflationRate}
      />

      {/* Main Page Body */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Top Key Metrics Overview */}
        <div id="cpi-metrics-overview">
          <CPIMetricsOverview
            currentPoint={latestPoint}
            latestDailyPoint={dailyData[dailyData.length - 1]}
            totalDataPoints={latestPoint.sampleCount}
            outlierCount={outliers.length}
            onOpenOutlierModal={() => setIsOutlierModalOpen(true)}
          />
        </div>

        {/* Tab 1: Overview */}
        {activeTab === 'overview' && (
          <div className="space-y-6">
            <DataHealthPanel
              onOpenScraperTab={() => setActiveTab('scraper')}
              onRunScrape={handleRunScrape}
              isScraping={isScraping}
            />

            {scrapeNotification && (
              <div className="bg-emerald-500/15 border border-emerald-500/40 rounded-xl p-4 flex items-center justify-between shadow-lg shadow-emerald-950/40 animate-pulse">
                <div className="flex items-center space-x-3">
                  <span className="relative flex h-3 w-3">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
                  </span>
                  <span className="text-sm font-semibold text-emerald-300">
                    {scrapeNotification}
                  </span>
                </div>
                <span className="text-xs font-mono text-emerald-400 bg-emerald-500/20 px-2.5 py-1 rounded-md border border-emerald-500/30">
                  Graphs Updated Live
                </span>
              </div>
            )}

            <TransmissionChain currentAirfareSurgePct={latestPoint.momInflationRate || 11.4} />

            {/* Advance Purchase Horizon Elasticity Curve (T+1 to T+45) */}
            <div id="lead-time-elasticity-card">
              <LeadTimeElasticityCard
                fares={liveFares}
                selectedHorizon={selectedLeadTime}
                onSelectHorizon={setSelectedLeadTime}
              />
            </div>

            <IndexChart
              data={historicalData}
              selectedLeadTime={selectedLeadTime}
              onSelectLeadTime={setSelectedLeadTime}
              isLiveScraped={hasLiveScraped}
            />

            {/* 30-Day Backtest Validation vs DGCA Monthly Benchmarks */}
            <DgcaBacktestComparison
              dailyData={dailyData}
              onOpenApiModal={() => setIsRestApiModalOpen(true)}
            />

            <DailyCPIChart data={dailyData} isLiveScraped={hasLiveScraped} />

            <div id="fuel-price-simulator">
              <FuelPriceSimulator baseJevonsIndex={latestPoint.jevonsIndex} />
            </div>

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
            <strong>VayuSuchak (वायु सूचक)</strong> • Ministry of Statistics & Programme Implementation (MoSPI)
          </div>
          <div className="text-slate-400 font-mono text-[11px]">
            National Statistical Office (NSO) Augmentation Framework • Benchmarked against <a href="https://esankhyiki.mospi.gov.in/" target="_blank" rel="noopener noreferrer" className="text-purple-400 hover:text-purple-300 underline">MoSPI eSankhyiki</a>
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

      <LiveAPIModal
        isOpen={isLiveAPIModalOpen}
        onClose={() => setIsLiveAPIModalOpen(false)}
        onIngestLiveFares={handleIngestLiveFares}
      />

      <RestApiExplorerModal
        isOpen={isRestApiModalOpen}
        onClose={() => setIsRestApiModalOpen(false)}
      />
    </div>
  );
};
export default App;
