from market_mind_ai.agents.base_agent import BaseAgent
from market_mind_ai.models.agent_schemas import TechnicalAnalysisOutput
from market_mind_ai.services.market_data_service import MarketDataService
import pandas as pd

class TechnicalAgent(BaseAgent):
    """
    Technical Analysis Agent.
    Evaluates RSI, MACD, Moving Averages (20, 50, 200), Bollinger Bands, ATR, Support & Resistance.
    Returns technical score (0-100) + breakdown.
    """
    def __init__(self):
        super().__init__("Technical Analysis Agent")

    def analyze(self, ticker: str, **kwargs) -> TechnicalAnalysisOutput:
        ticker = ticker.upper()
        df = MarketDataService.get_historical_df(ticker, period="1y")
        
        if df.empty or len(df) < 20:
            return TechnicalAnalysisOutput(
                ticker=ticker,
                score=50.0,
                trend="Neutral",
                rsi_14=50.0,
                macd_signal="Neutral",
                sma_cross="Neutral",
                bollinger_state="Mid Channel",
                support_level=100.0,
                resistance_level=120.0,
                summary_reasoning="Insufficient price history available for full technical scoring."
            )
            
        last_row = df.iloc[-1]
        prev_row = df.iloc[-2]
        
        close = float(last_row["Close"])
        rsi = float(last_row["RSI_14"])
        macd = float(last_row["MACD"])
        macd_sig = float(last_row["MACD_Signal"])
        sma20 = float(last_row["SMA_20"])
        sma50 = float(last_row["SMA_50"])
        sma200 = float(last_row["SMA_200"])
        bb_upper = float(last_row["BB_Upper"])
        bb_lower = float(last_row["BB_Lower"])
        
        # 1. RSI Score (0-100)
        # Optimal RSI for buying is 40-60 or oversold rebound < 30
        if rsi < 30:
            rsi_score = 85.0  # Oversold opportunity
        elif rsi > 70:
            rsi_score = 30.0  # Overbought risk
        else:
            rsi_score = 50.0 + (rsi - 50) * 0.8
            
        # 2. Moving Average Alignment Score
        ma_score = 50.0
        if close > sma20: ma_score += 15.0
        if close > sma50: ma_score += 15.0
        if close > sma200: ma_score += 20.0
        if sma50 > sma200: ma_score += 10.0  # Golden cross environment
        
        sma_cross = "Golden Cross Environment" if sma50 > sma200 else "Death Cross Environment"
        if close > sma200:
            sma_cross += " (Above SMA 200)"
        else:
            sma_cross += " (Below SMA 200)"
            
        # 3. MACD Signal Score
        if macd > macd_sig:
            macd_signal = "Bullish Crossover"
            macd_score = 75.0
        else:
            macd_signal = "Bearish Divergence"
            macd_score = 35.0
            
        # 4. Bollinger Bands State
        if close >= bb_upper:
            bb_state = "Upper Band Breakout"
            bb_score = 60.0
        elif close <= bb_lower:
            bb_state = "Lower Band Oversold Bounce"
            bb_score = 80.0
        else:
            bb_state = "Mid Channel Equilibrium"
            bb_score = 50.0
            
        # Support & Resistance levels (52-week min/max or rolling min/max)
        support = round(float(df["Low"].tail(60).min()), 2)
        resistance = round(float(df["High"].tail(60).max()), 2)
        
        # Weighted Technical Score
        final_score = round(0.35 * ma_score + 0.30 * macd_score + 0.20 * rsi_score + 0.15 * bb_score, 1)
        final_score = max(0.0, min(100.0, final_score))
        
        trend = "Bullish" if final_score >= 60 else ("Bearish" if final_score <= 40 else "Neutral")
        
        reasoning = (
            f"Technical momentum is {trend.lower()} with an overall score of {final_score}/100. "
            f"Price (${close:.2f}) is trading {sma_cross.lower()}. RSI 14 stands at {rsi:.1f}. "
            f"MACD shows a {macd_signal.lower()}. Key support lies at ${support:.2f} and resistance at ${resistance:.2f}."
        )
        
        return TechnicalAnalysisOutput(
            ticker=ticker,
            score=final_score,
            trend=trend,
            rsi_14=round(rsi, 1),
            macd_signal=macd_signal,
            sma_cross=sma_cross,
            bollinger_state=bb_state,
            support_level=support,
            resistance_level=resistance,
            summary_reasoning=reasoning
        )
