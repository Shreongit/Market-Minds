import reflex as rx

# Color Palette Tokens
PRIMARY = "#6366F1"        # Indigo/Violet primary accent
PRIMARY_HOVER = "#4F46E5"
SUCCESS = "#10B981"        # Emerald Buy/Bullish
WARNING = "#F59E0B"        # Amber Hold/Neutral
DANGER = "#EF4444"         # Rose Sell/Bearish

BG_DARK = "#0F172A"        # Deep slate dark background
CARD_BG_DARK = "rgba(30, 41, 59, 0.75)" # Dark glassmorphism card
CARD_BORDER_DARK = "rgba(255, 255, 255, 0.1)"
TEXT_PRIMARY_DARK = "#F8FAFC"
TEXT_MUTED_DARK = "#94A3B8"

# Glassmorphism Card Style Dictionary
GLASS_CARD_STYLE = {
    "background": CARD_BG_DARK,
    "backdrop_filter": "blur(12px)",
    "border_radius": "16px",
    "border": f"1px solid {CARD_BORDER_DARK}",
    "box_shadow": "0 8px 32px 0 rgba(0, 0, 0, 0.37)",
    "padding": "1.5rem",
    "transition": "all 0.3s ease-in-out",
    "_hover": {
        "border_color": "rgba(99, 102, 241, 0.4)",
        "transform": "translateY(-2px)",
        "box_shadow": "0 12px 40px 0 rgba(99, 102, 241, 0.25)"
    }
}

BADGE_BUY_STYLE = {
    "background": "rgba(16, 185, 129, 0.15)",
    "color": "#34D399",
    "border": "1px solid rgba(16, 185, 129, 0.4)",
    "font_weight": "700",
    "font_size": "1.1rem",
    "padding_x": "1.2rem",
    "padding_y": "0.4rem",
    "border_radius": "9999px"
}

BADGE_HOLD_STYLE = {
    "background": "rgba(245, 158, 11, 0.15)",
    "color": "#FBBF24",
    "border": "1px solid rgba(245, 158, 11, 0.4)",
    "font_weight": "700",
    "font_size": "1.1rem",
    "padding_x": "1.2rem",
    "padding_y": "0.4rem",
    "border_radius": "9999px"
}

BADGE_SELL_STYLE = {
    "background": "rgba(239, 68, 68, 0.15)",
    "color": "#F87171",
    "border": "1px solid rgba(239, 68, 68, 0.4)",
    "font_weight": "700",
    "font_size": "1.1rem",
    "padding_x": "1.2rem",
    "padding_y": "0.4rem",
    "border_radius": "9999px"
}
