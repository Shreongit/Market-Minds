import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE

def debate_card_component(ticker: str, bull_case: str, bear_case: str, verdict: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="swords", size=24, color="#6366F1"),
                rx.text(f"BULL VS. BEAR DEBATE ARENA — {ticker}", font_size="1.1rem", font_weight="800", color="white"),
                rx.spacer(),
                rx.badge("AI Multi-Persona Debate", color_scheme="indigo", padding_x="0.8rem", border_radius="9999px"),
                width="100%",
                align_items="center"
            ),
            
            rx.grid(
                # Bull Case Box
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(tag="trending-up", size=20, color="#34D399"),
                            rx.text("BULL THESIS (AI Persona)", font_weight="800", font_size="0.9rem", color="#34D399"),
                            spacing="2", align_items="center"
                        ),
                        rx.text(bull_case, font_size="0.85rem", color="#E2E8F0", line_height="1.6"),
                        align_items="start", spacing="2"
                    ),
                    background="rgba(16, 185, 129, 0.08)",
                    padding="1.2rem",
                    border_radius="12px",
                    border="1px solid rgba(16, 185, 129, 0.3)"
                ),
                # Bear Case Box
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(tag="trending-down", size=20, color="#F87171"),
                            rx.text("BEAR THESIS (AI Persona)", font_weight="800", font_size="0.9rem", color="#F87171"),
                            spacing="2", align_items="center"
                        ),
                        rx.text(bear_case, font_size="0.85rem", color="#E2E8F0", line_height="1.6"),
                        align_items="start", spacing="2"
                    ),
                    background="rgba(239, 68, 68, 0.08)",
                    padding="1.2rem",
                    border_radius="12px",
                    border="1px solid rgba(239, 68, 68, 0.3)"
                ),
                columns="2",
                spacing="4",
                width="100%",
                margin_y="1rem"
            ),
            
            # Judge Verdict
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="gavel", size=20, color="#FBBF24"),
                        rx.text("IMPARTIAL JUDGE VERDICT", font_weight="800", font_size="0.9rem", color="#FBBF24"),
                        spacing="2", align_items="center"
                    ),
                    rx.text(verdict, font_size="0.9rem", color="#F8FAFC", line_height="1.6", font_weight="500"),
                    align_items="start", spacing="2"
                ),
                background="rgba(245, 158, 11, 0.1)",
                padding="1.2rem",
                border_radius="12px",
                border="1px solid rgba(245, 158, 11, 0.3)",
                width="100%"
            ),
            
            spacing="3",
            align_items="stretch"
        ),
        style=GLASS_CARD_STYLE,
        width="100%"
    )
