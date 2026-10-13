"use client";

import React from "react";
import { BullBearDebateOutput } from "@/lib/api";
import { TrendingUp, TrendingDown, Gavel, Swords } from "lucide-react";

interface DebateArenaProps {
  debate: BullBearDebateOutput;
}

export const DebateArena: React.FC<DebateArenaProps> = ({ debate }) => {
  return (
    <div className="glass-card p-6 w-full flex flex-col gap-6">
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div className="flex items-center gap-3">
          <div className="bg-indigo-600/20 p-2.5 rounded-xl border border-indigo-500/30">
            <Swords className="w-5 h-5 text-indigo-400" />
          </div>
          <div>
            <div className="text-base font-extrabold text-white">
              Bull vs. Bear AI Debate Arena — {debate.ticker}
            </div>
            <div className="text-xs text-slate-400 font-medium">
              Opposing LLM Personas Argue Thesis & Impartial Judge Settlement
            </div>
          </div>
        </div>
        <span className="bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-bold px-3 py-1 rounded-full">
          AI Multi-Persona Engine
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Bull Persona Bubble */}
        <div className="bg-emerald-500/10 border border-emerald-500/30 p-5 rounded-2xl flex flex-col gap-3">
          <div className="flex items-center gap-2 text-emerald-400 font-bold text-sm">
            <TrendingUp className="w-4 h-4" /> BULL PERSONA ARGUMENT
          </div>
          <p className="text-sm text-slate-200 leading-relaxed">
            {debate.bull_case}
          </p>
        </div>

        {/* Bear Persona Bubble */}
        <div className="bg-rose-500/10 border border-rose-500/30 p-5 rounded-2xl flex flex-col gap-3">
          <div className="flex items-center gap-2 text-rose-400 font-bold text-sm">
            <TrendingDown className="w-4 h-4" /> BEAR PERSONA ARGUMENT
          </div>
          <p className="text-sm text-slate-200 leading-relaxed">
            {debate.bear_case}
          </p>
        </div>
      </div>

      {/* Judge Verdict Box */}
      <div className="bg-amber-500/10 border border-amber-500/30 p-5 rounded-2xl flex flex-col gap-2">
        <div className="flex items-center gap-2 text-amber-400 font-bold text-sm">
          <Gavel className="w-4 h-4" /> IMPARTIAL JUDGE VERDICT
        </div>
        <p className="text-sm font-medium text-white leading-relaxed">
          {debate.judge_verdict}
        </p>
      </div>
    </div>
  );
};
