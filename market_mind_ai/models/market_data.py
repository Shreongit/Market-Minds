from typing import List, Optional
from pydantic import BaseModel

class TickerQuote(BaseModel):
    ticker: str
    company_name: str
    price: float
    change: float
    change_percent: float
    volume: int
    market_cap: Optional[float] = None
    sector: str = "Unknown"
    industry: str = "Unknown"
    day_high: float
    day_low: float
    fifty_two_week_high: float
    fifty_two_week_low: float

class OHLCVBar(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int

class StockHistoricalData(BaseModel):
    ticker: str
    period: str
    bars: List[OHLCVBar]

class NewsArticle(BaseModel):
    title: str
    url: str
    source: str
    published_at: str
    summary: str
    sentiment_score: float  # -1.0 to +1.0
    sentiment_label: str  # POSITIVE, NEGATIVE, NEUTRAL
    impact_level: str  # LOW, MEDIUM, HIGH
    related_tickers: List[str] = []
    impact_explanation: str = ""
