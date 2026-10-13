"use client";

import React, { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Search, Sparkles, TrendingUp, ShieldCheck, User } from "lucide-react";
import { useAppStore } from "@/lib/store";

export const Navbar = () => {
  const router = useRouter();
  const { activeTicker, setActiveTicker, user } = useAppStore();
  const [searchInput, setSearchInput] = useState("");

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchInput.trim()) {
      const ticker = searchInput.trim().toUpperCase();
      setActiveTicker(ticker);
      router.push(`/stock/${ticker}`);
    }
  };

  return (
    <header className="sticky top-0 z-50 w-full bg-[#0F172A]/90 backdrop-blur-md border-b border-slate-800 px-6 py-3">
      <div className="max-w-7xl mx-auto flex items-center justify-between gap-4">
        {/* Brand & Logo */}
        <Link href="/" className="flex items-center gap-3">
          <div className="bg-gradient-to-br from-indigo-500 to-blue-600 text-white font-black px-3 py-1.5 rounded-xl text-lg shadow-lg shadow-indigo-500/20">
            MM
          </div>
          <div>
            <div className="font-extrabold text-white text-lg leading-none tracking-tight">
              MarketMind AI
            </div>
            <div className="text-xs text-slate-400 font-medium">
              Autonomous Multi-Agent Copilot
            </div>
          </div>
        </Link>

        {/* Global Instant Ticker Search Bar */}
        <form onSubmit={handleSearch} className="flex-1 max-w-md">
          <div className="relative flex items-center">
            <Search className="absolute left-3.5 w-4 h-4 text-slate-400" />
            <input
              type="text"
              placeholder="Search ticker (e.g. AAPL, NVDA, TSLA, RELIANCE)..."
              value={searchInput}
              onChange={(e) => setSearchInput(e.target.value)}
              className="w-full bg-slate-900/80 text-white placeholder-slate-400 text-sm font-semibold pl-10 pr-24 py-2 rounded-xl border border-slate-800 focus:outline-none focus:border-indigo-500 transition"
            />
            <button
              type="submit"
              className="absolute right-1.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold px-3 py-1.5 rounded-lg flex items-center gap-1 transition shadow-md shadow-indigo-500/20"
            >
              <Sparkles className="w-3 h-3" />
              Analyze
            </button>
          </div>
        </form>

        {/* System Badges & User Profile */}
        <div className="flex items-center gap-3">
          <div className="hidden md:flex items-center gap-2 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold px-3 py-1.5 rounded-full">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            Multi-Agent Engine Active
          </div>
          {user ? (
            <Link
              href="/dashboard"
              className="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-white text-xs font-bold px-3 py-1.5 rounded-xl transition"
            >
              <User className="w-4 h-4 text-indigo-400" />
              {user.name}
            </Link>
          ) : (
            <Link
              href="/login"
              className="bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold px-4 py-2 rounded-xl transition shadow-md shadow-indigo-500/20"
            >
              Sign In
            </Link>
          )}
        </div>
      </div>
    </header>
  );
};
