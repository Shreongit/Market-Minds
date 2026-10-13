"use client";

import React from "react";
import Link from "next/link";
import { motion } from "framer-motion";
import { Sparkles, ArrowRight, ShieldCheck, Cpu, TrendingUp, LineChart, Swords, CheckCircle2, ChevronDown } from "lucide-react";

export default function LandingPage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#0F172A] overflow-hidden">
      {/* Hero Section */}
      <section className="relative pt-20 pb-16 px-6 text-center max-w-6xl mx-auto flex flex-col items-center">
        {/* Glowing Background Glow */}
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[300px] bg-indigo-500/20 blur-[120px] rounded-full pointer-events-none" />

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="inline-flex items-center gap-2 bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-extrabold px-4 py-2 rounded-full mb-6"
        >
          <Sparkles className="w-4 h-4" />
          Autonomous Multi-Agent Equity Research Committee
        </motion.div>

        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
          className="text-4xl md:text-6xl font-black text-white tracking-tight leading-tight max-w-4xl"
        >
          Invest Like an Institutional Desk with{" "}
          <span className="bg-gradient-to-r from-indigo-400 via-purple-400 to-blue-400 bg-clip-text text-transparent">
            Multi-Agent AI Intelligence
          </span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="text-slate-400 text-lg md:text-xl max-w-2xl mt-6 leading-relaxed font-medium"
        >
          MarketMind AI deploys 7 specialized, independent AI agents (Technical, Fundamental, Sentiment, Risk, Portfolio, Scenario, and Debate) to analyze global markets and synthesize transparent, fully explained investment calls.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.3 }}
          className="flex flex-wrap justify-center gap-4 mt-8"
        >
          <Link
            href="/dashboard"
            className="bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-base px-8 py-3.5 rounded-2xl flex items-center gap-2 transition shadow-xl shadow-indigo-500/25"
          >
            Launch Command Center
            <ArrowRight className="w-5 h-5" />
          </Link>
          <Link
            href="/stock/AAPL"
            className="bg-slate-800 hover:bg-slate-700 text-white font-bold text-base px-8 py-3.5 rounded-2xl border border-slate-700 transition"
          >
            Explore AAPL Analysis
          </Link>
        </motion.div>

        {/* Ticker Carousel */}
        <div className="w-full mt-14 overflow-hidden border-y border-slate-800/80 py-3 bg-slate-900/40">
          <div className="flex gap-8 justify-around text-xs font-bold text-slate-300">
            <span className="flex items-center gap-2"><strong className="text-white">AAPL</strong> $224.50 <span className="text-emerald-400">+1.54%</span></span>
            <span className="flex items-center gap-2"><strong className="text-white">NVDA</strong> $128.50 <span className="text-emerald-400">+5.80%</span></span>
            <span className="flex items-center gap-2"><strong className="text-white">TSLA</strong> $224.10 <span className="text-emerald-400">+4.20%</span></span>
            <span className="flex items-center gap-2"><strong className="text-white">NIFTY 50</strong> 24,820.50 <span className="text-emerald-400">+0.59%</span></span>
            <span className="flex items-center gap-2"><strong className="text-white">S&P 500</strong> 5,432.10 <span className="text-emerald-400">+0.45%</span></span>
          </div>
        </div>
      </section>

      {/* Feature Cards Grid */}
      <section className="py-16 px-6 max-w-6xl mx-auto">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-black text-white">Built Like a Real Equity Research Committee</h2>
          <p className="text-slate-400 text-sm mt-2">Zero black boxes. Every call is traceable to inputs.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="glass-card p-6 flex flex-col gap-3">
            <div className="bg-indigo-600/20 w-10 h-10 rounded-xl flex items-center justify-center border border-indigo-500/30">
              <Cpu className="w-5 h-5 text-indigo-400" />
            </div>
            <h3 className="text-lg font-bold text-white">7 Independent Agents</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Technical, Fundamental, Sentiment, Risk, Portfolio, Scenario, and Debate agents communicate exclusively through typed Pydantic contracts.
            </p>
          </div>

          <div className="glass-card p-6 flex flex-col gap-3">
            <div className="bg-emerald-600/20 w-10 h-10 rounded-xl flex items-center justify-center border border-emerald-500/30">
              <ShieldCheck className="w-5 h-5 text-emerald-400" />
            </div>
            <h3 className="text-lg font-bold text-white">Decision Synthesizer</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Synthesizes sub-agent views into a strict BUY/SELL/HOLD decision with confidence rating, target price, stop loss, and invalidation points.
            </p>
          </div>

          <div className="glass-card p-6 flex flex-col gap-3">
            <div className="bg-amber-600/20 w-10 h-10 rounded-xl flex items-center justify-center border border-amber-500/30">
              <Swords className="w-5 h-5 text-amber-400" />
            </div>
            <h3 className="text-lg font-bold text-white">Bull vs. Bear Debate</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Bull and Bear LLM personas argue opposing theses on a stock, followed by an impartial Judge agent verdict.
            </p>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="py-16 px-6 max-w-5xl mx-auto text-center">
        <h2 className="text-3xl font-black text-white mb-2">Simple Transparent Pricing</h2>
        <p className="text-slate-400 text-sm mb-10">Start free, upgrade for institutional Copilot capabilities.</p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
          <div className="glass-card p-6 flex flex-col justify-between">
            <div>
              <div className="text-lg font-bold text-white">Free Starter</div>
              <div className="text-3xl font-black text-white mt-2">$0<span className="text-xs text-slate-500">/mo</span></div>
              <ul className="text-xs text-slate-300 space-y-2 mt-4">
                <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> 5 Stock Queries/day</li>
                <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> Standard Technical Signals</li>
              </ul>
            </div>
            <Link href="/dashboard" className="mt-6 bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs text-center py-2.5 rounded-xl border border-slate-700 transition">Get Started</Link>
          </div>

          <div className="glass-card p-6 border-2 border-indigo-500 flex flex-col justify-between relative">
            <span className="absolute -top-3 right-4 bg-indigo-600 text-white text-[10px] font-extrabold px-3 py-1 rounded-full uppercase">Popular</span>
            <div>
              <div className="text-lg font-bold text-white">Pro Copilot</div>
              <div className="text-3xl font-black text-indigo-400 mt-2">$29<span className="text-xs text-slate-500">/mo</span></div>
              <ul className="text-xs text-slate-300 space-y-2 mt-4">
                <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-indigo-400" /> Unlimited AI Agent Reports</li>
                <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-indigo-400" /> Full Bull vs Bear Debates</li>
                <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-indigo-400" /> AI Portfolio Doctor & Backtester</li>
              </ul>
            </div>
            <Link href="/dashboard" className="mt-6 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs text-center py-2.5 rounded-xl transition shadow-lg shadow-indigo-500/20">Upgrade to Pro</Link>
          </div>

          <div className="glass-card p-6 flex flex-col justify-between">
            <div>
              <div className="text-lg font-bold text-white">Institutional</div>
              <div className="text-3xl font-black text-white mt-2">$199<span className="text-xs text-slate-500">/mo</span></div>
              <ul className="text-xs text-slate-300 space-y-2 mt-4">
                <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> WebSockets Real-Time Stream</li>
                <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> Custom Strategy API Webhooks</li>
              </ul>
            </div>
            <Link href="/dashboard" className="mt-6 bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs text-center py-2.5 rounded-xl border border-slate-700 transition">Contact Desk</Link>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-800 py-8 px-6 text-center text-xs text-slate-500 mt-auto">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
          <div>© 2026 MarketMind AI. All rights reserved. Production Multi-Agent Copilot Platform.</div>
          <div className="flex gap-6 font-semibold text-slate-400">
            <Link href="/dashboard">Dashboard</Link>
            <Link href="/stock/AAPL">Intelligence Hub</Link>
            <Link href="/markets">Markets</Link>
          </div>
        </div>
      </footer>
    </div>
  );
}
