"use client";

import React, { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { LogIn, Sparkles, ArrowRight } from "lucide-react";
import { useAppStore } from "@/lib/store";

export default function LoginPage() {
  const router = useRouter();
  const { setUser } = useAppStore();
  const [email, setEmail] = useState("investor@marketmind.ai");
  const [password, setPassword] = useState("password123");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setUser({
      user_id: "usr_001",
      name: "MarketMind Investor",
      email: email
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
          <h1 className="text-2xl font-black text-white">Sign In to Command Center</h1>
          <p className="text-xs text-slate-400 mt-1">Access multi-agent investment research & portfolio doctor</p>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div>
            <label className="text-xs font-bold text-slate-400 mb-1 block">Email Address</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full bg-slate-900 text-white border border-slate-800 rounded-xl px-4 py-2.5 text-sm font-semibold focus:outline-none focus:border-indigo-500"
              required
            />
          </div>

          <div>
            <div className="flex justify-between items-center mb-1">
              <label className="text-xs font-bold text-slate-400">Password</label>
              <a href="#" className="text-[11px] font-bold text-indigo-400 hover:underline">Forgot password?</a>
            </div>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-slate-900 text-white border border-slate-800 rounded-xl px-4 py-2.5 text-sm font-semibold focus:outline-none focus:border-indigo-500"
              required
            />
          </div>

          <div className="flex items-center gap-2 text-xs text-slate-400">
            <input type="checkbox" id="remember" defaultChecked className="rounded border-slate-800" />
            <label htmlFor="remember">Remember this device</label>
          </div>

          <button
            type="submit"
            className="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-sm py-3 rounded-xl flex items-center justify-center gap-2 transition shadow-lg shadow-indigo-500/20"
          >
            Sign In
            <ArrowRight className="w-4 h-4" />
          </button>
        </form>

        <div className="relative flex py-2 items-center">
          <div className="flex-grow border-t border-slate-800" />
          <span className="flex-shrink mx-4 text-[10px] font-bold text-slate-500 uppercase">Or continue with</span>
          <div className="flex-grow border-t border-slate-800" />
        </div>

        <div className="grid grid-cols-2 gap-3">
          <button
            onClick={() => handleSubmit({ preventDefault: () => {} } as any)}
            className="bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs py-2.5 rounded-xl border border-slate-800 transition"
          >
            Google Login
          </button>
          <button
            onClick={() => handleSubmit({ preventDefault: () => {} } as any)}
            className="bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs py-2.5 rounded-xl border border-slate-800 transition"
          >
            GitHub Login
          </button>
        </div>

        <div className="text-center text-xs text-slate-400">
          Don&apos;t have an account?{" "}
          <Link href="/signup" className="text-indigo-400 font-bold hover:underline">
            Create Account
          </Link>
        </div>
      </div>
    </div>
  );
}
