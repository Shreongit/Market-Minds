import sys
import traceback
import os

# Set UTF-8 encoding for Windows terminal output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Add root directory to python path
sys.path.insert(0, os.path.abspath("."))

def run():
    print("==================================================")
    print(" Running MarketMind AI Agent & Backtest Unit Tests ")
    print("==================================================")
    
    passed = 0
    failed = 0
    
    from tests.test_agents import (
        test_technical_agent,
        test_fundamental_agent,
        test_sentiment_agent,
        test_risk_agent,
        test_portfolio_agent,
        test_scenario_agent,
        test_debate_agent,
        test_decision_agent
    )
    from tests.test_backtester import test_backtester_execution
    
    tests = [
        ("Technical Agent", test_technical_agent),
        ("Fundamental Agent", test_fundamental_agent),
        ("Sentiment Agent", test_sentiment_agent),
        ("Risk Agent", test_risk_agent),
        ("Portfolio Agent", test_portfolio_agent),
        ("Scenario Agent", test_scenario_agent),
        ("Debate Agent", test_debate_agent),
        ("Decision Agent Synthesizer", test_decision_agent),
        ("Strategy Backtester Engine", test_backtester_execution)
    ]
    
    for name, test_func in tests:
        try:
            print(f"[TESTING] {name}...", end=" ", flush=True)
            test_func()
            print("PASSED [OK]")
            passed += 1
        except Exception as e:
            print("FAILED [ERR]")
            traceback.print_exc()
            failed += 1
            
    print("--------------------------------------------------")
    print(f"Results: {passed} PASSED, {failed} FAILED out of {len(tests)} tests.")
    print("==================================================")
    
    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    run()
