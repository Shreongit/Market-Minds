from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

# --- Individual Agent Output Schemas ---

class TechnicalAnalysisOutput(BaseModel):
    ticker: str
    score: float = Field(..., ge=0, le=100, description="Technical score from 0 to 100")
    trend: str = Field(..., description="Bullish, Bearish, or Neutral")
    rsi_14: float
    macd_signal: str
    sma_cross: str  # e.g., "Golden Cross", "Death Cross", "Above SMA 200", "Below SMA 200"
    bollinger_state: str  # "Upper Band Breakout", "Lower Band Bounce", "Mid Channel"
    support_level: float
    resistance_level: float
    summary_reasoning: str

class FundamentalAnalysisOutput(BaseModel):
    ticker: str
    score: float = Field(..., ge=0, le=100, description="Fundamental score from 0 to 100")
    pe_ratio: Optional[float] = None
    pb_ratio: Optional[float] = None
    ev_to_ebitda: Optional[float] = None
    debt_to_equity: Optional[float] = None
    revenue_growth_yoy: Optional[float] = None
    net_margin: Optional[float] = None
    roe: Optional[float] = None
    fair_value_estimate: Optional[float] = None
    valuation_status: str  # "Undervalued", "Fairly Valued", "Overvalued"
    summary_reasoning: str

class SentimentAnalysisOutput(BaseModel):
    ticker: str
    score: float = Field(..., ge=0, le=100, description="Sentiment score from 0 to 100")
    sentiment_label: str  # "Strongly Bullish", "Bullish", "Neutral", "Bearish", "Strongly Bearish"
    news_sentiment_score: float
    social_noise_level: str  # "Low", "Medium", "High"
    fear_and_greed_index: float  # 0-100
    top_headlines_summary: List[str] = []
    summary_reasoning: str

class RiskAnalysisOutput(BaseModel):
    ticker: str
    score: float = Field(..., ge=0, le=100, description="Risk score from 0 (Safe) to 100 (Extreme Risk)")
    risk_level: str  # "Low", "Medium", "High", "Critical"
    annualized_volatility: float
    beta_vs_sp500: float
    max_drawdown_1y: float
    macro_sensitivity: str  # "High Rate Sensitivity", "Oil Price Vulnerable", etc.
    summary_reasoning: str

class PortfolioHealthOutput(BaseModel):
    health_score: float = Field(..., ge=0, le=100)
    diversification_index: float  # 0 to 100
    top_sector_concentration: str
    max_correlated_pair: str
    expected_annual_return: float
    portfolio_beta: float
    actionable_suggestions: List[str]

class ScenarioImpactOutput(BaseModel):
    scenario_title: str
    description: str
    estimated_portfolio_impact_pct: float
    vulnerable_tickers: List[str]
    benefiting_tickers: List[str]
    strategic_advice: str

class BullBearDebateOutput(BaseModel):
    ticker: str
    bull_case: str
    bear_case: str
    judge_verdict: str
    key_catalysts: List[str]
    key_downside_risks: List[str]

# --- Decision Agent Synthesizer Output Schema ---

class DecisionOutput(BaseModel):
    ticker: str
    recommendation: str = Field(..., description="BUY, SELL, or HOLD")
    confidence: float = Field(..., ge=0, le=100, description="Confidence percentage 0-100%")
    risk_level: str = Field(..., description="Low, Medium, High")
    suggested_holding_period: str  # e.g., "3-6 Months", "1-2 Years", "Short-term Tactical (1-4 weeks)"
    entry_range: str  # e.g., "$175.00 - $180.00"
    target_price: float
    stop_loss: float
    
    # Sub-agent Scores & Why
    technical_score: float = Field(..., ge=0, le=100)
    technical_why: str
    fundamental_score: float = Field(..., ge=0, le=100)
    fundamental_why: str
    sentiment_score: float = Field(..., ge=0, le=100)
    sentiment_why: str
    risk_score: float = Field(..., ge=0, le=100)
    risk_why: str
    overall_ai_score: float = Field(..., ge=0, le=100)
    
    # Narrative & Transparency
    reasoning: str  # Plain-English synthesis narrative
    what_could_invalidate: str  # Specific triggers that break the thesis
    historical_accuracy: str  # Historical performance of similar agent calls
    known_limitations: str  # Stated limitations of current analysis
