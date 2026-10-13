from market_mind_ai.models.strategy import StrategyConfig, StrategyRule
from market_mind_ai.services.backtester import StrategyBacktester

def test_backtester_execution():
    config = StrategyConfig(
        name="RSI Mean Reversion",
        ticker="AAPL",
        timeframe="1y",
        initial_capital=10000.0,
        entry_rules=[
            StrategyRule(indicator="RSI", operator="<", value=45.0)
        ],
        stop_loss_pct=5.0,
        take_profit_pct=10.0
    )
    
    result = StrategyBacktester.run_backtest(config)
    assert result.ticker == "AAPL"
    assert result.initial_capital == 10000.0
    assert result.final_capital > 0
    assert isinstance(result.total_return_pct, float)
    assert isinstance(result.equity_curve, list)
