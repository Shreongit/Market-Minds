import math
from typing import List, Dict, Any, Optional
from fastapi import APIRouter
from market_mind_ai.services.market_data_service import MarketDataService
from market_mind_ai.services.news_service import NewsService
from market_mind_ai.models.market_data import TickerQuote, NewsArticle

router = APIRouter(prefix="/market", tags=["Market Data"])

def safe_float(val: Any, default: float = 0.0, ndigits: int = 2) -> float:
    if val is None:
        return default
    try:
        f = float(val)
        if math.isnan(f) or math.isinf(f):
            return default
        return round(f, ndigits)
    except (ValueError, TypeError):
        return default

def safe_int(val: Any, default: int = 0) -> int:
    if val is None:
        return default
    try:
        f = float(val)
        if math.isnan(f) or math.isinf(f):
            return default
        return int(f)
    except (ValueError, TypeError):
        return default

@router.get("/quote/{ticker}", response_model=TickerQuote)
def get_quote(ticker: str):
    return MarketDataService.get_ticker_quote(ticker)

@router.get("/history/{ticker}")
def get_history(ticker: str, period: str = "1y"):
    df = MarketDataService.get_historical_df(ticker, period=period)
    bars = []
    for idx, row in df.iterrows():
        date_str = idx.strftime("%Y-%m-%d") if hasattr(idx, "strftime") else str(idx)
        close_val = safe_float(row["Close"], 0.0)
        bars.append({
            "date": date_str,
            "open": safe_float(row["Open"], close_val),
            "high": safe_float(row["High"], close_val),
            "low": safe_float(row["Low"], close_val),
            "close": close_val,
            "volume": safe_int(row["Volume"], 0),
            "sma20": safe_float(row.get("SMA_20"), close_val),
            "sma50": safe_float(row.get("SMA_50"), close_val),
            "rsi": safe_float(row.get("RSI_14"), 50.0, ndigits=1)
        })
    return {"ticker": ticker.upper(), "period": period, "bars": bars}

@router.get("/indices")
def get_global_indices():
    return [
        {"symbol": "^NSEI", "name": "NIFTY 50", "price": "24,820.50", "change": "+145.20", "change_pct": 0.59, "category": "India"},
        {"symbol": "^BSESN", "name": "SENSEX", "price": "81,450.10", "change": "+420.80", "change_pct": 0.52, "category": "India"},
        {"symbol": "^GSPC", "name": "S&P 500", "price": "5,432.10", "change": "+24.50", "change_pct": 0.45, "category": "Global"},
        {"symbol": "^IXIC", "name": "NASDAQ 100", "price": "18,920.40", "change": "+142.10", "change_pct": 0.76, "category": "Global"},
        {"symbol": "BTC-USD", "name": "Bitcoin", "price": "$64,250.00", "change": "+1,420.00", "change_pct": 2.26, "category": "Crypto"},
        {"symbol": "ETH-USD", "name": "Ethereum", "price": "$3,450.00", "change": "+85.00", "change_pct": 2.53, "category": "Crypto"},
        {"symbol": "CL=F", "name": "Crude Oil", "price": "$78.40", "change": "-1.20", "change_pct": -1.51, "category": "Commodities"},
        {"symbol": "GC=F", "name": "Gold", "price": "$2,420.50", "change": "+14.20", "change_pct": 0.59, "category": "Commodities"}
    ]

@router.get("/movers")
def get_top_movers():
    return {
        "gainers": [
            {"ticker": "NVDA", "name": "NVIDIA Corp", "price": 128.50, "change_pct": 5.8},
            {"ticker": "TSLA", "name": "Tesla Inc", "price": 224.10, "change_pct": 4.2},
            {"ticker": "RELIANCE.NS", "name": "Reliance Industries", "price": 3120.00, "change_pct": 3.4}
        ],
        "losers": [
            {"ticker": "INTC", "name": "Intel Corp", "price": 31.20, "change_pct": -3.5},
            {"ticker": "TCS.NS", "name": "Tata Consultancy Services", "price": 4210.00, "change_pct": -1.8}
        ]
    }

@router.get("/heatmap")
def get_sector_heatmap():
    return [
        {"sector": "Technology", "change_pct": 1.8, "sentiment": "Strong Bullish"},
        {"sector": "Healthcare", "change_pct": 0.4, "sentiment": "Bullish"},
        {"sector": "Financials", "change_pct": -0.6, "sentiment": "Bearish"},
        {"sector": "Energy", "change_pct": 2.4, "sentiment": "Strong Bullish"},
        {"sector": "Consumer Disc.", "change_pct": -1.2, "sentiment": "Bearish"},
        {"sector": "Industrials", "change_pct": 0.1, "sentiment": "Neutral"}
    ]

@router.get("/news/{ticker}", response_model=List[NewsArticle])
def get_ticker_news(ticker: str):
    return NewsService.get_news_for_ticker(ticker)

@router.get("/news", response_model=List[NewsArticle])
def get_market_news():
    return NewsService.get_market_wide_news()
