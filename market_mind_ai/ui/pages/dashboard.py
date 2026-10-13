import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE, PRIMARY
from market_mind_ai.ui.components.navbar import navbar_component
from market_mind_ai.ui.components.sidebar import sidebar_component

def index_card(symbol: str, name: str, price: str, change: str, change_pct: float) -> rx.Component:
    is_pos = change_pct >= 0
    val_color = "#34D399" if is_pos else "#F87171"
    icon_tag = "trending-up" if is_pos else "trending-down"
    
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text(symbol, font_size="1.1rem", font_weight="800", color="white"),
                    rx.text(name, font_size="0.75rem", color="#94A3B8"),
                    align_items="start", spacing="1"
                ),
                rx.spacer(),
                rx.icon(tag=icon_tag, size=20, color=val_color),
                width="100%", align_items="center"
            ),
            rx.hstack(
                rx.text(price, font_size="1.5rem", font_weight="900", color="white"),
                rx.spacer(),
                rx.badge(f"{change} ({change_pct:+.2f}%)", color_scheme="green" if is_pos else "red", padding_x="0.6rem"),
                width="100%", align_items="baseline"
            ),
            align_items="stretch", spacing="3"
        ),
        style=GLASS_CARD_STYLE,
        width="100%"
    )

def dashboard_page() -> rx.Component:
    return rx.box(
        navbar_component("Dashboard"),
        rx.hstack(
            sidebar_component("Dashboard"),
            rx.box(
                rx.vstack(
                    # Header Banner
                    rx.hstack(
                        rx.vstack(
                            rx.heading("Market Intelligence Command Center", font_size="1.8rem", color="white", font_weight="900"),
                            rx.text("Autonomous multi-agent synthesis across global indices, sector heatmaps, and sentiment alerts.", color="#94A3B8", font_size="0.9rem"),
                            align_items="start", spacing="1"
                        ),
                        rx.spacer(),
                        rx.button("Refresh Live Feeds", icon="rotate-cw", color_scheme="indigo", variant="soft", border_radius="10px"),
                        width="100%", align_items="center"
                    ),
                    
                    # Major Indices Cards Grid
                    rx.grid(
                        index_card("S&P 500", "US Large Cap Benchmark", "5,432.10", "+24.50", 0.45),
                        index_card("NASDAQ 100", "Tech Growth Index", "18,920.40", "+142.10", 0.76),
                        index_card("DOW JONES", "Industrial Average", "39,115.80", "-45.20", -0.12),
                        index_card("CBOE VIX", "Volatility Fear Index", "14.25", "-0.85", -5.63),
                        columns="4", spacing="4", width="100%", margin_y="1.5rem"
                    ),
                    
                    # Dashboard Main Content Grid
                    rx.grid(
                        # Left Column: Market Heatmap & Intelligence Feed
                        rx.vstack(
                            rx.box(
                                rx.vstack(
                                    rx.hstack(
                                        rx.icon(tag="layout-grid", size=20, color="#6366F1"),
                                        rx.text("SECTOR PERFORMANCE HEATMAP", font_size="0.9rem", font_weight="800", color="white"),
                                        width="100%", align_items="center"
                                    ),
                                    rx.grid(
                                        rx.box(rx.text("Technology", font_size="0.8rem", font_weight="700", color="white"), rx.text("+1.8%", font_weight="900", color="#34D399"), background="rgba(16, 185, 129, 0.2)", padding="1rem", border_radius="10px", border="1px solid rgba(16, 185, 129, 0.3)"),
                                        rx.box(rx.text("Healthcare", font_size="0.8rem", font_weight="700", color="white"), rx.text("+0.4%", font_weight="900", color="#34D399"), background="rgba(16, 185, 129, 0.1)", padding="1rem", border_radius="10px", border="1px solid rgba(16, 185, 129, 0.2)"),
                                        rx.box(rx.text("Financials", font_size="0.8rem", font_weight="700", color="white"), rx.text("-0.6%", font_weight="900", color="#F87171"), background="rgba(239, 68, 68, 0.1)", padding="1rem", border_radius="10px", border="1px solid rgba(239, 68, 68, 0.2)"),
                                        rx.box(rx.text("Energy", font_size="0.8rem", font_weight="700", color="white"), rx.text("+2.4%", font_weight="900", color="#34D399"), background="rgba(16, 185, 129, 0.25)", padding="1rem", border_radius="10px", border="1px solid rgba(16, 185, 129, 0.4)"),
                                        rx.box(rx.text("Consumer Disc.", font_size="0.8rem", font_weight="700", color="white"), rx.text("-1.2%", font_weight="900", color="#F87171"), background="rgba(239, 68, 68, 0.2)", padding="1rem", border_radius="10px", border="1px solid rgba(239, 68, 68, 0.3)"),
                                        rx.box(rx.text("Industrials", font_size="0.8rem", font_weight="700", color="white"), rx.text("+0.1%", font_weight="900", color="#FBBF24"), background="rgba(245, 158, 11, 0.1)", padding="1rem", border_radius="10px", border="1px solid rgba(245, 158, 11, 0.2)"),
                                        columns="3", spacing="3", width="100%"
                                    ),
                                    align_items="stretch", spacing="3"
                                ),
                                style=GLASS_CARD_STYLE, width="100%"
                            ),
                            
                            rx.box(
                                rx.vstack(
                                    rx.hstack(
                                        rx.icon(tag="zap", size=20, color="#F59E0B"),
                                        rx.text("AI REAL-TIME INSIGHTS FEED", font_size="0.9rem", font_weight="800", color="white"),
                                        width="100%", align_items="center"
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.text("BULLISH BREAKOUT: NVDA crossed 50-day SMA ($122.50) on 1.8x average volume.", font_size="0.85rem", color="#E2E8F0"),
                                            rx.text("Technical Agent | 92% Confidence", font_size="0.75rem", color="#34D399", font_weight="700", margin_top="0.2rem"),
                                            background="rgba(255, 255, 255, 0.03)", padding="0.8rem", border_radius="8px", border_left="4px solid #34D399"
                                        ),
                                        rx.box(
                                            rx.text("EARNINGS SURPRISE: AAPL Services revenue expanded +14% YoY, beating consensus.", font_size="0.85rem", color="#E2E8F0"),
                                            rx.text("Fundamental Agent | 88% Confidence", font_size="0.75rem", color="#6366F1", font_weight="700", margin_top="0.2rem"),
                                            background="rgba(255, 255, 255, 0.03)", padding="0.8rem", border_radius="8px", border_left="4px solid #6366F1"
                                        ),
                                        spacing="2", width="100%"
                                    ),
                                    align_items="stretch", spacing="3"
                                ),
                                style=GLASS_CARD_STYLE, width="100%"
                            ),
                            align_items="stretch", spacing="4"
                        ),
                        
                        # Right Column: Fear & Greed Gauge & Top Gainers/Losers
                        rx.vstack(
                            rx.box(
                                rx.vstack(
                                    rx.text("MARKET FEAR & GREED GAUGE", font_size="0.85rem", font_weight="800", color="white"),
                                    rx.hstack(
                                        rx.text("68", font_size="3rem", font_weight="900", color="#34D399"),
                                        rx.vstack(
                                            rx.badge("GREED ENVIRONMENT", color_scheme="green", padding_x="0.8rem"),
                                            rx.text("Bullish macro risk appetite active", font_size="0.75rem", color="#94A3B8"),
                                            align_items="start", spacing="1"
                                        ),
                                        align_items="center", spacing="4"
                                    ),
                                    rx.progress(value=68, color_scheme="green", width="100%", height="8px", border_radius="9999px"),
                                    align_items="stretch", spacing="3"
                                ),
                                style=GLASS_CARD_STYLE, width="100%"
                            ),
                            
                            rx.box(
                                rx.vstack(
                                    rx.text("TOP MARKET MOVERS", font_size="0.85rem", font_weight="800", color="white"),
                                    rx.hstack(
                                        rx.vstack(rx.text("NVDA", font_weight="800", color="white"), rx.text("$128.50", font_size="0.8rem", color="#94A3B8"), align_items="start"),
                                        rx.spacer(),
                                        rx.text("+5.8%", font_weight="800", color="#34D399"),
                                        width="100%", align_items="center", background="rgba(255, 255, 255, 0.03)", padding="0.6rem", border_radius="8px"
                                    ),
                                    rx.hstack(
                                        rx.vstack(rx.text("TSLA", font_weight="800", color="white"), rx.text("$224.10", font_size="0.8rem", color="#94A3B8"), align_items="start"),
                                        rx.spacer(),
                                        rx.text("+4.2%", font_weight="800", color="#34D399"),
                                        width="100%", align_items="center", background="rgba(255, 255, 255, 0.03)", padding="0.6rem", border_radius="8px"
                                    ),
                                    rx.hstack(
                                        rx.vstack(rx.text("INTC", font_weight="800", color="white"), rx.text("$31.20", font_size="0.8rem", color="#94A3B8"), align_items="start"),
                                        rx.spacer(),
                                        rx.text("-3.5%", font_weight="800", color="#F87171"),
                                        width="100%", align_items="center", background="rgba(255, 255, 255, 0.03)", padding="0.6rem", border_radius="8px"
                                    ),
                                    align_items="stretch", spacing="2"
                                ),
                                style=GLASS_CARD_STYLE, width="100%"
                            ),
                            align_items="stretch", spacing="4"
                        ),
                        columns="3", spacing="4", width="100%"
                    ),
                    align_items="stretch", spacing="4", width="100%"
                ),
                margin_left="260px", padding="2rem", width="calc(100vw - 260px)", min_height="calc(100vh - 70px)"
            )
        ),
        background="#0F172A", min_height="100vh"
    )
