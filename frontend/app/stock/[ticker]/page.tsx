"use client";

import React, { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import { Sidebar } from "@/components/sidebar";
import { TradingViewChart } from "@/components/tradingview-chart";
import { fetchQuote } from "@/lib/api";
import { Sparkles, ArrowUpRight, DollarSign, TrendingUp, Building2, BarChart2 } from "lucide-react";

export default function StockPage() {
  const params = useParams();
  const ticker = (params?.ticker as string || "AAPL").toUpperCase();
  const [quote, setQuote] = useState<any>(null);

  useEffect(() => {
    fetchQuote(ticker)
      .then(setQuote)
      .catch(console.error);
  }, [ticker]);

  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-7xl">
        {/* Header Bar */}
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
          <div>
            <div className="flex items-center gap-3">
              <h1 className="text-3xl font-black text-white">{quote?.company_name || ticker} ({ticker})</h1>
              <span className="bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-extrabold px-3 py-1 rounded-full uppercase">
                {quote?.sector || "Technology"}
              </span>
            </div>
            <div className="flex items-baseline gap-3 mt-2">
              <span className="text-3xl font-black text-white">${quote?.price?.toFixed(2) || "224.50"}</span>
              <span className={`text-base font-bold ${quote?.change >= 0 ? "text-emerald-400" : "text-rose-400"}`}>
                {quote?.change >= 0 ? "+" : ""}${quote?.change?.toFixed(2) || "3.40"} ({quote?.change_percent >= 0 ? "+" : ""}{quote?.change_percent || 1.54}%)
              </span>
            </div>
          </div>

          <Link
            href={`/analysis/${ticker}`}
            className="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white font-extrabold text-sm px-6 py-3 rounded-xl flex items-center gap-2 transition shadow-xl shadow-indigo-500/25"
          >
            <Sparkles className="w-4 h-4" />
            Run Multi-Agent AI Analysis
          </Link>
        </div>

        {/* Live TradingView Candlestick Chart Embed */}
        <div className="glass-card p-4">
          <div className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-3 flex items-center gap-2">
            <BarChart2 className="w-4 h-4 text-indigo-400" /> Interactive TradingView Real-Time Candlestick Chart
          </div>
          <TradingViewChart symbol={ticker} />
        </div>

        {/* Key Fundamentals Grid */}
        <div>
          <div className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-3">
            Company Financial Metrics & Valuation
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="glass-card p-4">
              <div className="text-xs text-slate-400 font-bold">P/E Ratio</div>
              <div className="text-xl font-extrabold text-white mt-1">28.5</div>
              <div className="text-[11px] text-slate-500">Trailing 12 Months</div>
            </div>
            <div className="glass-card p-4">
              <div className="text-xs text-slate-400 font-bold">Market Cap</div>
              <div className="text-xl font-extrabold text-white mt-1">$3.45 Trillion</div>
              <div className="text-[11px] text-slate-500">Large-Cap Growth</div>
            </div>
            <div className="glass-card p-4">
              <div className="text-xs text-slate-400 font-bold">52-Week High</div>
              <div className="text-xl font-extrabold text-emerald-400 mt-1">${quote?.fifty_two_week_high || "237.23"}</div>
              <div className="text-[11px] text-slate-500">Peak Valuation</div>
            </div>
            <div className="glass-card p-4">
              <div className="text-xs text-slate-400 font-bold">52-Week Low</div>
              <div className="text-xl font-extrabold text-rose-400 mt-1">${quote?.fifty_two_week_low || "164.08"}</div>
              <div className="text-[11px] text-slate-500">Support Floor</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
