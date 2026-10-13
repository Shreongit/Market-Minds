"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import { Sidebar } from "@/components/sidebar";
import { fetchIndices, fetchMovers } from "@/lib/api";
import { useAppStore } from "@/lib/store";
import { TrendingUp, TrendingDown, Zap, Shield, Activity, RefreshCw } from "lucide-react";

export default function DashboardPage() {
  const { user, watchlist } = useAppStore();
  const [indices, setIndices] = useState<any[]>([]);
  const [movers, setMovers] = useState<any>({ gainers: [], losers: [] });

  useEffect(() => {
    const load = async () => {
      try {
        const ind = await fetchIndices();
        const mov = await fetchMovers();
        setIndices(ind);
        setMovers(mov);
      } catch (err) {
        console.error(err);
      }
    };
    load();
  }, []);

  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-7xl">
        {/* Header Greeting & Metrics */}
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
          <div>
            <h1 className="text-2xl font-black text-white">
              Good Morning, {user?.name || "Investor"} 👋
            </h1>
            <p className="text-xs text-slate-400 font-medium mt-0.5">
              Autonomous multi-agent synthesis active across global markets.
            </p>
          </div>
          <button
            onClick={() => window.location.reload()}
            className="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold px-4 py-2 rounded-xl border border-slate-700 transition"
          >
            <RefreshCw className="w-3.5 h-3.5 text-indigo-400" />
            Refresh Live Feeds
          </button>
        </div>

        {/* Portfolio & AI Key Metrics Grid */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="glass-card p-5 flex flex-col gap-1">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Total Portfolio Value</span>
            <span className="text-2xl font-black text-white">$128,450.00</span>
            <span className="text-xs font-bold text-emerald-400 flex items-center gap-1 mt-1">
              <TrendingUp className="w-3.5 h-3.5" /> +$2,450.00 (+1.95%) Today
            </span>
          </div>

          <div className="glass-card p-5 flex flex-col gap-1">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">AI Avg Confidence</span>
            <span className="text-2xl font-black text-indigo-400">86.4%</span>
            <span className="text-xs text-slate-400 font-medium mt-1">Based on 12 multi-agent scans</span>
          </div>

          <div className="glass-card p-5 flex flex-col gap-1">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Fear & Greed Index</span>
            <div className="flex items-baseline gap-2">
              <span className="text-2xl font-black text-emerald-400">68</span>
              <span className="text-xs font-extrabold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-md">GREED</span>
            </div>
            <span className="text-xs text-slate-400 font-medium mt-1">Bullish risk appetite active</span>
          </div>

          <div className="glass-card p-5 flex flex-col gap-1">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Portfolio Health</span>
            <span className="text-2xl font-black text-emerald-400">82 / 100</span>
            <span className="text-xs text-slate-400 font-medium mt-1">Low sector concentration risk</span>
          </div>
        </div>

        {/* Live Global Market Indices Ticker Cards */}
        <div>
          <div className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-3">
            Live Global Benchmark Indices
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {indices.slice(0, 4).map((idx) => (
              <div key={idx.symbol} className="glass-card p-4 flex flex-col justify-between">
                <div className="flex justify-between items-start">
                  <div>
                    <div className="text-sm font-extrabold text-white">{idx.name}</div>
                    <div className="text-[10px] text-slate-400 font-semibold">{idx.symbol}</div>
                  </div>
                  <span className={`text-xs font-bold ${idx.change_pct >= 0 ? "text-emerald-400" : "text-rose-400"}`}>
                    {idx.change_pct >= 0 ? "+" : ""}{idx.change_pct}%
                  </span>
                </div>
                <div className="text-lg font-black text-white mt-2">{idx.price}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Sector Heatmap & AI Insights */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="md:col-span-2 glass-card p-6 flex flex-col gap-4">
            <div className="flex justify-between items-center border-b border-slate-800 pb-3">
              <div className="text-sm font-extrabold text-white flex items-center gap-2">
                <Activity className="w-4 h-4 text-indigo-400" /> SECTOR PERFORMANCE HEATMAP
              </div>
              <span className="text-xs text-slate-400">Updated Real-Time</span>
            </div>

            <div className="grid grid-cols-3 gap-3">
              <div className="bg-emerald-500/10 border border-emerald-500/30 p-3.5 rounded-xl">
                <div className="text-xs font-bold text-white">Technology</div>
                <div className="text-base font-black text-emerald-400 mt-1">+1.80%</div>
              </div>
              <div className="bg-emerald-500/10 border border-emerald-500/30 p-3.5 rounded-xl">
                <div className="text-xs font-bold text-white">Energy</div>
                <div className="text-base font-black text-emerald-400 mt-1">+2.40%</div>
              </div>
              <div className="bg-rose-500/10 border border-rose-500/30 p-3.5 rounded-xl">
                <div className="text-xs font-bold text-white">Financials</div>
                <div className="text-base font-black text-rose-400 mt-1">-0.60%</div>
              </div>
              <div className="bg-emerald-500/10 border border-emerald-500/30 p-3.5 rounded-xl">
                <div className="text-xs font-bold text-white">Healthcare</div>
                <div className="text-base font-black text-emerald-400 mt-1">+0.40%</div>
              </div>
              <div className="bg-rose-500/10 border border-rose-500/30 p-3.5 rounded-xl">
                <div className="text-xs font-bold text-white">Consumer Disc.</div>
                <div className="text-base font-black text-rose-400 mt-1">-1.20%</div>
              </div>
              <div className="bg-amber-500/10 border border-amber-500/30 p-3.5 rounded-xl">
                <div className="text-xs font-bold text-white">Industrials</div>
                <div className="text-base font-black text-amber-400 mt-1">+0.10%</div>
              </div>
            </div>
          </div>

          {/* AI Insights & Quick Analysis Feed */}
          <div className="glass-card p-6 flex flex-col gap-4">
            <div className="text-sm font-extrabold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
              <Zap className="w-4 h-4 text-amber-400" /> REAL-TIME AI INSIGHTS
            </div>

            <div className="space-y-3">
              <div className="bg-slate-900/60 p-3 rounded-xl border-l-4 border-emerald-500 text-xs space-y-1">
                <div className="font-bold text-white">BULLISH BREAKOUT: NVDA</div>
                <p className="text-slate-400">Crossed 50-day SMA ($122.50) on 2.1x volume. Technical score 92/100.</p>
              </div>

              <div className="bg-slate-900/60 p-3 rounded-xl border-l-4 border-indigo-500 text-xs space-y-1">
                <div className="font-bold text-white">EARNINGS SURPRISE: AAPL</div>
                <p className="text-slate-400">Services revenue expanded +14% YoY, beating consensus estimates.</p>
              </div>
            </div>
          </div>
        </div>

        {/* Top Market Movers */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="glass-card p-6">
            <div className="text-sm font-extrabold text-emerald-400 mb-4 flex items-center gap-2">
              <TrendingUp className="w-4 h-4" /> TOP GAINERS TODAY
            </div>
            <div className="space-y-2">
              {movers.gainers?.map((g: any) => (
                <Link
                  key={g.ticker}
                  href={`/stock/${g.ticker}`}
                  className="flex items-center justify-between bg-slate-900/40 hover:bg-slate-800 p-3 rounded-xl border border-slate-800 transition"
                >
                  <div>
                    <div className="text-sm font-bold text-white">{g.ticker}</div>
                    <div className="text-xs text-slate-400">{g.name}</div>
                  </div>
                  <div className="text-right">
                    <div className="text-sm font-extrabold text-white">${g.price}</div>
                    <div className="text-xs font-bold text-emerald-400">+{g.change_pct}%</div>
                  </div>
                </Link>
              ))}
            </div>
          </div>

          <div className="glass-card p-6">
            <div className="text-sm font-extrabold text-rose-400 mb-4 flex items-center gap-2">
              <TrendingDown className="w-4 h-4" /> TOP LOSERS TODAY
            </div>
            <div className="space-y-2">
              {movers.losers?.map((l: any) => (
                <Link
                  key={l.ticker}
                  href={`/stock/${l.ticker}`}
                  className="flex items-center justify-between bg-slate-900/40 hover:bg-slate-800 p-3 rounded-xl border border-slate-800 transition"
                >
                  <div>
                    <div className="text-sm font-bold text-white">{l.ticker}</div>
                    <div className="text-xs text-slate-400">{l.name}</div>
                  </div>
                  <div className="text-right">
                    <div className="text-sm font-extrabold text-white">${l.price}</div>
                    <div className="text-xs font-bold text-rose-400">{l.change_pct}%</div>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
