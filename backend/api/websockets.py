import asyncio
import json
import random
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(tags=["WebSockets"])

@router.websocket("/ws/live")
async def websocket_live_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        tickers = ["AAPL", "NVDA", "TSLA", "MSFT", "RELIANCE.NS"]
        while True:
            t = random.choice(tickers)
            price_delta = round(random.uniform(-0.8, 1.2), 2)
            alert_payload = {
                "type": "PRICE_UPDATE",
                "ticker": t,
                "delta": price_delta,
                "timestamp": str(asyncio.get_event_loop().time())
            }
            await websocket.send_text(json.dumps(alert_payload))
            await asyncio.sleep(3.0)
    except WebSocketDisconnect:
        pass
