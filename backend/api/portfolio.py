from fastapi import APIRouter
from typing import List
from market_mind_ai.agents.portfolio_agent import PortfolioAgent
from market_mind_ai.models.portfolio import PortfolioPosition
from market_mind_ai.models.agent_schemas import PortfolioHealthOutput

router = APIRouter(prefix="/portfolio", tags=["Portfolio Doctor"])

portfolio_agent = PortfolioAgent()

@router.post("/analyze", response_model=PortfolioHealthOutput)
def analyze_portfolio_health(positions: List[PortfolioPosition]):
    return portfolio_agent.analyze(positions)
