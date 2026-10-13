import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE
from market_mind_ai.ui.components.navbar import navbar_component
from market_mind_ai.ui.components.sidebar import sidebar_component

def market_story_page() -> rx.Component:
    return rx.box(
        navbar_component("Story"),
        rx.hstack(
            sidebar_component("Story"),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.vstack(
                            rx.heading("Daily AI Market Story Digest", font_size="1.8rem", color="white", font_weight="900"),
                            rx.text("Auto-generated daily executive briefing on what happened, why it matters, and what to watch tomorrow.", color="#94A3B8", font_size="0.9rem"),
                            align_items="start", spacing="1"
                        ),
                        rx.spacer(),
                        rx.badge("Scheduled Daily Digest", color_scheme="indigo", padding_x="0.8rem"),
                        width="100%", align_items="center"
                    ),
                    
                    rx.box(
                        rx.vstack(
                            rx.heading("Tech Rally & Yield Stabilization Drive Market Expansion", font_size="1.3rem", color="white", font_weight="800"),
                            rx.divider(border_color="rgba(255, 255, 255, 0.1)", margin_y="0.8rem"),
                            
                            rx.text("1. WHAT HAPPENED TODAY", font_size="0.85rem", font_weight="800", color="#6366F1", letter_spacing="1px"),
                            rx.text("US equity benchmark indices closed near session highs with the S&P 500 gaining +0.45% and the Nasdaq Composite rising +0.76%. Semiconductor leaders NVDA (+5.8%) and AMD (+3.4%) led gains following positive supply chain channel checks.", font_size="0.9rem", color="#E2E8F0", line_height="1.6"),
                            
                            rx.text("2. WHY IT MATTERS", font_size="0.85rem", font_weight="800", color="#34D399", letter_spacing="1px", margin_top="1rem"),
                            rx.text("Treasury yields stabilized following the latest inflation release, reducing discount rate pressure on growth equities. Corporate earnings revisions remain upwardly biased across 74% of S&P 500 components.", font_size="0.9rem", color="#E2E8F0", line_height="1.6"),
                            
                            rx.text("3. WHAT TO WATCH TOMORROW", font_size="0.85rem", font_weight="800", color="#FBBF24", letter_spacing="1px", margin_top="1rem"),
                            rx.text("Key catalyst events include the Federal Reserve's FOMC meeting minutes, weekly jobless claims data, and quarterly earnings calls from major industrial technology suppliers.", font_size="0.9rem", color="#E2E8F0", line_height="1.6"),
                            
                            align_items="start", spacing="2"
                        ),
                        style=GLASS_CARD_STYLE, width="100%", margin_top="1rem"
                    ),
                    align_items="stretch", spacing="4", width="100%"
                ),
                margin_left="260px", padding="2rem", width="calc(100vw - 260px)", min_height="calc(100vh - 70px)"
            )
        ),
        background="#0F172A", min_height="100vh"
    )
