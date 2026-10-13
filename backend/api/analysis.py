from fastapi import APIRouter
from market_mind_ai.agents.decision_agent import DecisionAgent
from market_mind_ai.agents.debate_agent import DebateAgent
from market_mind_ai.agents.technical_agent import TechnicalAgent
from market_mind_ai.agents.fundamental_agent import FundamentalAgent
from market_mind_ai.agents.sentiment_agent import SentimentAgent
from market_mind_ai.agents.risk_agent import RiskAgent
from market_mind_ai.models.agent_schemas import DecisionOutput, BullBearDebateOutput

router = APIRouter(prefix="/analysis", tags=["AI Agent Analysis Engine"])

# Initialize preserved existing AI agents
decision_agent = DecisionAgent()
debate_agent = DebateAgent()
tech_agent = TechnicalAgent()
fund_agent = FundamentalAgent()
sent_agent = SentimentAgent()
risk_agent = RiskAgent()

@router.get("/decision/{ticker}", response_model=DecisionOutput)
def get_full_ai_decision(ticker: str):
    """
    Executes the multi-agent decision synthesizer engine for a given ticker.
    Combines Technical, Fundamental, Sentiment, and Risk agent outputs.
    """
    return decision_agent.analyze(ticker)

@router.get("/debate/{ticker}", response_model=BullBearDebateOutput)
def get_bull_vs_bear_debate(ticker: str):
    """
    Runs Bull AI vs Bear AI persona debate and Judge verdict.
    """
    return debate_agent.analyze(ticker)

@router.get("/technical/{ticker}")
def get_technical_breakdown(ticker: str):
    return tech_agent.analyze(ticker)

@router.get("/fundamental/{ticker}")
def get_fundamental_breakdown(ticker: str):
    return fund_agent.analyze(ticker)

@router.get("/sentiment/{ticker}")
def get_sentiment_breakdown(ticker: str):
    return sent_agent.analyze(ticker)

@router.get("/risk/{ticker}")
def get_risk_breakdown(ticker: str):
    return risk_agent.analyze(ticker)
