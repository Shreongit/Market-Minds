import reflex as rx
from market_mind_ai.ui.theme import GLASS_CARD_STYLE, BADGE_BUY_STYLE, BADGE_HOLD_STYLE, BADGE_SELL_STYLE

def decision_card_component(
    ticker: str,
    recommendation: str,
    confidence: float,
    target_price: float,
    stop_loss: float,
    entry_range: str,
    holding_period: str,
    risk_level: str,
    overall_score: float,
    tech_score: float,
    tech_why: str,
    fund_score: float,
    fund_why: str,
    sent_score: float,
    sent_why: str,
    risk_score: float,
    risk_why: str,
    reasoning: str,
    invalidation: str,
    limitations: str
) -> rx.Component:
    
    # Select recommendation badge style
    if recommendation == "BUY":
        badge_style = BADGE_BUY_STYLE
        rec_color = "#34D399"
    elif recommendation == "SELL":
        badge_style = BADGE_SELL_STYLE
        rec_color = "#F87171"
    else:
        badge_style = BADGE_HOLD_STYLE
        rec_color = "#FBBF24"

    return rx.box(
        rx.vstack(
            # Header Row: Recommendation Badge & Overall AI Score
            rx.hstack(
                rx.vstack(
                    rx.text(f"SYNTHESIZED RECOMMENDATION FOR {ticker}", font_size="0.75rem", font_weight="800", color="#94A3B8", letter_spacing="1px"),
                    rx.box(
                        rx.text(recommendation, style=badge_style),
                        margin_top="0.3rem"
                    ),
                    align_items="start"
                ),
                rx.spacer(),
                rx.vstack(
                    rx.text("OVERALL AI SCORE", font_size="0.75rem", font_weight="800", color="#94A3B8", letter_spacing="1px"),
                    rx.hstack(
                        rx.text(f"{overall_score:.0f}", font_size="2.2rem", font_weight="900", color=rec_color),
                        rx.text("/100", font_size="1rem", font_weight="600", color="#64748B"),
                        align_items="baseline",
                        spacing="1"
                    ),
                    align_items="end"
                ),
                width="100%",
                align_items="center"
            ),
            
            rx.divider(border_color="rgba(255, 255, 255, 0.1)", margin_y="1rem"),
            
            # Key Price Targets & Parameters Grid
            rx.grid(
                rx.box(
                    rx.text("CONFIDENCE", font_size="0.7rem", color="#94A3B8", font_weight="700"),
                    rx.text(f"{confidence:.0f}%", font_size="1.2rem", font_weight="800", color="#F8FAFC"),
                    background="rgba(255, 255, 255, 0.04)", padding="0.8rem", border_radius="10px"
                ),
                rx.box(
                    rx.text("TARGET PRICE", font_size="0.7rem", color="#94A3B8", font_weight="700"),
                    rx.text(f"${target_price:.2f}", font_size="1.2rem", font_weight="800", color="#34D399"),
                    background="rgba(255, 255, 255, 0.04)", padding="0.8rem", border_radius="10px"
                ),
                rx.box(
                    rx.text("STOP LOSS", font_size="0.7rem", color="#94A3B8", font_weight="700"),
                    rx.text(f"${stop_loss:.2f}", font_size="1.2rem", font_weight="800", color="#F87171"),
                    background="rgba(255, 255, 255, 0.04)", padding="0.8rem", border_radius="10px"
                ),
                rx.box(
                    rx.text("ENTRY RANGE", font_size="0.7rem", color="#94A3B8", font_weight="700"),
                    rx.text(entry_range, font_size="1.0rem", font_weight="800", color="#F8FAFC"),
                    background="rgba(255, 255, 255, 0.04)", padding="0.8rem", border_radius="10px"
                ),
                rx.box(
                    rx.text("HOLDING PERIOD", font_size="0.7rem", color="#94A3B8", font_weight="700"),
                    rx.text(holding_period, font_size="1.0rem", font_weight="800", color="#6366F1"),
                    background="rgba(255, 255, 255, 0.04)", padding="0.8rem", border_radius="10px"
                ),
                rx.box(
                    rx.text("RISK RATING", font_size="0.7rem", color="#94A3B8", font_weight="700"),
                    rx.text(risk_level, font_size="1.0rem", font_weight="800", color="#FBBF24"),
                    background="rgba(255, 255, 255, 0.04)", padding="0.8rem", border_radius="10px"
                ),
                columns="3",
                spacing="3",
                width="100%"
            ),
            
            rx.divider(border_color="rgba(255, 255, 255, 0.1)", margin_y="1rem"),
            
            # Multi-Agent Scores Breakdown
            rx.text("INDEPENDENT AGENT SCORECARD", font_size="0.8rem", font_weight="800", color="#94A3B8", letter_spacing="1px"),
            rx.grid(
                rx.vstack(
                    rx.hstack(
                        rx.text("Technical Analysis", font_weight="700", font_size="0.85rem", color="#F8FAFC"),
                        rx.spacer(),
                        rx.text(f"{tech_score:.0f}/100", font_weight="800", color="#6366F1")
                    ),
                    rx.progress(value=tech_score, color_scheme="indigo", width="100%", height="6px", border_radius="9999px"),
                    rx.text(tech_why, font_size="0.75rem", color="#94A3B8"),
                    align_items="stretch", spacing="1", background="rgba(255, 255, 255, 0.03)", padding="0.8rem", border_radius="10px"
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text("Fundamental Analysis", font_weight="700", font_size="0.85rem", color="#F8FAFC"),
                        rx.spacer(),
                        rx.text(f"{fund_score:.0f}/100", font_weight="800", color="#10B981")
                    ),
                    rx.progress(value=fund_score, color_scheme="green", width="100%", height="6px", border_radius="9999px"),
                    rx.text(fund_why, font_size="0.75rem", color="#94A3B8"),
                    align_items="stretch", spacing="1", background="rgba(255, 255, 255, 0.03)", padding="0.8rem", border_radius="10px"
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text("Market Sentiment", font_weight="700", font_size="0.85rem", color="#F8FAFC"),
                        rx.spacer(),
                        rx.text(f"{sent_score:.0f}/100", font_weight="800", color="#F59E0B")
                    ),
                    rx.progress(value=sent_score, color_scheme="amber", width="100%", height="6px", border_radius="9999px"),
                    rx.text(sent_why, font_size="0.75rem", color="#94A3B8"),
                    align_items="stretch", spacing="1", background="rgba(255, 255, 255, 0.03)", padding="0.8rem", border_radius="10px"
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text("Risk Volatility", font_weight="700", font_size="0.85rem", color="#F8FAFC"),
                        rx.spacer(),
                        rx.text(f"{risk_score:.0f}/100", font_weight="800", color="#EF4444")
                    ),
                    rx.progress(value=risk_score, color_scheme="red", width="100%", height="6px", border_radius="9999px"),
                    rx.text(risk_why, font_size="0.75rem", color="#94A3B8"),
                    align_items="stretch", spacing="1", background="rgba(255, 255, 255, 0.03)", padding="0.8rem", border_radius="10px"
                ),
                columns="2",
                spacing="3",
                width="100%"
            ),
            
            rx.divider(border_color="rgba(255, 255, 255, 0.1)", margin_y="1rem"),
            
            # Plain-English Rationale
            rx.text("FULL INVESTMENT RATIONALE", font_size="0.8rem", font_weight="800", color="#94A3B8", letter_spacing="1px"),
            rx.box(
                rx.text(reasoning, font_size="0.9rem", color="#E2E8F0", line_height="1.6"),
                background="rgba(255, 255, 255, 0.03)",
                padding="1rem",
                border_radius="10px",
                border_left=f"4px solid {rec_color}"
            ),
            
            # Invalidation Criteria & Limitations Accordion / Boxes
            rx.hstack(
                rx.box(
                    rx.text("THESIS INVALIDATION TRIGGERS", font_size="0.75rem", font_weight="800", color="#F87171", letter_spacing="1px"),
                    rx.text(invalidation, font_size="0.8rem", color="#CBD5E1", line_height="1.5", margin_top="0.3rem"),
                    background="rgba(239, 68, 68, 0.08)", padding="0.8rem", border_radius="10px", border="1px solid rgba(239, 68, 68, 0.2)", width="50%"
                ),
                rx.box(
                    rx.text("STATED ANALYSIS LIMITATIONS", font_size="0.75rem", font_weight="800", color="#FBBF24", letter_spacing="1px"),
                    rx.text(limitations, font_size="0.8rem", color="#CBD5E1", line_height="1.5", margin_top="0.3rem"),
                    background="rgba(245, 158, 11, 0.08)", padding="0.8rem", border_radius="10px", border="1px solid rgba(245, 158, 11, 0.2)", width="50%"
                ),
                spacing="3",
                width="100%",
                margin_top="0.8rem"
            ),
            
            spacing="3",
            align_items="stretch"
        ),
        style=GLASS_CARD_STYLE,
        width="100%"
    )
