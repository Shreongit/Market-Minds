from fastapi import APIRouter
from pydantic import BaseModel
from market_mind_ai.services.llm_orchestrator import LLMOrchestrator
from market_mind_ai.agents.decision_agent import DecisionAgent

router = APIRouter(prefix="/chat", tags=["AI Copilot Chat"])

decision_agent = DecisionAgent()

class ChatQueryRequest(BaseModel):
    query: str

class ChatQueryResponse(BaseModel):
    response: str
    ticker_analyzed: str = ""

@router.post("/query", response_model=ChatQueryResponse)
def handle_copilot_chat(req: ChatQueryRequest):
    query = req.query.strip()
    words = query.upper().split()
    
    # Check if query targets a specific ticker
    known_tickers = ["AAPL", "NVDA", "TSLA", "MSFT", "GOOGL", "RELIANCE.NS", "TCS.NS", "INFY.NS"]
    target = ""
    for w in words:
        clean_w = w.strip("?,.!")
        if clean_w in known_tickers or (len(clean_w) <= 5 and clean_w.isalpha()):
            target = clean_w
            break

    if target:
        dec = decision_agent.analyze(target)
        ans = (
            f"**Multi-Agent Intelligence Analysis for {target}**:\n\n"
            f"• **Recommendation**: {dec.recommendation} (Confidence: {dec.confidence:.0f}%)\n"
            f"• **Target Price**: ${dec.target_price:.2f} | **Stop Loss**: ${dec.stop_loss:.2f}\n"
            f"• **Score Breakdown**: Technical ({dec.technical_score}/100), Fundamental ({dec.fundamental_score}/100), Sentiment ({dec.sentiment_score}/100), Risk ({dec.risk_score}/100).\n\n"
            f"**Rationale**: {dec.reasoning}"
        )
        return ChatQueryResponse(response=ans, ticker_analyzed=target)
        
    completion = LLMOrchestrator.generate_completion(query)
    return ChatQueryResponse(response=completion)
