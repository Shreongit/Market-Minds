from market_mind_ai.agents.base_agent import BaseAgent
from market_mind_ai.models.agent_schemas import FundamentalAnalysisOutput
from market_mind_ai.services.market_data_service import MarketDataService

class FundamentalAgent(BaseAgent):
    """
    Fundamental Analysis Agent.
    Evaluates P/E ratio, P/B ratio, Debt-to-Equity, Revenue Growth (YoY), Profit Margins, ROE, and Fair Value DCF.
    Returns fundamental score (0-100) + breakdown.
    """
    def __init__(self):
        super().__init__("Fundamental Analysis Agent")

    def analyze(self, ticker: str, **kwargs) -> FundamentalAnalysisOutput:
        ticker = ticker.upper()
        fund = MarketDataService.get_fundamental_metrics(ticker)
        quote = MarketDataService.get_ticker_quote(ticker)
        
        pe = fund.get("pe_ratio")
        pb = fund.get("pb_ratio")
        ev_ebitda = fund.get("ev_to_ebitda")
        debt_eq = fund.get("debt_to_equity")
        rev_growth = fund.get("revenue_growth_yoy")
        net_margin = fund.get("net_margin")
        roe = fund.get("roe")
        fair_value = fund.get("fair_value_estimate")
        
        current_price = quote.price
        
        # Scoring Logic
        pe_score = 50.0
        if pe:
            if pe < 15: pe_score = 85.0
            elif pe < 25: pe_score = 70.0
            elif pe < 40: pe_score = 50.0
            else: pe_score = 30.0
            
        growth_score = 50.0
        if rev_growth:
            if rev_growth > 20: growth_score = 90.0
            elif rev_growth > 10: growth_score = 75.0
            elif rev_growth > 0: growth_score = 55.0
            else: growth_score = 25.0
            
        quality_score = 50.0
        if roe and net_margin:
            quality_score = min(100.0, (roe * 1.5) + (net_margin * 1.2))
            
        fair_value_score = 50.0
        if fair_value and current_price > 0:
            upside = ((fair_value - current_price) / current_price) * 100
            if upside > 20:
                fair_value_score = 90.0
                val_status = "Undervalued"
            elif upside < -15:
                fair_value_score = 30.0
                val_status = "Overvalued"
            else:
                fair_value_score = 60.0
                val_status = "Fairly Valued"
        else:
            val_status = "Fairly Valued"
            
        final_score = round(0.30 * pe_score + 0.30 * growth_score + 0.20 * quality_score + 0.20 * fair_value_score, 1)
        final_score = max(0.0, min(100.0, final_score))
        
        reasoning = (
            f"Fundamental quality score is {final_score}/100 ({val_status}). "
            f"P/E ratio stands at {pe if pe else 'N/A'}, YoY Revenue Growth at {rev_growth:.1f}%, "
            f"Net Margin at {net_margin:.1f}%, and ROE at {roe:.1f}%. "
            f"Fair value estimated at ${fair_value:.2f} vs current market price of ${current_price:.2f}."
        )
        
        return FundamentalAnalysisOutput(
            ticker=ticker,
            score=final_score,
            pe_ratio=pe,
            pb_ratio=pb,
            ev_to_ebitda=ev_ebitda,
            debt_to_equity=debt_eq,
            revenue_growth_yoy=rev_growth,
            net_margin=net_margin,
            roe=roe,
            fair_value_estimate=fair_value,
            valuation_status=val_status,
            summary_reasoning=reasoning
        )
