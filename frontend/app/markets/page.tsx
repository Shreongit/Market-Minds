"use client";

import React, { useEffect, useState } from "react";
import { Sidebar } from "@/components/sidebar";
import { fetchIndices } from "@/lib/api";
import { Globe, TrendingUp, TrendingDown, RefreshCw } from "lucide-react";

export default function MarketsPage() {
  const [indices, setIndices] = useState<any[]>([]);

  useEffect(() => {
    fetchIndices().then(setIndices).catch(console.error);
  }, []);

  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-7xl">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-black text-white flex items-center gap-3">
              <Globe className="w-7 h-7 text-indigo-400" /> Global Markets Command Center
            </h1>
            <p className="text-xs text-slate-400 mt-1">Live real-time indices across Equities, Forex, Commodities, and Crypto.</p>
          </div>
          <button
            onClick={() => fetchIndices().then(setIndices)}
            className="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold px-4 py-2 rounded-xl border border-slate-700 transition"
          >
            <RefreshCw className="w-3.5 h-3.5 text-indigo-400" /> Refresh Feeds
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {indices.map((idx) => (
            <div key={idx.symbol} className="glass-card p-5 flex flex-col justify-between">
              <div>
                <div className="flex justify-between items-center">
                  <span className="text-xs font-bold text-indigo-400 uppercase tracking-wider">{idx.category}</span>
                  <span className={`text-xs font-bold flex items-center gap-1 ${idx.change_pct >= 0 ? "text-emerald-400" : "text-rose-400"}`}>
                    {idx.change_pct >= 0 ? <TrendingUp className="w-3.5 h-3.5" /> : <TrendingDown className="w-3.5 h-3.5" />}
                    {idx.change_pct}%
                  </span>
                </div>
                <div className="text-lg font-black text-white mt-2">{idx.name}</div>
                <div className="text-[11px] text-slate-400 font-semibold">{idx.symbol}</div>
              </div>
              <div className="text-2xl font-black text-white mt-4">{idx.price}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
