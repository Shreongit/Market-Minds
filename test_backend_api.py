import sys
import os

sys.path.insert(0, os.path.abspath("."))

def test_fastapi_backend():
    print("==================================================")
    print(" Testing FastAPI Backend Initialization & Routes ")
    print("==================================================")
    
    from backend.main import app
    from fastapi.testclient import TestClient
    
    client = TestClient(app)
    
    # 1. Test Root
    res = client.get("/")
    assert res.status_code == 200
    assert res.json()["status"] == "online"
    print("[OK] Root endpoint online")
    
    # 2. Test Market Indices
    res = client.get("/api/v1/market/indices")
    assert res.status_code == 200
    assert len(res.json()) > 0
    print("[OK] Market Indices route operational")
    
    # 3. Test TTWO History Route (Fix Verification)
    res = client.get("/api/v1/market/history/TTWO")
    assert res.status_code == 200
    history_data = res.json()
    assert history_data["ticker"] == "TTWO"
    assert len(history_data["bars"]) > 0
    print(f"[OK] TTWO Market History Route operational ({len(history_data['bars'])} bars returned, JSON compliant)")

    # 4. Test Multi-Agent Decision Route (calls DecisionAgent)
    res = client.get("/api/v1/analysis/decision/AAPL")
    assert res.status_code == 200
    data = res.json()
    assert data["ticker"] == "AAPL"
    assert data["recommendation"] in ["BUY", "SELL", "HOLD"]
    print(f"[OK] AI Agent Decision Route operational ({data['recommendation']} call for AAPL)")
    
    print("==================================================")
    print(" ALL FASTAPI BACKEND API ROUTES PASSED SUCCESSFULLY ")
    print("==================================================")

if __name__ == "__main__":
    test_fastapi_backend()
