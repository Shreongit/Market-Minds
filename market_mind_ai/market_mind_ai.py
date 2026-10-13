import reflex as rx
from market_mind_ai.ui.pages.dashboard import dashboard_page
from market_mind_ai.ui.pages.stock_analysis import stock_analysis_page
from market_mind_ai.ui.pages.portfolio_doctor import portfolio_doctor_page
from market_mind_ai.ui.pages.strategy_builder import strategy_builder_page
from market_mind_ai.ui.pages.what_if_simulator import what_if_simulator_page
from market_mind_ai.ui.pages.news_alerts import news_alerts_page
from market_mind_ai.ui.pages.market_story import market_story_page
from market_mind_ai.ui.pages.ai_chat import ai_chat_page
from market_mind_ai.ui.pages.export_hub import export_hub_page

class State(rx.State):
    """Global Application State for MarketMind AI."""
    selected_ticker: str = "AAPL"
    search_query: str = ""
    is_loading: bool = False

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="indigo",
        gray_color="slate",
        radius="medium"
    )
)

# Register Application Routes
app.add_page(dashboard_page, route="/", title="MarketMind AI — Command Center")
app.add_page(stock_analysis_page, route="/stock", title="Stock Intelligence Hub — MarketMind AI")
app.add_page(portfolio_doctor_page, route="/portfolio", title="AI Portfolio Doctor — MarketMind AI")
app.add_page(strategy_builder_page, route="/strategy", title="Strategy Lab — MarketMind AI")
app.add_page(what_if_simulator_page, route="/what-if", title="What-If Simulator — MarketMind AI")
app.add_page(news_alerts_page, route="/news", title="News Impact & Smart Alerts — MarketMind AI")
app.add_page(market_story_page, route="/story", title="Daily Market Story — MarketMind AI")
app.add_page(ai_chat_page, route="/chat", title="AI Chat Copilot — MarketMind AI")
app.add_page(export_hub_page, route="/export", title="Export Hub — MarketMind AI")
