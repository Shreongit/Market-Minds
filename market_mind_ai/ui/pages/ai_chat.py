import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE, PRIMARY
from market_mind_ai.ui.components.navbar import navbar_component
from market_mind_ai.ui.components.sidebar import sidebar_component

def chat_bubble(sender: str, message: str, is_user: bool = False) -> rx.Component:
    bg_color = "rgba(99, 102, 241, 0.2)" if is_user else "rgba(30, 41, 59, 0.8)"
    border_color = "rgba(99, 102, 241, 0.4)" if is_user else "rgba(255, 255, 255, 0.1)"
    align_pos = "end" if is_user else "start"
    
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="user" if is_user else "bot", size=14, color="#6366F1"),
                rx.text(sender, font_size="0.75rem", font_weight="700", color="#94A3B8"),
                spacing="2", align_items="center"
            ),
            rx.text(message, font_size="0.9rem", color="#F8FAFC", line_height="1.5"),
            align_items="start", spacing="1",
            padding="1rem", border_radius="14px",
            background=bg_color, border=f"1px solid {border_color}",
            max_width="80%"
        ),
        width="100%", justify_content=align_pos
    )

def ai_chat_page() -> rx.Component:
    return rx.box(
        navbar_component("Chat"),
        rx.hstack(
            sidebar_component("Chat"),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.vstack(
                            rx.heading("Conversational AI Investment Copilot", font_size="1.8rem", color="white", font_weight="900"),
                            rx.text("Ask any market or portfolio question to trigger the multi-agent intelligence pipeline.", color="#94A3B8", font_size="0.9rem"),
                            align_items="start", spacing="1"
                        ),
                        rx.spacer(),
                        rx.badge("TTS Voice Enabled", color_scheme="purple", padding_x="0.8rem"),
                        width="100%", align_items="center"
                    ),
                    
                    # Chat Window
                    rx.box(
                        rx.vstack(
                            chat_bubble("USER", "Should I buy Reliance or Apple right now?", is_user=True),
                            chat_bubble(
                                "MarketMind Copilot",
                                "Running multi-agent pipeline for Reliance Industries (RELIANCE.NS) and Apple Inc. (AAPL)...\n\n"
                                "• AAPL: Technical score 76/100, Fundamental 82/100. Recommendation: BUY (Target $250, Stop $210).\n"
                                "• RELIANCE: Strong energy refining margins + Jio telecom subscriber growth support a BUY rating with target ₹3,200.\n\n"
                                "Overall, both demonstrate strong balance sheets, but AAPL offers higher momentum while RELIANCE provides value safety."
                            ),
                            spacing="3", align_items="stretch"
                        ),
                        style=GLASS_CARD_STYLE, width="100%", min_height="400px", padding="1.5rem", margin_y="1rem"
                    ),
                    
                    # Input Box
                    rx.hstack(
                        rx.input(
                            placeholder="Ask a question (e.g. 'Compare Tesla vs Nvidia', 'Is Microsoft overvalued?')...",
                            variant="unstyled",
                            color="white",
                            font_size="1rem",
                            width="100%"
                        ),
                        rx.icon(tag="mic", size=20, color="#94A3B8", cursor="pointer"),
                        rx.button("Send Query", icon="send", color_scheme="indigo", border_radius="10px"),
                        spacing="3", width="100%", align_items="center",
                        background="rgba(30, 41, 59, 0.8)", padding="0.75rem 1rem", border_radius="12px", border="1px solid rgba(255, 255, 255, 0.1)"
                    ),
                    align_items="stretch", spacing="4", width="100%"
                ),
                margin_left="260px", padding="2rem", width="calc(100vw - 260px)", min_height="calc(100vh - 70px)"
            )
        ),
        background="#0F172A", min_height="100vh"
    )
