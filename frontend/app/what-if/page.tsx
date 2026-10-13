"use client";

import React, { useState } from "react";
import { Sidebar } from "@/components/sidebar";
import { Cpu, AlertTriangle, ArrowRight, Shield } from "lucide-react";
import { simulateScenario } from "@/lib/api";

export default function WhatIfPage() {
  const [query, setQuery] = useState("What if crude oil reaches $120?");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleSimulate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;
    setLoading(true);
    try {
      const res = await simulateScenario(query);
      setResult(res);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-7xl">
        <div>
          <h1 className="text-3xl font-black text-white flex items-center gap-3">
            <Cpu className="w-7 h-7 text-indigo-400" /> Macro Scenario Simulator
          </h1>
          <p className="text-xs text-slate-400 mt-1">Ask natural-language macro questions to stress test sector and portfolio sensitivity.</p>
        </div>

        {/* Query Input Box */}
        <form onSubmit={handleSimulate} className="glass-card p-4 flex items-center gap-3">
          <input
            type="text"
            placeholder="e.g. What if crude oil reaches $120 per barrel? What if interest rates increase 50 bps?"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="flex-1 bg-slate-900 text-white placeholder-slate-400 border border-slate-800 rounded-xl px-4 py-3 text-sm font-semibold focus:outline-none focus:border-indigo-500"
          />
          <button
            type="submit"
            disabled={loading}
            className="bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-xs px-6 py-3.5 rounded-xl flex items-center gap-2 transition shadow-lg shadow-indigo-500/20"
          >
            {loading ? "Simulating..." : "Run Simulation"}
            <ArrowRight className="w-4 h-4" />
          </button>
        </form>

        {/* Results Card */}
        {result ? (
          <div className="glass-card p-6 space-y-4">
            <div className="flex justify-between items-center border-b border-slate-800 pb-3">
              <div className="text-base font-extrabold text-white flex items-center gap-2">
                <AlertTriangle className="w-5 h-5 text-amber-400" /> {result.scenario_title}
              </div>
              <span className="bg-rose-500/10 border border-rose-500/30 text-rose-400 text-xs font-bold px-3 py-1 rounded-full">
                {result.estimated_portfolio_impact_pct}% Estimated Impact
              </span>
            </div>

            <p className="text-sm text-slate-300 leading-relaxed">{result.description}</p>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="bg-rose-500/10 border border-rose-500/30 p-4 rounded-xl">
                <div className="text-xs font-bold text-rose-400 uppercase tracking-wider mb-2">Vulnerable Tickers</div>
                <div className="text-sm font-extrabold text-white">{result.vulnerable_tickers?.join(", ")}</div>
              </div>

              <div className="bg-emerald-500/10 border border-emerald-500/30 p-4 rounded-xl">
                <div className="text-xs font-bold text-emerald-400 uppercase tracking-wider mb-2">Benefiting Tickers</div>
                <div className="text-sm font-extrabold text-white">{result.benefiting_tickers?.join(", ")}</div>
              </div>
            </div>

            <div className="bg-slate-900/60 p-4 rounded-xl border-l-4 border-indigo-500">
              <div className="text-xs font-bold text-indigo-400 uppercase tracking-wider mb-1 flex items-center gap-1.5">
                <Shield className="w-4 h-4" /> Strategic Advice
              </div>
              <p className="text-sm text-slate-200">{result.strategic_advice}</p>
            </div>
          </div>
        ) : (
          <div className="glass-card p-12 text-center text-slate-400 text-sm">
            Enter a macro question above to trigger the Scenario Simulation Agent.
          </div>
        )}
      </div>
    </div>
  );
}
