import { create } from "zustand";

interface User {
  user_id: string;
  name: string;
  email: string;
}

interface AppState {
  user: User | null;
  activeTicker: string;
  watchlist: string[];
  setUser: (user: User | null) => void;
  setActiveTicker: (ticker: string) => void;
  toggleWatchlist: (ticker: string) => void;
}

export const useAppStore = create<AppState>((set) => ({
  user: { user_id: "usr_001", name: "MarketMind Investor", email: "investor@marketmind.ai" },
  activeTicker: "AAPL",
  watchlist: ["AAPL", "NVDA", "TSLA", "RELIANCE.NS", "MSFT"],
  setUser: (user) => set({ user }),
  setActiveTicker: (activeTicker) => set({ activeTicker: activeTicker.toUpperCase() }),
  toggleWatchlist: (ticker) => set((state) => {
    const exists = state.watchlist.includes(ticker);
    return {
      watchlist: exists ? state.watchlist.filter(t => t !== ticker) : [...state.watchlist, ticker]
    };
  }),
}));
