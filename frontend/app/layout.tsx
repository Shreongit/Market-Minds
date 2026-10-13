import type { Metadata } from "next";
import "./globals.css";
import { Navbar } from "@/components/navbar";

export const metadata: Metadata = {
  title: "MarketMind AI — Your Autonomous Multi-Agent Investment Copilot",
  description: "Production-grade AI investment intelligence platform synthesizing multi-agent market research into transparent BUY/SELL/HOLD calls.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className="bg-[#0F172A] text-slate-100 min-h-screen antialiased flex flex-col">
        <Navbar />
        <main className="flex-1">{children}</main>
      </body>
    </html>
  );
}
