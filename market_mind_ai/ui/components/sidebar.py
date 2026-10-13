import reflex as rx
from market_mind_ai.ui.theme import PRIMARY

def sidebar_item(icon_name: str, text: str, href: str, active: bool = False) -> rx.Component:
    bg_color = "rgba(99, 102, 241, 0.2)" if active else "transparent"
    text_color = "#F8FAFC" if active else "#94A3B8"
    font_wt = "700" if active else "500"
    border_left = f"4px solid {PRIMARY}" if active else "4px solid transparent"
    
    return rx.link(
        rx.hstack(
            rx.icon(tag=icon_name, size=18, color=text_color),
            rx.text(text, font_size="0.95rem", font_weight=font_wt, color=text_color),
            spacing="3",
            align_items="center",
            padding_x="1rem",
            padding_y="0.75rem",
            border_radius="0 10px 10px 0",
            background=bg_color,
            border_left=border_left,
            transition="all 0.2s ease-in-out",
            _hover={"background": "rgba(99, 102, 241, 0.15)", "color": "#F8FAFC"}
        ),
        href=href,
        width="100%",
        style={"text_decoration": "none"}
    )

def sidebar_component(current_page: str = "Dashboard") -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("INVESTMENT SUITE", font_size="0.7rem", font_weight="800", color="#64748B", letter_spacing="1px", padding_x="1rem", padding_top="1rem"),
            sidebar_item("layout-dashboard", "Market Dashboard", "/", active=(current_page == "Dashboard")),
            sidebar_item("trending-up", "Stock Intelligence Hub", "/stock", active=(current_page == "Stock")),
            sidebar_item("stethoscope", "AI Portfolio Doctor", "/portfolio", active=(current_page == "Portfolio")),
            sidebar_item("flask-conical", "Strategy & Backtesting Lab", "/strategy", active=(current_page == "Strategy")),
            
            rx.text("SIMULATIONS & ALERTS", font_size="0.7rem", font_weight="800", color="#64748B", letter_spacing="1px", padding_x="1rem", padding_top="1rem"),
            sidebar_item("cpu", "What-If Macro Simulator", "/what-if", active=(current_page == "What-If")),
            sidebar_item("bell", "News Impact & Alerts", "/news", active=(current_page == "News")),
            sidebar_item("book-open", "Daily Market Story", "/story", active=(current_page == "Story")),
            
            rx.text("COPILOT & EXPORTS", font_size="0.7rem", font_weight="800", color="#64748B", letter_spacing="1px", padding_x="1rem", padding_top="1rem"),
            sidebar_item("bot", "AI Chat Assistant", "/chat", active=(current_page == "Chat")),
            sidebar_item("download", "Export Hub", "/export", active=(current_page == "Export")),
            
            spacing="1",
            width="100%",
            align_items="stretch"
        ),
        width="260px",
        height="calc(100vh - 70px)",
        background="rgba(15, 23, 42, 0.95)",
        border_right="1px solid rgba(255, 255, 255, 0.1)",
        padding_y="1rem",
        position="fixed",
        top="70px",
        left="0",
        z_index="90"
    )
