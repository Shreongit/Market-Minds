"use client";

import React, { useState } from "react";
import { Sidebar } from "@/components/sidebar";
import { Download, FileText, Table, FileSpreadsheet } from "lucide-react";

export default function ExportsPage() {
  const [ticker, setTicker] = useState("AAPL");

  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-5xl">
        <div>
          <h1 className="text-3xl font-black text-white flex items-center gap-3">
            <Download className="w-7 h-7 text-indigo-400" /> Research Report Export Hub
          </h1>
          <p className="text-xs text-slate-400 mt-1">Generate institutional-grade PDF reports, Excel models, or CSV trade logs.</p>
        </div>

        <div className="glass-card p-4 flex items-center gap-3">
          <label className="text-xs font-bold text-slate-400">Select Stock Ticker:</label>
          <input
            type="text"
            value={ticker}
            onChange={(e) => setTicker(e.target.value.toUpperCase())}
            className="bg-slate-900 text-white font-bold border border-slate-800 rounded-xl px-4 py-2 text-sm uppercase focus:outline-none focus:border-indigo-500 w-36"
          />
        </div>

        <div className="space-y-4">
          <div className="glass-card p-6 flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="bg-indigo-600/20 p-3 rounded-xl border border-indigo-500/30">
                <FileText className="w-6 h-6 text-indigo-400" />
              </div>
              <div>
                <div className="text-base font-extrabold text-white">Full Equity Research Report (PDF)</div>
                <p className="text-xs text-slate-400">Multi-agent scorecard, price targets, target entry range, reasoning narrative, and invalidation triggers.</p>
              </div>
            </div>
            <a
              href={`http://localhost:8000/api/v1/export/pdf/${ticker}`}
              target="_blank"
              rel="noopener noreferrer"
              className="bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs px-5 py-2.5 rounded-xl flex items-center gap-2 transition shadow-lg shadow-indigo-500/20"
            >
              <Download className="w-4 h-4" /> Download PDF
            </a>
          </div>

          <div className="glass-card p-6 flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="bg-emerald-600/20 p-3 rounded-xl border border-emerald-500/30">
                <Table className="w-6 h-6 text-emerald-400" />
              </div>
              <div>
                <div className="text-base font-extrabold text-white">Decision & Metrics Data Log (CSV)</div>
                <p className="text-xs text-slate-400">Raw quantitative decision scores, target prices, stop-loss limits, and indicator metrics.</p>
              </div>
            </div>
            <a
              href={`http://localhost:8000/api/v1/export/csv/${ticker}`}
              target="_blank"
              rel="noopener noreferrer"
              className="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs px-5 py-2.5 rounded-xl flex items-center gap-2 transition shadow-lg shadow-emerald-500/20"
            >
              <Download className="w-4 h-4" /> Download CSV
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
