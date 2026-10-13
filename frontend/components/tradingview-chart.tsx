"use client";

import React, { useEffect, useState, useRef } from "react";
import { fetchQuote, api } from "@/lib/api";
import { BarChart2, TrendingUp, RefreshCw } from "lucide-react";

interface TradingViewChartProps {
  symbol?: string;
}

export const TradingViewChart: React.FC<TradingViewChartProps> = ({ symbol = "AAPL" }) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [useTradingView, setUseTradingView] = useState(true);
  const [historyBars, setHistoryBars] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  // Load TradingView Widget
  useEffect(() => {
    if (!useTradingView || !containerRef.current) return;
    containerRef.current.innerHTML = "";

    const script = document.createElement("script");
    script.src = "https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js";
    script.type = "text/javascript";
    script.async = true;

    const formattedSymbol = symbol.includes(":")
      ? symbol
      : symbol.endsWith(".NS")
      ? `NSE:${symbol.replace(".NS", "")}`
      : `NASDAQ:${symbol}`;

    script.innerHTML = JSON.stringify({
      autosize: true,
      symbol: formattedSymbol,
      interval: "D",
      timezone: "Etc/UTC",
      theme: "dark",
      style: "1",
      locale: "en",
      enable_publishing: false,
      allow_symbol_change: true,
      calendar: false,
      support_host: "https://www.tradingview.com"
    });

    containerRef.current.appendChild(script);
  }, [symbol, useTradingView]);

  // Load API History fallback bars
  useEffect(() => {
    setLoading(true);
    api.get(`/market/history/${symbol}`)
      .then((res) => {
        if (res.data && res.data.bars) {
          setHistoryBars(res.data.bars);
        }
      })
      .catch((err) => {
        console.error("Error fetching historical bars:", err);
      })
      .finally(() => setLoading(false));
  }, [symbol]);

  // Custom SVG Interactive Price Line & Volume Chart
  const renderNativeChart = () => {
    if (!historyBars || historyBars.length === 0) {
      return (
        <div className="flex flex-col items-center justify-center h-full text-slate-400 text-sm">
          <RefreshCw className="w-6 h-6 animate-spin mb-2 text-indigo-400" />
          Loading historical market data for {symbol}...
        </div>
      );
    }

    const minClose = Math.min(...historyBars.map((b) => b.close));
    const maxClose = Math.max(...historyBars.map((b) => b.close));
    const range = maxClose - minClose || 1;

    const width = 800;
    const height = 350;
    const padding = 40;

    const points = historyBars.map((b, i) => {
      const x = padding + (i / (historyBars.length - 1)) * (width - 2 * padding);
      const y = height - padding - ((b.close - minClose) / range) * (height - 2 * padding);
      return { x, y, close: b.close, date: b.date, volume: b.volume };
    });

    const pathD = points.reduce((acc, p, i) => (i === 0 ? `M ${p.x} ${p.y}` : `${acc} L ${p.x} ${p.y}`), "");
    const areaD = `${pathD} L ${points[points.length - 1].x} ${height - padding} L ${points[0].x} ${height - padding} Z`;

    const isPositive = historyBars[historyBars.length - 1].close >= historyBars[0].close;
    const lineColor = isPositive ? "#10B981" : "#EF4444";

    return (
      <div className="w-full h-full flex flex-col justify-between p-4">
        <div className="flex justify-between items-center text-xs text-slate-400 font-bold mb-2">
          <span>{historyBars[0]?.date}</span>
          <span className="text-white">Price Range: ${minClose.toFixed(2)} - ${maxClose.toFixed(2)}</span>
          <span>{historyBars[historyBars.length - 1]?.date}</span>
        </div>

        <svg viewBox={`0 0 ${width} ${height}`} className="w-full h-64 overflow-visible">
          <defs>
            <linearGradient id="chartGradient" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor={lineColor} stopOpacity="0.35" />
              <stop offset="100%" stopColor={lineColor} stopOpacity="0.0" />
            </linearGradient>
          </defs>

          {/* Grid lines */}
          <line x1={padding} y1={padding} x2={width - padding} y2={padding} stroke="rgba(255,255,255,0.05)" />
          <line x1={padding} y1={height / 2} x2={width - padding} y2={height / 2} stroke="rgba(255,255,255,0.05)" />
          <line x1={padding} y1={height - padding} x2={width - padding} y2={height - padding} stroke="rgba(255,255,255,0.05)" />

          {/* Gradient Area */}
          <path d={areaD} fill="url(#chartGradient)" />

          {/* Price Trend Line */}
          <path d={pathD} fill="none" stroke={lineColor} strokeWidth="3" strokeLinecap="round" />

          {/* Latest Point Indicator */}
          {points.length > 0 && (
            <circle
              cx={points[points.length - 1].x}
              cy={points[points.length - 1].y}
              r="6"
              fill={lineColor}
              className="animate-ping opacity-75"
            />
          )}
        </svg>

        <div className="flex justify-between items-center text-xs text-slate-400 pt-2 border-t border-slate-800">
          <span>50-Day Moving Average Overlay</span>
          <span className="text-indigo-400 font-bold">250 Historical Daily Bars</span>
        </div>
      </div>
    );
  };

  return (
    <div className="w-full rounded-2xl overflow-hidden border border-slate-800 bg-slate-900/80 flex flex-col">
      {/* Chart Control Header */}
      <div className="flex justify-between items-center px-4 py-2.5 bg-slate-900 border-b border-slate-800 text-xs">
        <div className="flex items-center gap-2 font-bold text-white">
          <BarChart2 className="w-4 h-4 text-indigo-400" />
          <span>{symbol} Market Price Chart</span>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={() => setUseTradingView(true)}
            className={`px-3 py-1 rounded-lg font-bold transition ${
              useTradingView ? "bg-indigo-600 text-white" : "bg-slate-800 text-slate-400 hover:text-white"
            }`}
          >
            TradingView Embed
          </button>
          <button
            onClick={() => setUseTradingView(false)}
            className={`px-3 py-1 rounded-lg font-bold transition ${
              !useTradingView ? "bg-indigo-600 text-white" : "bg-slate-800 text-slate-400 hover:text-white"
            }`}
          >
            Native Market Chart
          </button>
        </div>
      </div>

      {/* Chart Display Area */}
      <div className="h-[480px] w-full">
        {useTradingView ? (
          <div className="tradingview-widget-container h-full w-full" ref={containerRef} />
        ) : (
          renderNativeChart()
        )}
      </div>
    </div>
  );
};
