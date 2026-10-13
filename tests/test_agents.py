from market_mind_ai.agents.technical_agent import TechnicalAgent
from market_mind_ai.agents.fundamental_agent import FundamentalAgent
from market_mind_ai.agents.sentiment_agent import SentimentAgent
from market_mind_ai.agents.risk_agent import RiskAgent
from market_mind_ai.agents.portfolio_agent import PortfolioAgent
from market_mind_ai.agents.scenario_agent import ScenarioAgent
from market_mind_ai.agents.debate_agent import DebateAgent
from market_mind_ai.agents.decision_agent import DecisionAgent
from market_mind_ai.models.portfolio import PortfolioPosition

def test_technical_agent():
    agent = TechnicalAgent()
    res = agent.analyze("AAPL")
    assert res.ticker == "AAPL"
    assert 0 <= res.score <= 100
    assert res.trend in ["Bullish", "Bearish", "Neutral"]

def test_fundamental_agent():
    agent = FundamentalAgent()
    res = agent.analyze("MSFT")
    assert res.ticker == "MSFT"
    assert 0 <= res.score <= 100
    assert res.valuation_status in ["Undervalued", "Fairly Valued", "Overvalued"]

def test_sentiment_agent():
    agent = SentimentAgent()
    res = agent.analyze("NVDA")
    assert res.ticker == "NVDA"
    assert 0 <= res.score <= 100

def test_risk_agent():
    agent = RiskAgent()
    res = agent.analyze("GOOGL")
    assert res.ticker == "GOOGL"
    assert 0 <= res.score <= 100
    assert res.risk_level in ["Low", "Medium", "High", "Critical"]

def test_portfolio_agent():
    agent = PortfolioAgent()
    positions = [
        PortfolioPosition(ticker="AAPL", shares=10, avg_buy_price=150.0, current_price=180.0, total_value=1800.0, sector="Technology"),
        PortfolioPosition(ticker="JPM", shares=5, avg_buy_price=140.0, current_price=160.0, total_value=800.0, sector="Financials")
    ]
    res = agent.analyze(positions)
    assert 0 <= res.health_score <= 100
    assert len(res.actionable_suggestions) > 0

def test_scenario_agent():
    agent = ScenarioAgent()
    res = agent.analyze("What if crude oil hits $100?")
    assert "Crude Oil" in res.scenario_title
    assert len(res.vulnerable_tickers) > 0

def test_debate_agent():
    agent = DebateAgent()
    res = agent.analyze("TSLA")
    assert res.ticker == "TSLA"
    assert len(res.bull_case) > 0
    assert len(res.bear_case) > 0

def test_decision_agent():
    agent = DecisionAgent()
    res = agent.analyze("AAPL")
    assert res.ticker == "AAPL"
    assert res.recommendation in ["BUY", "SELL", "HOLD"]
    assert 0 <= res.confidence <= 100
    assert res.target_price > 0
    assert res.stop_loss > 0
    assert len(res.reasoning) > 0
    assert len(res.what_could_invalidate) > 0
