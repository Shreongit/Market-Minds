"use client";

import React, { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { Sidebar } from "@/components/sidebar";
import { DecisionCard } from "@/components/decision-card";
import { DebateArena } from "@/components/debate-arena";
import { fetchDecision, fetchDebate, DecisionOutput, BullBearDebateOutput } from "@/lib/api";
import { Sparkles, Loader2, Download } from "lucide-react";

export default function AnalysisPage() {
  const params = useParams();
  const ticker = (params?.ticker as string || "AAPL").toUpperCase();

  const [decision, setDecision] = useState<DecisionOutput | null>(null);
  const [debate, setDebate] = useState<BullBearDebateOutput | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Promise.all([fetchDecision(ticker), fetchDebate(ticker)])
      .then(([dec, deb]) => {
        setDecision(dec);
        setDebate(deb);
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [ticker]);

  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-7xl">
        {/* Header */}
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
          <div>
            <div className="inline-flex items-center gap-2 bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-bold px-3 py-1 rounded-full mb-2">
              <Sparkles className="w-3.5 h-3.5" />
              Preserved Multi-Agent Pipeline Execution
            </div>
            <h1 className="text-3xl font-black text-white">
              Multi-Agent AI Intelligence Desk — {ticker}
            </h1>
          </div>

          <div className="flex items-center gap-3">
            <a
              href={`http://localhost:8000/api/v1/export/pdf/${ticker}`}
              target="_blank"
              rel="noopener noreferrer"
              className="bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-xs px-4 py-2.5 rounded-xl flex items-center gap-2 transition shadow-lg shadow-indigo-500/20"
            >
              <Download className="w-4 h-4" /> Download PDF Report
            </a>
          </div>
        </div>

        {loading ? (
          <div className="glass-card p-16 flex flex-col items-center justify-center gap-4 text-center">
            <Loader2 className="w-10 h-10 text-indigo-400 animate-spin" />
            <div>
              <div className="text-lg font-bold text-white">Running Multi-Agent AI Pipeline...</div>
              <p className="text-xs text-slate-400 mt-1">Executing Technical, Fundamental, Sentiment, Risk, and Decision agents.</p>
            </div>
          </div>
        ) : (
          <div className="space-y-6">
            {decision && <DecisionCard decision={decision} />}
            {debate && <DebateArena debate={debate} />}
          </div>
        )}
      </div>
    </div>
  );
}
