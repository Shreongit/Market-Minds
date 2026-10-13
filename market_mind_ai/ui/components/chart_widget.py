import reflex as rx
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from market_mind_ai.services.market_data_service import MarketDataService

def render_plotly_chart(ticker: str = "AAPL", period: str = "1y") -> go.Figure:
    df = MarketDataService.get_historical_df(ticker, period=period)
    
    if df.empty:
        fig = go.Figure()
        fig.add_annotation(text="No Price Data Available", showarrow=False, font=dict(color="white", size=20))
        fig.update_layout(template="plotly_dark", background="rgba(0,0,0,0)")
        return fig

    # Create 2 subplots: Price Candlestick + Volume/RSI
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[0.75, 0.25])

    # Candlestick
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name=ticker,
        increasing_line_color="#10B981",
        decreasing_line_color="#EF4444"
    ), row=1, col=1)

    # Moving Averages
    if "SMA_20" in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df["SMA_20"], mode="lines", name="SMA 20", line=dict(color="#3B82F6", width=1.5)), row=1, col=1)
    if "SMA_50" in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df["SMA_50"], mode="lines", name="SMA 50", line=dict(color="#F59E0B", width=1.5)), row=1, col=1)
    if "SMA_200" in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df["SMA_200"], mode="lines", name="SMA 200", line=dict(color="#8B5CF6", width=1.5)), row=1, col=1)

    # Volume
    colors_vol = ["#10B981" if c >= o else "#EF4444" for c, o in zip(df["Close"], df["Open"])]
    fig.add_trace(go.Bar(x=df.index, y=df["Volume"], name="Volume", marker_color=colors_vol, opacity=0.5), row=2, col=1)

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(15, 23, 42, 0.0)",
        plot_bgcolor="rgba(15, 23, 42, 0.0)",
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_rangeslider_visible=False,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    fig.update_xaxes(gridcolor="rgba(255, 255, 255, 0.05)")
    fig.update_yaxes(gridcolor="rgba(255, 255, 255, 0.05)")
    
    return fig

def chart_widget_component(ticker: str = "AAPL") -> rx.Component:
    return rx.plotly(
        data=render_plotly_chart(ticker),
        width="100%",
        height="450px"
    )
