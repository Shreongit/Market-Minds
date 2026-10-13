import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE
from market_mind_ai.ui.components.navbar import navbar_component
from market_mind_ai.ui.components.sidebar import sidebar_component

def what_if_simulator_page() -> rx.Component:
    return rx.box(
        navbar_component("What-If"),
        rx.hstack(
            sidebar_component("What-If"),
            rx.box(
                rx.vstack(
                    rx.heading("Macro 'What-If' Scenario Simulator", font_size="1.8rem", color="white", font_weight="900"),
                    rx.text("Ask natural-language macro questions to simulate sector sensitivity and portfolio stress testing.", color="#94A3B8", font_size="0.9rem"),
                    
                    rx.box(
                        rx.hstack(
                            rx.input(
                                placeholder="e.g., What if crude oil spikes to $100 per barrel?",
                                variant="unstyled",
                                color="white",
                                font_size="1rem",
                                width="100%"
                            ),
                            rx.button("Simulate Impact", icon="cpu", color_scheme="indigo", border_radius="10px"),
                            spacing="3", width="100%", align_items="center"
                        ),
                        style=GLASS_CARD_STYLE, width="100%", margin_y="1rem"
                    ),
                    
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.icon(tag="alert-triangle", size=22, color="#F59E0B"),
                                rx.text("SIMULATED IMPACT: Crude Oil Spike to $100/bbl", font_size="1.1rem", font_weight="800", color="white"),
                                rx.spacer(),
                                rx.badge("-3.8% Estimated Portfolio Impact", color_scheme="red", padding_x="0.8rem"),
                                width="100%", align_items="center"
                            ),
                            rx.text("Oil price surge increases transportation costs, depresses consumer disposable income, and compresses airline/retail margins while boosting energy producers.", font_size="0.9rem", color="#CBD5E1", margin_y="0.5rem"),
                            
                            rx.grid(
                                rx.box(
                                    rx.text("VULNERABLE TICKERS", font_size="0.8rem", font_weight="800", color="#F87171"),
                                    rx.text("DAL, AAL, UAL, AMZN, TSLA", font_size="0.9rem", color="white", font_weight="700"),
                                    background="rgba(239, 68, 68, 0.1)", padding="1rem", border_radius="10px", border="1px solid rgba(239, 68, 68, 0.3)"
                                ),
                                rx.box(
                                    rx.text("BENEFITING TICKERS", font_size="0.8rem", font_weight="800", color="#34D399"),
                                    rx.text("XOM, CVX, COP, OXY, SLB", font_size="0.9rem", color="white", font_weight="700"),
                                    background="rgba(16, 185, 129, 0.1)", padding="1rem", border_radius="10px", border="1px solid rgba(16, 185, 129, 0.3)"
                                ),
                                columns="2", spacing="4", width="100%"
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
