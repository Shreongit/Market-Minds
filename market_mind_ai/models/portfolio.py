from typing import List, Optional
from pydantic import BaseModel, Field

class PortfolioPosition(BaseModel):
    ticker: str
    company_name: str = ""
    shares: float
    avg_buy_price: float
    current_price: float = 0.0
    total_value: float = 0.0
    unrealized_pnl: float = 0.0
    unrealized_pnl_pct: float = 0.0
    sector: str = "Technology"

class PortfolioSummary(BaseModel):
    name: str = "My Investment Portfolio"
    total_value: float = 0.0
    total_invested: float = 0.0
    total_pnl: float = 0.0
    total_pnl_pct: float = 0.0
    positions: List[PortfolioPosition] = []
