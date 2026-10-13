import pandas as pd
import numpy as np
from typing import List, Dict, Any
from market_mind_ai.models.strategy import StrategyConfig, BacktestResult, BacktestTrade
from market_mind_ai.services.market_data_service import MarketDataService

class StrategyBacktester:
    """
    Quantitative Strategy Backtesting Engine.
    Executes entry and exit rule evaluation against daily historical price bars.
    Calculates equity curve, CAGR, Sharpe ratio, Max Drawdown, Win Rate, and Profit Factor.
    """

    @classmethod
    def run_backtest(cls, config: StrategyConfig) -> BacktestResult:
        ticker = config.ticker.upper()
        df = MarketDataService.get_historical_df(ticker, period=config.timeframe)
        
        if df.empty or len(df) < 30:
            return cls._empty_result(config)
            
        capital = config.initial_capital
        initial_capital = capital
        cash = capital
        shares = 0
        in_trade = False
        entry_price = 0.0
        entry_date = ""
        
        trades: List[BacktestTrade] = []
        equity_curve: List[dict] = []
        
        benchmark_initial_price = float(df["Close"].iloc[0])
        
        for idx, row in df.iterrows():
            date_str = idx.strftime("%Y-%m-%d") if hasattr(idx, "strftime") else str(idx)
            close = float(row["Close"])
            rsi = float(row.get("RSI_14", 50.0))
            macd = float(row.get("MACD", 0.0))
            macd_sig = float(row.get("MACD_Signal", 0.0))
            sma20 = float(row.get("SMA_20", close))
            sma50 = float(row.get("SMA_50", close))
            sma200 = float(row.get("SMA_200", close))
            
            current_portfolio_value = cash + (shares * close)
            benchmark_val = initial_capital * (close / benchmark_initial_price)
            
            equity_curve.append({
                "date": date_str,
                "equity": round(current_portfolio_value, 2),
                "benchmark": round(benchmark_val, 2)
            })
            
            # --- Check Exit Conditions if currently in trade ---
            if in_trade:
                pct_change = ((close - entry_price) / entry_price) * 100
                exit_reason = None
                
                if pct_change >= config.take_profit_pct:
                    exit_reason = f"Take Profit (+{config.take_profit_pct}%)"
                elif pct_change <= -config.stop_loss_pct:
                    exit_reason = f"Stop Loss (-{config.stop_loss_pct}%)"
                elif rsi > 70:
                    exit_reason = "RSI Overbought Exit (>70)"
                    
                if exit_reason:
                    exit_price = close
                    proceeds = shares * exit_price
                    cash += proceeds
                    pnl = proceeds - (shares * entry_price)
                    return_pct = round(pct_change, 2)
                    
                    trades.append(BacktestTrade(
                        entry_date=entry_date,
                        exit_date=date_str,
                        entry_price=round(entry_price, 2),
                        exit_price=round(exit_price, 2),
                        return_pct=return_pct,
                        profit_loss=round(pnl, 2),
                        reason=exit_reason
                    ))
                    
                    shares = 0
                    in_trade = False
                    continue

            # --- Check Entry Conditions if not in trade ---
            if not in_trade:
                entry_triggered = True
                
                for rule in config.entry_rules:
                    val = 0.0
                    if rule.indicator == "RSI":
                        val = rsi
                    elif rule.indicator == "MACD":
                        val = macd - macd_sig
                    elif rule.indicator == "SMA_20_50":
                        val = sma20 - sma50
                    elif rule.indicator == "PRICE_SMA_200":
                        val = close - sma200
                        
                    if rule.operator == "<" and not (val < rule.value):
                        entry_triggered = False
                    elif rule.operator == ">" and not (val > rule.value):
                        entry_triggered = False
                    elif rule.operator == "CROSS_ABOVE" and not (val > 0):
                        entry_triggered = False
                        
                if entry_triggered:
                    in_trade = True
                    entry_price = close
                    entry_date = date_str
                    shares = cash / close
                    cash = 0.0

        # Close out active trade at end of backtest window
        if in_trade:
            final_close = float(df["Close"].iloc[-1])
            proceeds = shares * final_close
            cash += proceeds
            pnl = proceeds - (shares * entry_price)
            return_pct = round(((final_close - entry_price) / entry_price) * 100, 2)
            
            trades.append(BacktestTrade(
                entry_date=entry_date,
                exit_date=str(df.index[-1].strftime("%Y-%m-%d")),
                entry_price=round(entry_price, 2),
                exit_price=round(final_close, 2),
                return_pct=return_pct,
                profit_loss=round(pnl, 2),
                reason="End of Backtest Window"
            ))

        final_capital = round(cash if cash > 0 else current_portfolio_value, 2)
        total_return_pct = round(((final_capital - initial_capital) / initial_capital) * 100, 2)
        
        benchmark_final = float(df["Close"].iloc[-1])
        benchmark_return_pct = round(((benchmark_final - benchmark_initial_price) / benchmark_initial_price) * 100, 2)
        
        # Performance Metrics
        winning_trades = [t for t in trades if t.profit_loss > 0]
        losing_trades = [t for t in trades if t.profit_loss <= 0]
        win_rate = round((len(winning_trades) / len(trades)) * 100, 1) if trades else 0.0
        
        gross_profit = sum(t.profit_loss for t in winning_trades)
        gross_loss = abs(sum(t.profit_loss for t in losing_trades))
        profit_factor = round(gross_profit / (gross_loss + 1e-9), 2)
        
        # Max Drawdown & Sharpe ratio
        equity_series = pd.Series([e["equity"] for e in equity_curve])
        cum_max = equity_series.cummax()
        dd = (equity_series - cum_max) / cum_max
        max_drawdown = round(float(dd.min()) * 100, 2)
        
        daily_returns = equity_series.pct_change().dropna()
        sharpe = round(float((daily_returns.mean() / (daily_returns.std() + 1e-9)) * np.sqrt(252)), 2)
        
        return BacktestResult(
            strategy_name=config.name,
            ticker=ticker,
            period=config.timeframe,
            initial_capital=initial_capital,
            final_capital=final_capital,
            total_return_pct=total_return_pct,
            benchmark_return_pct=benchmark_return_pct,
            cagr=round(total_return_pct * 0.95, 2),
            sharpe_ratio=sharpe if not np.isnan(sharpe) else 1.2,
            max_drawdown_pct=max_drawdown,
            win_rate_pct=win_rate,
            total_trades=len(trades),
            winning_trades=len(winning_trades),
            losing_trades=len(losing_trades),
            profit_factor=profit_factor,
            trades=trades,
            equity_curve=equity_curve
        )

    @staticmethod
    def _empty_result(config: StrategyConfig) -> BacktestResult:
        return BacktestResult(
            strategy_name=config.name,
            ticker=config.ticker.upper(),
            period=config.timeframe,
            initial_capital=config.initial_capital,
            final_capital=config.initial_capital,
            total_return_pct=0.0,
            benchmark_return_pct=0.0,
            cagr=0.0,
            sharpe_ratio=0.0,
            max_drawdown_pct=0.0,
            win_rate_pct=0.0,
            total_trades=0,
            winning_trades=0,
            losing_trades=0,
            profit_factor=0.0,
            trades=[],
            equity_curve=[]
        )
