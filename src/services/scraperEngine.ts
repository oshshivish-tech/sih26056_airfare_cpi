import { FlightFare, ScraperSourceStatus } from '../types';
import { generateLiveScrapedFares, MOCK_SCRAPER_SOURCES } from '../data/mockData';

export interface ScrapingLogEntry {
  id: string;
  timestamp: string;
  source: string;
  level: 'INFO' | 'SUCCESS' | 'WARN' | 'ERROR';
  message: string;
  recordsCount?: number;
  latencyMs?: number;
}

export type ScrapingEventListener = (log: ScrapingLogEntry, fares?: FlightFare[]) => void;

export class ScraperOrchestrator {
  private sourcesStatus: ScraperSourceStatus[] = [...MOCK_SCRAPER_SOURCES];
  private listeners: ScrapingEventListener[] = [];
  private isRunning: boolean = false;

  public subscribe(listener: ScrapingEventListener) {
    this.listeners.push(listener);
    return () => {
      this.listeners = this.listeners.filter(l => l !== listener);
    };
  }

  private emit(log: ScrapingLogEntry, fares?: FlightFare[]) {
    this.listeners.forEach(l => l(log, fares));
  }

  public getSourceStatuses(): ScraperSourceStatus[] {
    return this.sourcesStatus;
  }

  /**
   * Executes a live simulated scraping job across target portals
   */
  public async executeLiveScrapeJob(): Promise<{ newFares: FlightFare[]; logs: ScrapingLogEntry[] }> {
    if (this.isRunning) {
      throw new Error('Scraping job already in progress.');
    }

    this.isRunning = true;
    const logs: ScrapingLogEntry[] = [];
    const now = () => new Date().toLocaleTimeString('en-US', { hour12: false });

    // Initial log
    const initLog: ScrapingLogEntry = {
      id: `log-${Date.now()}-0`,
      timestamp: now(),
      source: 'ORCHESTRATOR',
      level: 'INFO',
      message: 'Initializing multi-threaded scraping job across 5 target portals & 12 domestic corridors...'
    };
    logs.push(initLog);
    this.emit(initLog);

    await new Promise(r => setTimeout(r, 600));

    // Scrape Source 1: IndiGo Direct
    const indigoLog: ScrapingLogEntry = {
      id: `log-${Date.now()}-1`,
      timestamp: now(),
      source: 'goindigo.in',
      level: 'SUCCESS',
      message: 'Bypassed Cloudflare TLS fingerprint. Extracted 4,200 fares via Stealth Playwright headless cluster.',
      recordsCount: 4200,
      latencyMs: 310
    };
    logs.push(indigoLog);
    this.emit(indigoLog);

    await new Promise(r => setTimeout(r, 800));

    // Scrape Source 2: MakeMyTrip OTA
    const mmtLog: ScrapingLogEntry = {
      id: `log-${Date.now()}-2`,
      timestamp: now(),
      source: 'makemytrip.com',
      level: 'SUCCESS',
      message: 'Intercepted JSON XHR payload `/api/v2/search/flights`. Extracted 7,800 fares.',
      recordsCount: 7800,
      latencyMs: 240
    };
    logs.push(mmtLog);
    this.emit(mmtLog);

    await new Promise(r => setTimeout(r, 700));

    // Scrape Source 3: Air India Direct
    const aiLog: ScrapingLogEntry = {
      id: `log-${Date.now()}-3`,
      timestamp: now(),
      source: 'airindia.com',
      level: 'SUCCESS',
      message: 'Extracted 3,600 base fares with disaggregated fuel surcharges & airport fees.',
      recordsCount: 3600,
      latencyMs: 390
    };
    logs.push(aiLog);
    this.emit(aiLog);

    await new Promise(r => setTimeout(r, 500));

    // Scrape Source 4: EaseMyTrip OTA
    const emtLog: ScrapingLogEntry = {
      id: `log-${Date.now()}-4`,
      timestamp: now(),
      source: 'easemytrip.com',
      level: 'SUCCESS',
      message: 'HTML DOM resilient parser successfully extracted 5,100 quotes.',
      recordsCount: 5100,
      latencyMs: 210
    };
    logs.push(emtLog);
    this.emit(emtLog);

    await new Promise(r => setTimeout(r, 600));

    // Generate new scraped fares
    const newFares = generateLiveScrapedFares();

    // Final Completion Log
    const doneLog: ScrapingLogEntry = {
      id: `log-${Date.now()}-5`,
      timestamp: now(),
      source: 'ORCHESTRATOR',
      level: 'SUCCESS',
      message: `Scraping job completed cleanly! Total ${newFares.length} verified quotes ingested into TimescaleDB pipeline.`,
      recordsCount: newFares.length,
      latencyMs: 1750
    };
    logs.push(doneLog);
    this.emit(doneLog, newFares);

    this.isRunning = false;
    return { newFares, logs };
  }
}

export const scraperOrchestrator = new ScraperOrchestrator();
