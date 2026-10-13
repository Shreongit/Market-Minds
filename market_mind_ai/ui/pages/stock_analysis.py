import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE
from market_mind_ai.ui.components.navbar import navbar_component
from market_mind_ai.ui.components.sidebar import sidebar_component
from market_mind_ai.ui.components.decision_card import decision_card_component
from market_mind_ai.ui.components.chart_widget import chart_widget_component
from market_mind_ai.ui.components.debate_modal import debate_card_component
from market_mind_ai.ui.components.indicator_tooltip import indicator_tooltip_component

def stock_analysis_page() -> rx.Component:
    return rx.box(
        navbar_component("Stock"),
        rx.hstack(
            sidebar_component("Stock"),
            rx.box(
                rx.vstack(
                    # Search Header
                    rx.hstack(
                        rx.box(
                            rx.hstack(
                                rx.icon(tag="search", size=18, color="#94A3B8"),
                                rx.input(
                                    placeholder="Enter Ticker (e.g. AAPL, NVDA, TSLA, MSFT)...",
                                    variant="unstyled",
                                    color="white",
                                    font_weight="600",
                                    font_size="1rem",
                                    width="320px"
                                ),
                                align_items="center", spacing="2"
                            ),
                            background="rgba(30, 41, 59, 0.8)",
                            padding_x="1rem", padding_y="0.6rem",
                            border_radius="12px",
                            border="1px solid rgba(255, 255, 255, 0.1)"
                        ),
                        rx.button("Analyze Stock", icon="sparkles", color_scheme="indigo", size="3", border_radius="12px"),
                        rx.spacer(),
                        # Learning Mode Explainers Quick Menu
                        rx.hstack(
                            indicator_tooltip_component("RSI"),
                            indicator_tooltip_component("MACD"),
                            indicator_tooltip_component("PE"),
                            indicator_tooltip_component("BETA"),
                            spacing="3", align_items="center"
                        ),
                        width="100%", align_items="center"
                    ),
                    
                    # Chart & Stock Overview Header
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.vstack(
                                    rx.hstack(
                                        rx.heading("Apple Inc. (AAPL)", font_size="1.8rem", color="white", font_weight="900"),
                                        rx.badge("NASDAQ", color_scheme="purple", padding_x="0.6rem"),
                                        rx.badge("Technology", color_scheme="indigo", padding_x="0.6rem"),
                                        align_items="center", spacing="3"
                                    ),
                                    rx.hstack(
                                        rx.text("$224.50", font_size="2.2rem", font_weight="900", color="white"),
                                        rx.text("+$3.40 (+1.54%)", font_size="1.1rem", font_weight="700", color="#34D399"),
                                        align_items="baseline", spacing="3"
                                    ),
                                    align_items="start", spacing="1"
                                ),
                                rx.spacer(),
                                align_items="start", width="100%"
                            ),
                            chart_widget_component("AAPL"),
                            spacing="3", align_items="stretch"
                        ),
                        style=GLASS_CARD_STYLE, width="100%", margin_y="1rem"
                    ),
                    
                    # Full Decision Output Card
                    decision_card_component(
                        ticker="AAPL",
                        recommendation="BUY",
                        confidence=86.0,
                        target_price=250.00,
                        stop_loss=210.00,
                        entry_range="$220.00 - $225.00",
                        holding_period="3-6 Months",
                        risk_level="Medium",
                        overall_score=78.5,
                        tech_score=76.0,
                        tech_why="Trading above SMA 20/50/200 with RSI at 58.2 and positive MACD histogram.",
                        fund_score=82.0,
                        fund_why="P/E at 28.5, YoY revenue growth +8.4%, Net margin 26.2%, and ROE 145%.",
                        sent_score=75.0,
                        sent_why="Positive news sentiment rating (+0.45) on iPhone 16 demand and AI Services expansion.",
                        risk_score=35.0,
                        risk_why="Annualized volatility 18.2%, Beta 1.02 vs S&P 500, Max drawdown -12.4%.",
                        reasoning="MarketMind AI Research Desk issues a BUY call for AAPL with 86% confidence. The stock displays robust fundamental cash flow generation paired with constructive price momentum above key 50-day moving averages.",
                        invalidation="1) Daily closing price below $210.00.\n2) Services revenue deceleration under +5% YoY.\n3) Broader macroeconomic valuation contraction across tech sector.",
                        limitations="Analysis excludes unannounced regulatory antitrust rulings or immediate geopolitical supply chain disruptions."
                    ),
                    
                    # Bull vs Bear Debate Section
                    rx.box(
                        debate_card_component(
                            ticker="AAPL",
                            bull_case="BULL THESIS: Apple's Services division generates recurring software-like gross margins (>70%), expanding earnings power. Apple Intelligence AI integration will drive a massive multi-year iPhone upgrade supercycle.",
                            bear_case="BEAR THESIS: Valuation at 28.5x P/E leaves minimal safety buffer. Growth in Greater China market faces headwinds, while antitrust scrutiny against App Store fees presents long-term margin pressure.",
                            verdict="JUDGE VERDICT: Bull thesis dominates on cash flow predictability and ecosystem lock-in. Staged accumulation recommended near the 50-day SMA ($220)."
                        ),
                        margin_top="1rem", width="100%"
                    ),
                    
                    align_items="stretch", spacing="4", width="100%"
                ),
                margin_left="260px", padding="2rem", width="calc(100vw - 260px)", min_height="calc(100vh - 70px)"
            )
        ),
        background="#0F172A", min_height="100vh"
    )
