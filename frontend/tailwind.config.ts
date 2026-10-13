import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#0F172A",
        card: "rgba(30, 41, 59, 0.75)",
        primary: {
          DEFAULT: "#6366F1",
          hover: "#4F46E5",
        },
        accent: {
          emerald: "#10B981",
          rose: "#EF4444",
          amber: "#F59E0B",
        }
      },
      backdropBlur: {
        glass: "16px",
      }
    },
  },
  plugins: [],
};

export default config;
