from typing import List, Optional
from pydantic import BaseModel, Field

class StrategyRule(BaseModel):
    indicator: str  # "RSI", "MACD", "SMA_20_50", "PRICE_SMA_200"
    operator: str  # "<", ">", "CROSS_ABOVE", "CROSS_BELOW"
    value: float
    logic: str = "AND"  # "AND", "OR"

class StrategyConfig(BaseModel):
    name: str
    ticker: str = "AAPL"
    timeframe: str = "1y"  # "6m", "1y", "2y", "5y"
    initial_capital: float = 10000.0
    entry_rules: List[StrategyRule]
    stop_loss_pct: float = 5.0
    take_profit_pct: float = 15.0

class BacktestTrade(BaseModel):
    entry_date: str
    exit_date: str
    entry_price: float
    exit_price: float
    return_pct: float
    profit_loss: float
    reason: str  # "Take Profit", "Stop Loss", "Signal Exit"

class BacktestResult(BaseModel):
    strategy_name: str
    ticker: str
    period: str
    initial_capital: float
    final_capital: float
    total_return_pct: float
    benchmark_return_pct: float  # S&P 500 return over same period
    cagr: float
    sharpe_ratio: float
    max_drawdown_pct: float
    win_rate_pct: float
    total_trades: int
    winning_trades: int
    losing_trades: int
    profit_factor: float
    trades: List[BacktestTrade] = []
    equity_curve: List[dict] = []  # List of {"date": str, "equity": float, "benchmark": float}
