"use client";

import React from "react";
import { Sidebar } from "@/components/sidebar";
import { FlaskConical, Play, TrendingUp, BarChart2 } from "lucide-react";

export default function StrategyPage() {
  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-7xl">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-black text-white flex items-center gap-3">
              <FlaskConical className="w-7 h-7 text-indigo-400" /> Strategy Builder & Backtest Lab
            </h1>
            <p className="text-xs text-slate-400 mt-1">Build technical strategies and backtest against multi-year historical data.</p>
          </div>
          <button className="bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold px-5 py-2.5 rounded-xl flex items-center gap-2 transition shadow-lg shadow-indigo-500/20">
            <Play className="w-4 h-4 fill-white" /> Run Historical Backtest
          </button>
        </div>

        {/* Rule Builder Card */}
        <div className="glass-card p-6 space-y-4">
          <div className="text-sm font-extrabold text-white">STRATEGY RULES CONFIGURATION</div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div>
              <label className="text-xs font-bold text-slate-400 block mb-1">Target Ticker</label>
              <input type="text" defaultValue="AAPL" className="w-full bg-slate-900 border border-slate-800 rounded-xl px-3 py-2 text-sm text-white font-bold" />
            </div>
            <div>
              <label className="text-xs font-bold text-slate-400 block mb-1">Initial Capital ($)</label>
              <input type="number" defaultValue={10000} className="w-full bg-slate-900 border border-slate-800 rounded-xl px-3 py-2 text-sm text-white font-bold" />
            </div>
            <div>
              <label className="text-xs font-bold text-slate-400 block mb-1">Stop Loss (%)</label>
              <input type="number" defaultValue={5.0} className="w-full bg-slate-900 border border-slate-800 rounded-xl px-3 py-2 text-sm text-white font-bold" />
            </div>
            <div>
              <label className="text-xs font-bold text-slate-400 block mb-1">Take Profit (%)</label>
              <input type="number" defaultValue={15.0} className="w-full bg-slate-900 border border-slate-800 rounded-xl px-3 py-2 text-sm text-white font-bold" />
            </div>
          </div>
        </div>

        {/* Backtest Results Cards */}
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
          <div className="glass-card p-4">
            <div className="text-xs text-slate-400 font-bold">Total Return</div>
            <div className="text-2xl font-black text-emerald-400 mt-1">+28.4%</div>
            <div className="text-[11px] text-slate-500">vs Benchmark +14.2%</div>
          </div>
          <div className="glass-card p-4">
            <div className="text-xs text-slate-400 font-bold">CAGR</div>
            <div className="text-2xl font-black text-indigo-400 mt-1">26.8%</div>
            <div className="text-[11px] text-slate-500">Annualized Return</div>
          </div>
          <div className="glass-card p-4">
            <div className="text-xs text-slate-400 font-bold">Sharpe Ratio</div>
            <div className="text-2xl font-black text-amber-400 mt-1">1.84</div>
            <div className="text-[11px] text-slate-500">Risk-Adjusted</div>
          </div>
          <div className="glass-card p-4">
            <div className="text-xs text-slate-400 font-bold">Max Drawdown</div>
            <div className="text-2xl font-black text-rose-400 mt-1">-8.2%</div>
            <div className="text-[11px] text-slate-500">Peak-to-Trough Loss</div>
          </div>
          <div className="glass-card p-4">
            <div className="text-xs text-slate-400 font-bold">Win Rate</div>
            <div className="text-2xl font-black text-emerald-400 mt-1">68.5%</div>
            <div className="text-[11px] text-slate-500">14 Wins / 6 Losses</div>
          </div>
        </div>
      </div>
    </div>
  );
}
