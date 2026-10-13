"use client";

import React, { useEffect, useState } from "react";
import { Sidebar } from "@/components/sidebar";
import { fetchNews } from "@/lib/api";
import { Bell, Zap, Filter } from "lucide-react";

export default function NewsPage() {
  const [news, setNews] = useState<any[]>([]);

  useEffect(() => {
    fetchNews().then(setNews).catch(console.error);
  }, []);

  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-7xl">
        <div>
          <h1 className="text-3xl font-black text-white flex items-center gap-3">
            <Bell className="w-7 h-7 text-indigo-400" /> News Impact Engine & Smart Alerts
          </h1>
          <p className="text-xs text-slate-400 mt-1">Real-time NLP sentiment classification, ticker impact ratings, and context-driven alerts.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* News Feed */}
          <div className="space-y-4">
            <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">Classified Financial News Feed</div>
            {news.map((item, idx) => (
              <div key={idx} className="glass-card p-5 space-y-2">
                <div className="flex justify-between items-center text-xs">
                  <span className={`font-bold px-2.5 py-0.5 rounded-md ${item.sentiment_label === "POSITIVE" ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/30" : "bg-rose-500/10 text-rose-400 border border-rose-500/30"}`}>
                    {item.sentiment_label} ({item.sentiment_score > 0 ? "+" : ""}{item.sentiment_score})
                  </span>
                  <span className="bg-purple-500/10 text-purple-400 font-bold px-2 py-0.5 rounded border border-purple-500/30">
                    {item.impact_level} IMPACT
                  </span>
                </div>
                <h3 className="text-sm font-bold text-white leading-snug">{item.title}</h3>
                <p className="text-xs text-slate-400 line-clamp-2">{item.summary}</p>
              </div>
            ))}
          </div>

          {/* Smart Alerts Feed */}
          <div className="space-y-4">
            <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">Context-Driven Smart Alerts</div>
            <div className="glass-card p-5 border-l-4 border-emerald-500 space-y-1">
              <div className="flex justify-between items-center">
                <span className="text-xs font-bold text-emerald-400 flex items-center gap-1"><Zap className="w-3.5 h-3.5" /> BULLISH BREAKOUT: NVDA</span>
                <span className="text-[10px] font-bold text-slate-400">94% Confidence</span>
              </div>
              <p className="text-xs text-slate-300">NVDA crossed 50-day SMA ($122.50) on 2.1x average daily volume.</p>
            </div>

            <div className="glass-card p-5 border-l-4 border-rose-500 space-y-1">
              <div className="flex justify-between items-center">
                <span className="text-xs font-bold text-rose-400 flex items-center gap-1"><Zap className="w-3.5 h-3.5" /> UNUSUAL INSTITUTIONAL SELLING: TSLA</span>
                <span className="text-[10px] font-bold text-slate-400">88% Confidence</span>
              </div>
              <p className="text-xs text-slate-300">Block trade distribution detected at key resistance ($230.00).</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
