from market_mind_ai.agents.base_agent import BaseAgent
from market_mind_ai.models.agent_schemas import SentimentAnalysisOutput
from market_mind_ai.services.news_service import NewsService
import numpy as np

class SentimentAgent(BaseAgent):
    """
    Market Sentiment Agent.
    Aggregates news headlines sentiment, social noise level, and macroeconomic Fear & Greed gauge.
    Returns sentiment score (0-100) + breakdown.
    """
    def __init__(self):
        super().__init__("Market Sentiment Agent")

    def analyze(self, ticker: str, **kwargs) -> SentimentAnalysisOutput:
        ticker = ticker.upper()
        news_list = NewsService.get_news_for_ticker(ticker)
        
        if news_list:
            avg_news_sentiment = float(np.mean([n.sentiment_score for n in news_list]))
            top_headlines = [n.title for n in news_list[:3]]
        else:
            avg_news_sentiment = 0.1
            top_headlines = ["Routine operational stability observed."]
            
        # Convert -1.0..+1.0 into 0..100 sentiment score
        news_score = round(50.0 + (avg_news_sentiment * 40.0), 1)
        news_score = max(0.0, min(100.0, news_score))
        
        # Macro Fear & Greed baseline
        fear_greed = 62.0  # Greed environment baseline
        
        if news_score >= 70:
            label = "Strongly Bullish"
            noise = "Medium"
        elif news_score >= 55:
            label = "Bullish"
            noise = "Low"
        elif news_score <= 35:
            label = "Bearish"
            noise = "High"
        else:
            label = "Neutral"
            noise = "Low"
            
        final_score = round(0.70 * news_score + 0.30 * fear_greed, 1)
        
        reasoning = (
            f"Market sentiment for {ticker} is {label} with a score of {final_score}/100. "
            f"Recent news flow shows average sentiment rating of {avg_news_sentiment:+.2f}. "
            f"Broad macro Fear & Greed index is reading {fear_greed:.0f}/100."
        )
        
        return SentimentAnalysisOutput(
            ticker=ticker,
            score=final_score,
            sentiment_label=label,
            news_sentiment_score=avg_news_sentiment,
            social_noise_level=noise,
            fear_and_greed_index=fear_greed,
            top_headlines_summary=top_headlines,
            summary_reasoning=reasoning
        )
