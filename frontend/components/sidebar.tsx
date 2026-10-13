"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  TrendingUp,
  Stethoscope,
  FlaskConical,
  Cpu,
  Bell,
  Globe,
  Bot,
  Download,
  BookOpen
} from "lucide-react";

const navItems = [
  { label: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
  { label: "Stock Intelligence", href: "/stock/AAPL", icon: TrendingUp },
  { label: "Global Markets", href: "/markets", icon: Globe },
  { label: "AI Portfolio Doctor", href: "/portfolio", icon: Stethoscope },
  { label: "Strategy Lab", href: "/strategy", icon: FlaskConical },
  { label: "What-If Simulator", href: "/what-if", icon: Cpu },
  { label: "News & Smart Alerts", href: "/news", icon: Bell },
  { label: "AI Chat Copilot", href: "/chat", icon: Bot },
  { label: "Export Reports", href: "/exports", icon: Download },
];

export const Sidebar = () => {
  const pathname = usePathname();

  return (
    <aside className="w-64 bg-[#0F172A]/95 border-r border-slate-800 min-h-[calc(100vh-65px)] p-4 flex flex-col gap-1">
      <div className="text-[10px] font-extrabold text-slate-500 tracking-wider px-3 py-2 uppercase">
        Navigation Menu
      </div>
      {navItems.map((item) => {
        const Icon = item.icon;
        const isActive = pathname === item.href || (item.href !== "/" && pathname.startsWith(item.href.split("/")[1]));
        return (
          <Link
            key={item.href}
            href={item.href}
            className={`flex items-center gap-3 px-3 py-2.5 rounded-xl font-medium text-sm transition-all ${
              isActive
                ? "bg-indigo-600/20 text-white border-l-4 border-indigo-500 font-bold"
                : "text-slate-400 hover:bg-slate-800/50 hover:text-white"
            }`}
          >
            <Icon className={`w-4 h-4 ${isActive ? "text-indigo-400" : "text-slate-400"}`} />
            {item.label}
          </Link>
        );
      })}
    </aside>
  );
};
