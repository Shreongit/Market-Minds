import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE, PRIMARY
from market_mind_ai.ui.components.navbar import navbar_component
from market_mind_ai.ui.components.sidebar import sidebar_component

def portfolio_doctor_page() -> rx.Component:
    return rx.box(
        navbar_component("Portfolio"),
        rx.hstack(
            sidebar_component("Portfolio"),
            rx.box(
                rx.vstack(
                    # Header
                    rx.hstack(
                        rx.vstack(
                            rx.heading("AI Portfolio Doctor", font_size="1.8rem", color="white", font_weight="900"),
                            rx.text("Evaluates portfolio diversification, sector concentration, correlation risk, and provides concrete optimization suggestions.", color="#94A3B8", font_size="0.9rem"),
                            align_items="start", spacing="1"
                        ),
                        rx.spacer(),
                        rx.button("Add Position", icon="plus", color_scheme="indigo", border_radius="10px"),
                        width="100%", align_items="center"
                    ),
                    
                    # Portfolio Health Score Overview Grid
                    rx.grid(
                        # Health Gauge
                        rx.box(
                            rx.vstack(
                                rx.text("PORTFOLIO HEALTH SCORE", font_size="0.8rem", font_weight="800", color="#94A3B8", letter_spacing="1px"),
                                rx.hstack(
                                    rx.text("82", font_size="3.2rem", font_weight="900", color="#34D399"),
                                    rx.vstack(
                                        rx.badge("HEALTHY & BALANCED", color_scheme="green", padding_x="0.8rem"),
                                        rx.text("Low sector concentration risk", font_size="0.75rem", color="#94A3B8"),
                                        align_items="start", spacing="1"
                                    ),
                                    align_items="center", spacing="4"
                                ),
                                rx.progress(value=82, color_scheme="green", width="100%", height="8px", border_radius="9999px"),
                                align_items="stretch", spacing="3"
                            ),
                            style=GLASS_CARD_STYLE, width="100%"
                        ),
                        
                        rx.box(
                            rx.vstack(
                                rx.text("DIVERSIFICATION INDEX", font_size="0.8rem", font_weight="800", color="#94A3B8", letter_spacing="1px"),
                                rx.text("74.5 / 100", font_size="2rem", font_weight="900", color="#6366F1"),
                                rx.text("Top Sector: Technology (32.4%)", font_size="0.85rem", color="#CBD5E1"),
                                align_items="start", spacing="2"
                            ),
                            style=GLASS_CARD_STYLE, width="100%"
                        ),
                        
                        rx.box(
                            rx.vstack(
                                rx.text("EXPECTED ANNUAL RETURN", font_size="0.8rem", font_weight="800", color="#94A3B8", letter_spacing="1px"),
                                rx.text("+14.2%", font_size="2rem", font_weight="900", color="#34D399"),
                                rx.text("Portfolio Beta: 1.08 vs S&P 500", font_size="0.85rem", color="#CBD5E1"),
                                align_items="start", spacing="2"
                            ),
                            style=GLASS_CARD_STYLE, width="100%"
                        ),
                        columns="3", spacing="4", width="100%", margin_y="1.5rem"
                    ),
                    
                    # Actionable AI Optimization Suggestions
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="sparkles", size=20, color="#6366F1"),
                                rx.text("ACTIONABLE AI OPTIMIZATION RECOMMENDATIONS", font_weight="800", font_size="0.95rem", color="white"),
                                spacing="2", align_items="center"
                            ),
                            rx.vstack(
                                rx.box(
                                    rx.hstack(
                                        rx.icon(tag="check-circle-2", size=18, color="#34D399"),
                                        rx.text("Rebalance Technology Exposure: Technology comprises 32.4% of total capital. Consider taking partial profits in NVDA to trim weight below 25%.", font_size="0.85rem", color="#E2E8F0"),
                                        align_items="center", spacing="3"
                                    ),
                                    background="rgba(255, 255, 255, 0.03)", padding="0.8rem", border_radius="10px"
                                ),
                                rx.box(
                                    rx.hstack(
                                        rx.icon(tag="plus-circle", size=18, color="#6366F1"),
                                        rx.text("Add Defensive Dividend Anchors: Rotate funds into Healthcare or Utilities (e.g. LLY or NEE) to reduce portfolio beta during interest rate shifts.", font_size="0.85rem", color="#E2E8F0"),
                                        align_items="center", spacing="3"
                                    ),
                                    background="rgba(255, 255, 255, 0.03)", padding="0.8rem", border_radius="10px"
                                ),
                                spacing="2", width="100%"
                            ),
                            align_items="stretch", spacing="3"
                        ),
                        style=GLASS_CARD_STYLE, width="100%"
                    ),
                    
                    align_items="stretch", spacing="4", width="100%"
                ),
                margin_left="260px", padding="2rem", width="calc(100vw - 260px)", min_height="calc(100vh - 70px)"
            )
        ),
        background="#0F172A", min_height="100vh"
    )
