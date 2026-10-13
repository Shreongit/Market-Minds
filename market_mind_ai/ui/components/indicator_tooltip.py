import reflex as rx

INDICATOR_EXPLAINERS = {
    "RSI": {
        "title": "Relative Strength Index (RSI 14)",
        "what": "RSI measures the speed and change of price movements on a scale from 0 to 100.",
        "why": "Readings above 70 indicate overbought conditions (potential pullback), while readings below 30 signal oversold conditions (potential buying opportunity).",
        "limitations": "In strong trending bull markets, RSI can stay overbought for extended periods without a price reversal."
    },
    "MACD": {
        "title": "Moving Average Convergence Divergence (MACD)",
        "what": "MACD tracks the relationship between two exponential moving averages (12-period and 26-period EMA).",
        "why": "When the MACD line crosses above the Signal line, it produces a bullish buy signal; crossing below indicates bearish momentum.",
        "limitations": "Prone to whipsaws in sideways or range-bound consolidation phases."
    },
    "PE": {
        "title": "Price-to-Earnings Ratio (P/E)",
        "what": "P/E compares a company's current stock price to its earnings per share.",
        "why": "Helps determine if a stock is overvalued or undervalued relative to historical averages and industry peers.",
        "limitations": "Does not account for future debt loads or non-cash earnings adjustments."
    },
    "BETA": {
        "title": "Equity Beta (β)",
        "what": "Beta measures stock price volatility relative to the benchmark index (S&P 500 = 1.0).",
        "why": "Beta > 1.0 means higher market sensitivity and volatility; Beta < 1.0 indicates defensive price stability.",
        "limitations": "Reflects historical trailing price moves and may fail during unprecedented structural shifts."
    }
}

def indicator_tooltip_component(indicator_key: str = "RSI") -> rx.Component:
    info = INDICATOR_EXPLAINERS.get(indicator_key.upper(), INDICATOR_EXPLAINERS["RSI"])
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.hstack(
                rx.icon(tag="help-circle", size=14, color="#6366F1"),
                rx.text(f"Learn {indicator_key}", font_size="0.75rem", color="#6366F1", font_weight="600"),
                align_items="center",
                spacing="1",
                cursor="pointer"
            )
        ),
        rx.hover_card.content(
            rx.vstack(
                rx.text(info["title"], font_weight="800", font_size="0.85rem", color="#F8FAFC"),
                rx.text(f"WHAT IT IS: {info['what']}", font_size="0.75rem", color="#CBD5E1"),
                rx.text(f"WHY IT MATTERS: {info['why']}", font_size="0.75rem", color="#34D399"),
                rx.text(f"LIMITATIONS: {info['limitations']}", font_size="0.75rem", color="#F87171"),
                align_items="start",
                spacing="2",
                padding="1rem"
            ),
            background="rgba(15, 23, 42, 0.98)",
            border="1px solid rgba(99, 102, 241, 0.4)",
            border_radius="12px",
            box_shadow="0 10px 30px rgba(0,0,0,0.5)",
            max_width="320px"
        )
    )
