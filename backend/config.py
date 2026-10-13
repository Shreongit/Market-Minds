import os
from market_mind_ai.config import settings

class BackendSettings:
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "MarketMind AI API"
    VERSION: str = "2.4.0"
    SECRET_KEY: str = settings.SECRET_KEY
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

backend_settings = BackendSettings()
