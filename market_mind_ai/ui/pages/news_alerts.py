import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE
from market_mind_ai.ui.components.navbar import navbar_component
from market_mind_ai.ui.components.sidebar import sidebar_component

def news_alerts_page() -> rx.Component:
    return rx.box(
        navbar_component("News"),
        rx.hstack(
            sidebar_component("News"),
            rx.box(
                rx.vstack(
                    rx.heading("News Impact Engine & Smart Alerts", font_size="1.8rem", color="white", font_weight="900"),
                    rx.text("Real-time financial news ingestion, NLP sentiment classification, and context-driven smart alerts.", color="#94A3B8", font_size="0.9rem"),
                    
                    rx.grid(
                        # Left Column: News Classifier Feed
                        rx.vstack(
                            rx.text("CLASSIFIED FINANCIAL NEWS FEED", font_size="0.85rem", font_weight="800", color="white", letter_spacing="1px"),
                            rx.box(
                                rx.vstack(
                                    rx.hstack(
                                        rx.badge("POSITIVE (+0.75)", color_scheme="green", padding_x="0.6rem"),
                                        rx.badge("HIGH IMPACT", color_scheme="purple", padding_x="0.6rem"),
                                        rx.spacer(),
                                        rx.text("AAPL", font_weight="800", color="white"),
                                        width="100%", align_items="center"
                                    ),
                                    rx.text("Apple Reports Record Services Revenue Growth of +14% YoY", font_weight="800", font_size="1rem", color="white"),
                                    rx.text("Services segment margin expansion drives full-year earnings upgrade across Wall Street analysts.", font_size="0.85rem", color="#94A3B8"),
                                    align_items="start", spacing="2"
                                ),
                                style=GLASS_CARD_STYLE, width="100%"
                            ),
                            rx.box(
                                rx.vstack(
                                    rx.hstack(
                                        rx.badge("NEGATIVE (-0.45)", color_scheme="red", padding_x="0.6rem"),
                                        rx.badge("MEDIUM IMPACT", color_scheme="amber", padding_x="0.6rem"),
                                        rx.spacer(),
                                        rx.text("INTC", font_weight="800", color="white"),
                                        width="100%", align_items="center"
                                    ),
                                    rx.text("Intel Delays Next-Gen Process Node Manufacturing Milestone", font_weight="800", font_size="1rem", color="white"),
                                    rx.text("Foundry division costs pressure near-term free cash flow yield.", font_size="0.85rem", color="#94A3B8"),
                                    align_items="start", spacing="2"
                                ),
                                style=GLASS_CARD_STYLE, width="100%"
                            ),
                            spacing="3", align_items="stretch"
                        ),
                        
                        # Right Column: Smart Alerts Feed
                        rx.vstack(
                            rx.text("CONTEXT-DRIVEN SMART ALERTS", font_size="0.85rem", font_weight="800", color="white", letter_spacing="1px"),
                            rx.box(
                                rx.vstack(
                                    rx.hstack(
                                        rx.icon(tag="zap", size=18, color="#34D399"),
                                        rx.text("BULLISH BREAKOUT: NVDA", font_weight="800", font_size="0.9rem", color="#34D399"),
                                        rx.spacer(),
                                        rx.text("Confidence: 94%", font_size="0.75rem", color="#94A3B8"),
                                        width="100%", align_items="center"
                                    ),
                                    rx.text("NVDA crossed 50-day SMA ($122.50) on 2.1x average daily volume.", font_size="0.85rem", color="#E2E8F0"),
                                    align_items="start", spacing="1"
                                ),
                                style=GLASS_CARD_STYLE, width="100%"
                            ),
                            rx.box(
                                rx.vstack(
                                    rx.hstack(
                                        rx.icon(tag="shield-alert", size=18, color="#F87171"),
                                        rx.text("INSTITUTIONAL SELLING: TSLA", font_weight="800", font_size="0.9rem", color="#F87171"),
                                        rx.spacer(),
                                        rx.text("Confidence: 88%", font_size="0.75rem", color="#94A3B8"),
                                        width="100%", align_items="center"
                                    ),
                                    rx.text("Unusual block trade distribution detected at key resistance ($230.00).", font_size="0.85rem", color="#E2E8F0"),
                                    align_items="start", spacing="1"
                                ),
                                style=GLASS_CARD_STYLE, width="100%"
                            ),
                            spacing="3", align_items="stretch"
                        ),
                        columns="2", spacing="4", width="100%", margin_top="1rem"
                    ),
                    align_items="stretch", spacing="4", width="100%"
                ),
                margin_left="260px", padding="2rem", width="calc(100vw - 260px)", min_height="calc(100vh - 70px)"
            )
        ),
        background="#0F172A", min_height="100vh"
    )
