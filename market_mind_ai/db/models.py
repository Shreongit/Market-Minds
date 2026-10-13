import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from market_mind_ai.db.base import Base

class StockModel(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(20), unique=True, index=True, nullable=False)
    name = Column(String(200))
    sector = Column(String(100))
    industry = Column(String(100))
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class PortfolioModel(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), default="My Portfolio")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    positions = relationship("PositionModel", back_populates="portfolio", cascade="all, delete-orphan")

class PositionModel(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"), nullable=False)
    ticker = Column(String(20), nullable=False)
    shares = Column(Float, nullable=False)
    buy_price = Column(Float, nullable=False)
    sector = Column(String(100), default="Technology")

    portfolio = relationship("PortfolioModel", back_populates="positions")

class AlertModel(Base):
    __tablename__ = "smart_alerts"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(20), nullable=False)
    alert_type = Column(String(50), nullable=False)  # Bullish Breakout, Institutional Buying, Unusual Volume, Momentum Shift
    confidence = Column(Float, nullable=False)
    impact_level = Column(String(20), nullable=False)  # LOW, MEDIUM, HIGH
    title = Column(String(200), nullable=False)
    reasoning = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class DailyMarketStoryModel(Base):
    __tablename__ = "daily_market_stories"

    id = Column(Integer, primary_key=True, index=True)
    date_str = Column(String(20), index=True, nullable=False)
    headline = Column(String(300), nullable=False)
    summary_what = Column(Text, nullable=False)
    summary_why = Column(Text, nullable=False)
    what_to_watch_tomorrow = Column(Text, nullable=False)
    fear_greed_score = Column(Float, default=50.0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
