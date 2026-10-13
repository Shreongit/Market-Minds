"use client";

import React from "react";
import { DecisionOutput } from "@/lib/api";
import { Shield, Target, AlertCircle, Clock, Zap, CheckCircle2, XCircle } from "lucide-react";

interface DecisionCardProps {
  decision: DecisionOutput;
}

export const DecisionCard: React.FC<DecisionCardProps> = ({ decision }) => {
  const getBadgeColor = (rec: string) => {
    if (rec === "BUY") return "bg-emerald-500/20 text-emerald-400 border-emerald-500/40";
    if (rec === "SELL") return "bg-rose-500/20 text-rose-400 border-rose-500/40";
    return "bg-amber-500/20 text-amber-400 border-amber-500/40";
  };

  return (
    <div className="glass-card p-6 w-full flex flex-col gap-6">
      {/* Header Row */}
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div>
          <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">
            Synthesized Decision Engine Output — {decision.ticker}
          </div>
          <div className="flex items-center gap-3 mt-2">
            <span className={`px-4 py-1.5 rounded-full border text-lg font-black tracking-wide ${getBadgeColor(decision.recommendation)}`}>
              {decision.recommendation}
            </span>
            <span className="text-sm text-slate-300 font-semibold">
              Confidence: <strong className="text-white font-bold">{decision.confidence}%</strong>
            </span>
          </div>
        </div>

        <div className="text-right">
          <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">
            Overall AI Score
          </div>
          <div className="text-3xl font-black text-indigo-400 mt-1">
            {decision.overall_ai_score}<span className="text-sm font-semibold text-slate-500">/100</span>
          </div>
        </div>
      </div>

      {/* Target Price Parameters Grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
          <div className="text-xs font-semibold text-slate-400 flex items-center gap-1.5">
            <Target className="w-3.5 h-3.5 text-emerald-400" /> Target Price
          </div>
          <div className="text-lg font-extrabold text-emerald-400 mt-1">
            ${decision.target_price.toFixed(2)}
          </div>
        </div>
        <div className="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
          <div className="text-xs font-semibold text-slate-400 flex items-center gap-1.5">
            <XCircle className="w-3.5 h-3.5 text-rose-400" /> Stop Loss
          </div>
          <div className="text-lg font-extrabold text-rose-400 mt-1">
            ${decision.stop_loss.toFixed(2)}
          </div>
        </div>
        <div className="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
          <div className="text-xs font-semibold text-slate-400 flex items-center gap-1.5">
            <Zap className="w-3.5 h-3.5 text-indigo-400" /> Entry Range
          </div>
          <div className="text-sm font-bold text-white mt-1">
            {decision.entry_range}
          </div>
        </div>
        <div className="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800">
          <div className="text-xs font-semibold text-slate-400 flex items-center gap-1.5">
            <Clock className="w-3.5 h-3.5 text-amber-400" /> Holding Period
          </div>
          <div className="text-sm font-bold text-white mt-1">
            {decision.suggested_holding_period}
          </div>
        </div>
      </div>

      {/* Independent Agent Scorecard */}
      <div>
        <div className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-3">
          Independent Multi-Agent Scorecard
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-slate-900/40 p-3.5 rounded-xl border border-slate-800/80">
            <div className="flex justify-between items-center text-xs font-bold mb-1">
              <span className="text-white">Technical Analysis</span>
              <span className="text-indigo-400">{decision.technical_score}/100</span>
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden mb-2">
              <div className="bg-indigo-500 h-full rounded-full" style={{ width: `${decision.technical_score}%` }} />
            </div>
            <p className="text-xs text-slate-400">{decision.technical_why}</p>
          </div>

          <div className="bg-slate-900/40 p-3.5 rounded-xl border border-slate-800/80">
            <div className="flex justify-between items-center text-xs font-bold mb-1">
              <span className="text-white">Fundamental Analysis</span>
              <span className="text-emerald-400">{decision.fundamental_score}/100</span>
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden mb-2">
              <div className="bg-emerald-500 h-full rounded-full" style={{ width: `${decision.fundamental_score}%` }} />
            </div>
            <p className="text-xs text-slate-400">{decision.fundamental_why}</p>
          </div>

          <div className="bg-slate-900/40 p-3.5 rounded-xl border border-slate-800/80">
            <div className="flex justify-between items-center text-xs font-bold mb-1">
              <span className="text-white">Market Sentiment</span>
              <span className="text-amber-400">{decision.sentiment_score}/100</span>
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden mb-2">
              <div className="bg-amber-500 h-full rounded-full" style={{ width: `${decision.sentiment_score}%` }} />
            </div>
            <p className="text-xs text-slate-400">{decision.sentiment_why}</p>
          </div>

          <div className="bg-slate-900/40 p-3.5 rounded-xl border border-slate-800/80">
            <div className="flex justify-between items-center text-xs font-bold mb-1">
              <span className="text-white">Risk Volatility</span>
              <span className="text-rose-400">{decision.risk_score}/100</span>
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden mb-2">
              <div className="bg-rose-500 h-full rounded-full" style={{ width: `${decision.risk_score}%` }} />
            </div>
            <p className="text-xs text-slate-400">{decision.risk_why}</p>
          </div>
        </div>
      </div>

      {/* Rationale & Transparency */}
      <div className="space-y-4">
        <div className="bg-slate-900/60 p-4 rounded-xl border-l-4 border-indigo-500">
          <div className="text-xs font-bold text-indigo-400 uppercase tracking-wider mb-1">
            Full Investment Rationale
          </div>
          <p className="text-sm text-slate-200 leading-relaxed font-normal">
            {decision.reasoning}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-rose-500/10 border border-rose-500/30 p-4 rounded-xl">
            <div className="text-xs font-bold text-rose-400 uppercase tracking-wider mb-1 flex items-center gap-1.5">
              <AlertCircle className="w-4 h-4" /> Thesis Invalidation Triggers
            </div>
            <p className="text-xs text-slate-300 whitespace-pre-line leading-relaxed">
              {decision.what_could_invalidate}
            </p>
          </div>

          <div className="bg-amber-500/10 border border-amber-500/30 p-4 rounded-xl">
            <div className="text-xs font-bold text-amber-400 uppercase tracking-wider mb-1 flex items-center gap-1.5">
              <Shield className="w-4 h-4" /> Stated Analysis Limitations
            </div>
            <p className="text-xs text-slate-300 leading-relaxed">
              {decision.known_limitations}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
