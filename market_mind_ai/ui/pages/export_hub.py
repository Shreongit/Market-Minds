import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE
from market_mind_ai.ui.components.navbar import navbar_component
from market_mind_ai.ui.components.sidebar import sidebar_component

def export_card(title: str, format_type: str, desc: str, icon_name: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(tag=icon_name, size=24, color="#6366F1"),
                rx.vstack(
                    rx.text(title, font_size="1rem", font_weight="800", color="white"),
                    rx.text(desc, font_size="0.8rem", color="#94A3B8"),
                    align_items="start", spacing="1"
                ),
                rx.spacer(),
                rx.button(f"Download {format_type}", icon="download", color_scheme="indigo", variant="soft", border_radius="10px"),
                width="100%", align_items="center"
            ),
            align_items="stretch"
        ),
        style=GLASS_CARD_STYLE, width="100%"
    )

def export_hub_page() -> rx.Component:
    return rx.box(
        navbar_component("Export"),
        rx.hstack(
            sidebar_component("Export"),
            rx.box(
                rx.vstack(
                    rx.heading("Investment Intelligence Export Hub", font_size="1.8rem", color="white", font_weight="900"),
                    rx.text("Generate and download institutional-grade PDF research reports, Excel models, or raw CSV datasets.", color="#94A3B8", font_size="0.9rem"),
                    
                    rx.vstack(
                        export_card("Full Equity Research Report", "PDF", "Comprehensive 3-page research report with multi-agent scores, price targets, reasoning, and invalidation triggers.", "file-text"),
                        export_card("Portfolio Health & Allocation Digest", "Excel (.xlsx)", "Detailed position breakdown, sector weightings, expected returns, and health metrics.", "table"),
                        export_card("Strategy Backtest Trade Logs", "CSV", "Complete raw trade execution logs, entry/exit prices, return percentages, and equity curve timestamps.", "file-spreadsheets"),
                        spacing="3", width="100%", margin_top="1rem"
                    ),
                    align_items="stretch", spacing="4", width="100%"
                ),
                margin_left="260px", padding="2rem", width="calc(100vw - 260px)", min_height="calc(100vh - 70px)"
            )
        ),
        background="#0F172A", min_height="100vh"
    )
