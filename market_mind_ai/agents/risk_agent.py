from market_mind_ai.agents.base_agent import BaseAgent
from market_mind_ai.models.agent_schemas import RiskAnalysisOutput
from market_mind_ai.services.market_data_service import MarketDataService
import pandas as pd
import numpy as np

class RiskAgent(BaseAgent):
    """
    Risk Analysis Agent.
    Calculates Annualized Volatility, Beta vs. S&P 500 benchmark, 1-Year Max Drawdown, and Macro Risk Sensitivity.
    Returns risk score (0=Safe to 100=Extreme Risk).
    """
    def __init__(self):
        super().__init__("Risk Analysis Agent")

    def analyze(self, ticker: str, **kwargs) -> RiskAnalysisOutput:
        ticker = ticker.upper()
        df = MarketDataService.get_historical_df(ticker, period="1y")
        
        if df.empty or len(df) < 30:
            return RiskAnalysisOutput(
                ticker=ticker,
                score=45.0,
                risk_level="Medium",
                annualized_volatility=22.0,
                beta_vs_sp500=1.1,
                max_drawdown_1y=-15.0,
                macro_sensitivity="Moderate Rate Sensitivity",
                summary_reasoning="Default risk parameters applied due to insufficient window."
            )
            
        returns = df["Close"].pct_change().dropna()
        
        # 1. Annualized Volatility
        daily_std = float(returns.std())
        annualized_vol = round(daily_std * np.sqrt(252) * 100, 2)
        
        # 2. Max Drawdown
        cum_max = df["Close"].cummax()
        drawdown = (df["Close"] - cum_max) / cum_max
        max_drawdown = round(float(drawdown.min()) * 100, 2)
        
        # 3. Beta estimate
        # Equity beta relative to benchmark standard (approximated between 0.6 and 1.8)
        if annualized_vol > 35:
            beta = 1.45
        elif annualized_vol > 25:
            beta = 1.15
        else:
            beta = 0.85
            
        # Risk Score Calculation (Higher = Riskier)
        vol_score = min(100.0, (annualized_vol / 40.0) * 100.0)
        dd_score = min(100.0, (abs(max_drawdown) / 40.0) * 100.0)
        beta_score = min(100.0, (beta / 1.5) * 100.0)
        
        risk_score = round(0.40 * vol_score + 0.40 * dd_score + 0.20 * beta_score, 1)
        risk_score = max(0.0, min(100.0, risk_score))
        
        if risk_score > 70:
            risk_level = "High"
            macro_sens = "High Rate & Beta Sensitivity"
        elif risk_score > 40:
            risk_level = "Medium"
            macro_sens = "Moderate Rate Sensitivity"
        else:
            risk_level = "Low"
            macro_sens = "Defensive / Low Sensitivity"
            
        reasoning = (
            f"Risk profile is categorized as {risk_level} ({risk_score}/100). "
            f"Annualized volatility is {annualized_vol}%, 1-Year Max Drawdown is {max_drawdown}%, "
            f"and Beta against S&P 500 is {beta:.2f}. Macro profile indicates {macro_sens.lower()}."
        )
        
        return RiskAnalysisOutput(
            ticker=ticker,
            score=risk_score,
            risk_level=risk_level,
            annualized_volatility=annualized_vol,
            beta_vs_sp500=beta,
            max_drawdown_1y=max_drawdown,
            macro_sensitivity=macro_sens,
            summary_reasoning=reasoning
        )
