"use client";

import React, { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Sparkles, ArrowRight } from "lucide-react";
import { useAppStore } from "@/lib/store";

export default function SignupPage() {
  const router = useRouter();
  const { setUser } = useAppStore();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setUser({
      user_id: "usr_new",
      name: name || "New MarketMind User",
      email: email || "user@marketmind.ai"
    });
    router.push("/dashboard");
  };

  return (
    <div className="min-h-[calc(100vh-65px)] flex items-center justify-center p-6 bg-[#0F172A]">
      <div className="glass-card p-8 w-full max-w-md flex flex-col gap-6">
        <div className="text-center">
          <div className="inline-flex items-center gap-2 bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-bold px-3 py-1 rounded-full mb-3">
            <Sparkles className="w-3.5 h-3.5" />
            MarketMind AI Copilot
          </div>
          <h1 className="text-2xl font-black text-white">Create Pro Account</h1>
          <p className="text-xs text-slate-400 mt-1">Unlock autonomous multi-agent equity research</p>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div>
            <label className="text-xs font-bold text-slate-400 mb-1 block">Full Name</label>
            <input
              type="text"
              placeholder="Alex Morgan"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full bg-slate-900 text-white border border-slate-800 rounded-xl px-4 py-2.5 text-sm font-semibold focus:outline-none focus:border-indigo-500"
              required
            />
          </div>

          <div>
            <label className="text-xs font-bold text-slate-400 mb-1 block">Email Address</label>
            <input
              type="email"
              placeholder="alex@company.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full bg-slate-900 text-white border border-slate-800 rounded-xl px-4 py-2.5 text-sm font-semibold focus:outline-none focus:border-indigo-500"
              required
            />
          </div>

          <div>
            <label className="text-xs font-bold text-slate-400 mb-1 block">Password</label>
            <input
              type="password"
              placeholder="••••••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-slate-900 text-white border border-slate-800 rounded-xl px-4 py-2.5 text-sm font-semibold focus:outline-none focus:border-indigo-500"
              required
            />
          </div>

          <button
            type="submit"
            className="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-sm py-3 rounded-xl flex items-center justify-center gap-2 transition shadow-lg shadow-indigo-500/20"
          >
            Create Account
            <ArrowRight className="w-4 h-4" />
          </button>
        </form>

        <div className="text-center text-xs text-slate-400">
          Already have an account?{" "}
          <Link href="/login" className="text-indigo-400 font-bold hover:underline">
            Sign In
          </Link>
        </div>
      </div>
    </div>
  );
}
