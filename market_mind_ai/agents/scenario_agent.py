from market_mind_ai.agents.base_agent import BaseAgent
from market_mind_ai.models.agent_schemas import ScenarioImpactOutput
from market_mind_ai.services.llm_orchestrator import LLMOrchestrator

class ScenarioAgent(BaseAgent):
    """
    Scenario Simulation Agent.
    Answers natural-language macro "what if" queries (e.g., Oil at $100, Fed rate hikes, inflation spikes)
    and estimates sector/portfolio impacts.
    """
    def __init__(self):
        super().__init__("Scenario Simulation Agent")

    def analyze(self, query: str, **kwargs) -> ScenarioImpactOutput:
        query_lower = query.lower()
        
        if "oil" in query_lower or "crude" in query_lower or "$100" in query_lower:
            title = "Macro Scenario: Crude Oil Spike to $100/bbl"
            impact_pct = -3.8
            vulnerable = ["AAL", "DAL", "UAL", "AMZN", "TSLA"]
            benefiting = ["XOM", "CVX", "COP", "OXY", "SLB"]
            desc = "Oil price surge increases transportation costs, depresses consumer disposable income, and compresses airline/retail margins while boosting energy producers."
            advice = "Overweight Energy sector (XOM, CVX); hedge airline and high-cost consumer discretionary exposure."
        elif "rate" in query_lower or "fed" in query_lower or "interest" in query_lower:
            title = "Macro Scenario: +50 bps Federal Reserve Interest Rate Hike"
            impact_pct = -4.5
            vulnerable = ["NVDA", "TSLA", "PLTR", "DOCU", "UPST"]
            benefiting = ["JPM", "BAC", "WFC", "BRK-B", "C"]
            desc = "Higher discount rates compress high-multiple tech valuations while expanding net interest margins for major money-center banks."
            advice = "Rotate from non-profitable hyper-growth tech into financial sector equities and short-duration fixed income."
        else:
            title = f"Macro Scenario: {query.strip()}"
            impact_pct = -2.5
            vulnerable = ["High-Beta Growth Equities", "Consumer Discretionary"]
            benefiting = ["Defensive Healthcare", "Energy", "Cash Reserves"]
            desc = f"Simulating market impact for scenario: '{query}'. Broader macroeconomic adjustments cause sector rotation and risk-off asset re-allocation."
            advice = "Maintain strict stop-loss limits and hold 10-15% cash reserves to capitalize on market dislocations."
            
        return ScenarioImpactOutput(
            scenario_title=title,
            description=desc,
            estimated_portfolio_impact_pct=impact_pct,
            vulnerable_tickers=vulnerable,
            benefiting_tickers=benefiting,
            strategic_advice=advice
        )
