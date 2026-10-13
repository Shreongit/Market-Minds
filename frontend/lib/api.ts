import axios from "axios";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export interface TickerQuote {
  ticker: string;
  company_name: string;
  price: number;
  change: number;
  change_percent: number;
  volume: number;
  market_cap?: number;
  sector: string;
  industry: string;
  day_high: number;
  day_low: number;
  fifty_two_week_high: number;
  fifty_two_week_low: number;
}

export interface DecisionOutput {
  ticker: string;
  recommendation: "BUY" | "SELL" | "HOLD";
  confidence: number;
  risk_level: string;
  suggested_holding_period: string;
  entry_range: string;
  target_price: number;
  stop_loss: number;
  technical_score: number;
  technical_why: string;
  fundamental_score: number;
  fundamental_why: string;
  sentiment_score: number;
  sentiment_why: string;
  risk_score: number;
  risk_why: string;
  overall_ai_score: number;
  reasoning: string;
  what_could_invalidate: string;
  historical_accuracy: string;
  known_limitations: string;
}

export interface BullBearDebateOutput {
  ticker: string;
  bull_case: string;
  bear_case: string;
  judge_verdict: string;
  key_catalysts: string[];
  key_downside_risks: string[];
}

export const fetchQuote = async (ticker: string) => {
  const res = await api.get(`/market/quote/${ticker}`);
  return res.data;
};

export const fetchDecision = async (ticker: string): Promise<DecisionOutput> => {
  const res = await api.get(`/analysis/decision/${ticker}`);
  return res.data;
};

export const fetchDebate = async (ticker: string): Promise<BullBearDebateOutput> => {
  const res = await api.get(`/analysis/debate/${ticker}`);
  return res.data;
};

export const fetchIndices = async () => {
  const res = await api.get("/market/indices");
  return res.data;
};

export const fetchMovers = async () => {
  const res = await api.get("/market/movers");
  return res.data;
};

export const fetchNews = async (ticker?: string) => {
  const url = ticker ? `/market/news/${ticker}` : "/market/news";
  const res = await api.get(url);
  return res.data;
};

export const postChatQuery = async (query: string) => {
  const res = await api.post("/chat/query", { query });
  return res.data;
};

export const simulateScenario = async (query: string) => {
  const res = await api.post("/simulator/scenario", { query });
  return res.data;
};
