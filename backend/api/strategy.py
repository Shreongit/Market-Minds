from fastapi import APIRouter
from market_mind_ai.models.strategy import StrategyConfig, BacktestResult
from market_mind_ai.services.backtester import StrategyBacktester

router = APIRouter(prefix="/strategy", tags=["Strategy & Backtesting Lab"])

@router.post("/backtest", response_model=BacktestResult)
def run_strategy_backtest(config: StrategyConfig):
    return StrategyBacktester.run_backtest(config)
