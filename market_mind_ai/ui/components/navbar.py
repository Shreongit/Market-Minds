import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE, PRIMARY

def navbar_component(current_page: str = "Dashboard") -> rx.Component:
    return rx.box(
        rx.hstack(
            # Brand & Tagline
            rx.hstack(
                rx.box(
                    rx.text("MM", font_weight="900", font_size="1.2rem", color="white"),
                    background=f"linear-gradient(135deg, {PRIMARY}, #3B82F6)",
                    border_radius="10px",
                    padding_x="0.6rem",
                    padding_y="0.3rem"
                ),
                rx.vstack(
                    rx.text("MarketMind AI", font_size="1.2rem", font_weight="800", color="white", line_height="1"),
                    rx.text("Your Autonomous Investment Copilot", font_size="0.75rem", color="#94A3B8", line_height="1"),
                    spacing="1",
                    align_items="start"
                ),
                spacing="3",
                align_items="center"
            ),
            rx.spacer(),
            # Status Badge & Quick Ticker
            rx.hstack(
                rx.badge("● System Active", color_scheme="green", variant="soft", padding_x="0.8rem", border_radius="9999px"),
                rx.badge("Multi-Agent Engine v2.4", color_scheme="purple", variant="soft", padding_x="0.8rem", border_radius="9999px"),
                spacing="3",
                align_items="center"
            ),
            width="100%",
            align_items="center"
        ),
        width="100%",
        padding_x="2rem",
        padding_y="1rem",
        background="rgba(15, 23, 42, 0.9)",
        backdrop_filter="blur(16px)",
        border_bottom="1px solid rgba(255, 255, 255, 0.1)",
        position="sticky",
        top="0",
        z_index="100"
    )
