"use client";

import React, { useState } from "react";
import { Sidebar } from "@/components/sidebar";
import { Stethoscope, Plus, CheckCircle2, AlertTriangle, ShieldCheck } from "lucide-react";

export default function PortfolioPage() {
  const [positions, setPositions] = useState([
    { ticker: "AAPL", name: "Apple Inc", shares: 25, avg_price: 180.0, current_price: 224.50, sector: "Technology" },
    { ticker: "NVDA", name: "NVIDIA Corp", shares: 40, avg_price: 110.0, current_price: 128.50, sector: "Technology" },
    { ticker: "JPM", name: "JPMorgan Chase", shares: 15, avg_price: 145.0, current_price: 162.00, sector: "Financials" }
  ]);

  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-7xl">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-black text-white flex items-center gap-3">
              <Stethoscope className="w-7 h-7 text-indigo-400" /> AI Portfolio Doctor
            </h1>
            <p className="text-xs text-slate-400 mt-1">Evaluates portfolio health score, sector allocation, and correlation risks.</p>
          </div>
          <button className="bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold px-4 py-2.5 rounded-xl flex items-center gap-2 transition">
            <Plus className="w-4 h-4" /> Add Position
          </button>
        </div>

        {/* Portfolio Health Score Banner */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="glass-card p-6 flex flex-col gap-2">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Portfolio Health Score</span>
            <div className="flex items-baseline gap-3">
              <span className="text-4xl font-black text-emerald-400">82</span>
              <span className="text-xs font-bold bg-emerald-500/10 text-emerald-400 px-2.5 py-1 rounded-full border border-emerald-500/30">HEALTHY</span>
            </div>
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mt-2">
              <div className="bg-emerald-400 h-full rounded-full" style={{ width: "82%" }} />
            </div>
          </div>

          <div className="glass-card p-6 flex flex-col justify-between">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Diversification Index</span>
            <span className="text-3xl font-black text-indigo-400">74.5 <span className="text-sm font-semibold text-slate-500">/100</span></span>
            <span className="text-xs text-slate-400 font-medium">Top Sector: Technology (32.4%)</span>
          </div>

          <div className="glass-card p-6 flex flex-col justify-between">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Expected Annual Return</span>
            <span className="text-3xl font-black text-emerald-400">+14.2%</span>
            <span className="text-xs text-slate-400 font-medium">Portfolio Beta: 1.08 vs S&P 500</span>
          </div>
        </div>

        {/* AI Recommendations Box */}
        <div className="glass-card p-6 space-y-4">
          <div className="text-sm font-extrabold text-white flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-indigo-400" /> ACTIONABLE AI OPTIMIZATION SUGGESTIONS
          </div>
          <div className="space-y-3 text-xs">
            <div className="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800 flex items-start gap-3">
              <AlertTriangle className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
              <p className="text-slate-300">
                <strong className="text-white">Rebalance Technology Weight:</strong> Technology comprises 32.4% of total capital. Consider taking partial profits in NVDA to trim sector weight below 25%.
              </p>
            </div>

            <div className="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800 flex items-start gap-3">
              <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
              <p className="text-slate-300">
                <strong className="text-white">Add Defensive Dividend Anchor:</strong> Rotate capital into Healthcare or Consumer Staples (e.g. LLY or PG) to reduce drawdown risk.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
