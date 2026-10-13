import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE, PRIMARY
from market_mind_ai.ui.components.navbar import navbar_component
from market_mind_ai.ui.components.sidebar import sidebar_component

def strategy_builder_page() -> rx.Component:
    return rx.box(
        navbar_component("Strategy"),
        rx.hstack(
            sidebar_component("Strategy"),
            rx.box(
                rx.vstack(
                    # Header
                    rx.hstack(
                        rx.vstack(
                            rx.heading("AI Strategy Builder & Backtester Lab", font_size="1.8rem", color="white", font_weight="900"),
                            rx.text("Build rule-based technical strategies and evaluate performance against multi-year historical data.", color="#94A3B8", font_size="0.9rem"),
                            align_items="start", spacing="1"
                        ),
                        rx.spacer(),
                        rx.button("Run Historical Backtest", icon="play", color_scheme="indigo", border_radius="10px"),
                        width="100%", align_items="center"
                    ),
                    
                    # Rule Builder Form & Config
                    rx.box(
                        rx.vstack(
                            rx.text("STRATEGY ENTRY RULES", font_size="0.85rem", font_weight="800", color="white", letter_spacing="1px"),
                            rx.hstack(
                                rx.box(
                                    rx.text("Ticker", font_size="0.75rem", color="#94A3B8"),
                                    rx.input(value="AAPL", width="120px", color="white", background="rgba(255, 255, 255, 0.05)")
                                ),
                                rx.box(
                                    rx.text("Initial Capital ($)", font_size="0.75rem", color="#94A3B8"),
                                    rx.input(value="10000", width="140px", color="white", background="rgba(255, 255, 255, 0.05)")
                                ),
                                rx.box(
                                    rx.text("Stop Loss (%)", font_size="0.75rem", color="#94A3B8"),
                                    rx.input(value="5.0", width="100px", color="white", background="rgba(255, 255, 255, 0.05)")
                                ),
                                rx.box(
                                    rx.text("Take Profit (%)", font_size="0.75rem", color="#94A3B8"),
                                    rx.input(value="15.0", width="100px", color="white", background="rgba(255, 255, 255, 0.05)")
                                ),
                                spacing="4", align_items="center"
                            ),
                            align_items="start", spacing="3"
                        ),
                        style=GLASS_CARD_STYLE, width="100%", margin_y="1rem"
                    ),
                    
                    # Backtest Results Output Cards Grid
                    rx.grid(
                        rx.box(
                            rx.text("TOTAL RETURN", font_size="0.75rem", color="#94A3B8", font_weight="700"),
                            rx.text("+28.4%", font_size="1.8rem", font_weight="900", color="#34D399"),
                            rx.text("vs S&P 500 (+14.2%)", font_size="0.75rem", color="#94A3B8"),
                            style=GLASS_CARD_STYLE, width="100%"
                        ),
                        rx.box(
                            rx.text("CAGR", font_size="0.75rem", color="#94A3B8", font_weight="700"),
                            rx.text("26.8%", font_size="1.8rem", font_weight="900", color="#6366F1"),
                            rx.text("Annualized Return", font_size="0.75rem", color="#94A3B8"),
                            style=GLASS_CARD_STYLE, width="100%"
                        ),
                        rx.box(
                            rx.text("SHARPE RATIO", font_size="0.75rem", color="#94A3B8", font_weight="700"),
                            rx.text("1.84", font_size="1.8rem", font_weight="900", color="#FBBF24"),
                            rx.text("Risk-Adjusted Return", font_size="0.75rem", color="#94A3B8"),
                            style=GLASS_CARD_STYLE, width="100%"
                        ),
                        rx.box(
                            rx.text("MAX DRAWDOWN", font_size="0.75rem", color="#94A3B8", font_weight="700"),
                            rx.text("-8.2%", font_size="1.8rem", font_weight="900", color="#F87171"),
                            rx.text("Peak-to-Trough Loss", font_size="0.75rem", color="#94A3B8"),
                            style=GLASS_CARD_STYLE, width="100%"
                        ),
                        rx.box(
                            rx.text("WIN RATE", font_size="0.75rem", color="#94A3B8", font_weight="700"),
                            rx.text("68.5%", font_size="1.8rem", font_weight="900", color="#34D399"),
                            rx.text("14 Wins / 6 Losses", font_size="0.75rem", color="#94A3B8"),
                            style=GLASS_CARD_STYLE, width="100%"
                        ),
                        columns="5", spacing="4", width="100%"
                    ),
                    
                    align_items="stretch", spacing="4", width="100%"
                ),
                margin_left="260px", padding="2rem", width="calc(100vw - 260px)", min_height="calc(100vh - 70px)"
            )
        ),
        background="#0F172A", min_height="100vh"
    )
