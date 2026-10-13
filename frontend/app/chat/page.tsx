"use client";

import React, { useState } from "react";
import { Sidebar } from "@/components/sidebar";
import { postChatQuery } from "@/lib/api";
import { Bot, Send, User, Sparkles, Mic } from "lucide-react";

interface Message {
  sender: "user" | "bot";
  text: string;
}

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([
    {
      sender: "bot",
      text: "Hello! I am your MarketMind Investment Copilot. Ask me any question (e.g., 'Should I buy Tesla?', 'Analyze Apple vs Microsoft') to trigger our multi-agent AI pipeline."
    }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userText = input.trim();
    setInput("");
    setMessages((prev) => [...prev, { sender: "user", text: userText }]);
    setLoading(true);

    try {
      const res = await postChatQuery(userText);
      setMessages((prev) => [...prev, { sender: "bot", text: res.response }]);
    } catch (err) {
      setMessages((prev) => [...prev, { sender: "bot", text: "Error executing agent pipeline. Please try again." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex bg-[#0F172A] min-h-[calc(100vh-65px)]">
      <Sidebar />
      <div className="flex-1 p-8 space-y-6 max-w-5xl flex flex-col justify-between">
        <div>
          <h1 className="text-3xl font-black text-white flex items-center gap-3">
            <Bot className="w-7 h-7 text-indigo-400" /> AI Chat Copilot
          </h1>
          <p className="text-xs text-slate-400 mt-1">Conversational research assistant connected to multi-agent pipeline.</p>
        </div>

        {/* Chat History Container */}
        <div className="glass-card p-6 min-h-[450px] max-h-[500px] overflow-y-auto space-y-4 flex flex-col">
          {messages.map((m, i) => (
            <div
              key={i}
              className={`flex items-start gap-3 ${m.sender === "user" ? "flex-row-reverse" : "flex-row"}`}
            >
              <div className={`p-2 rounded-xl border ${m.sender === "user" ? "bg-indigo-600/20 border-indigo-500/30 text-indigo-400" : "bg-slate-800 border-slate-700 text-slate-300"}`}>
                {m.sender === "user" ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4 text-indigo-400" />}
              </div>
              <div className={`p-4 rounded-2xl max-w-xl text-sm leading-relaxed ${m.sender === "user" ? "bg-indigo-600/20 border border-indigo-500/30 text-white" : "bg-slate-900/80 border border-slate-800 text-slate-200"}`}>
                <p className="whitespace-pre-line">{m.text}</p>
              </div>
            </div>
          ))}
          {loading && (
            <div className="flex items-center gap-2 text-xs font-bold text-indigo-400 animate-pulse">
              <Sparkles className="w-4 h-4" /> Dispatching multi-agent pipeline...
            </div>
          )}
        </div>

        {/* Input Form */}
        <form onSubmit={handleSend} className="glass-card p-2 flex items-center gap-3">
          <input
            type="text"
            placeholder="Ask a question (e.g. Should I buy Reliance or Apple right now?)..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="flex-1 bg-transparent text-white placeholder-slate-400 text-sm font-semibold px-4 py-2 focus:outline-none"
          />
          <button type="button" className="text-slate-400 hover:text-white p-2">
            <Mic className="w-4 h-4" />
          </button>
          <button
            type="submit"
            disabled={loading}
            className="bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-xs px-5 py-2.5 rounded-xl flex items-center gap-1.5 transition shadow-lg shadow-indigo-500/20"
          >
            Send
            <Send className="w-3.5 h-3.5" />
          </button>
        </form>
      </div>
    </div>
  );
}
