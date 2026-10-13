from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import backend_settings
from backend.api.auth import router as auth_router
from backend.api.market import router as market_router
from backend.api.analysis import router as analysis_router
from backend.api.portfolio import router as portfolio_router
from backend.api.strategy import router as strategy_router
from backend.api.simulator import router as simulator_router
from backend.api.chat import router as chat_router
from backend.api.export import router as export_router
from backend.api.websockets import router as ws_router

app = FastAPI(
    title=backend_settings.PROJECT_NAME,
    version=backend_settings.VERSION,
    description="MarketMind AI — Autonomous Multi-Agent Investment Copilot Backend API"
)

# Enable CORS for Next.js Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(auth_router, prefix=backend_settings.API_V1_PREFIX)
app.include_router(market_router, prefix=backend_settings.API_V1_PREFIX)
app.include_router(analysis_router, prefix=backend_settings.API_V1_PREFIX)
app.include_router(portfolio_router, prefix=backend_settings.API_V1_PREFIX)
app.include_router(strategy_router, prefix=backend_settings.API_V1_PREFIX)
app.include_router(simulator_router, prefix=backend_settings.API_V1_PREFIX)
app.include_router(chat_router, prefix=backend_settings.API_V1_PREFIX)
app.include_router(export_router, prefix=backend_settings.API_V1_PREFIX)
app.include_router(ws_router)

@app.get("/")
def root():
    return {
        "status": "online",
        "app": "MarketMind AI Backend Service",
        "version": backend_settings.VERSION,
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
