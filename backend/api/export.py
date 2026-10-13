from fastapi import APIRouter
from fastapi.responses import Response, PlainTextResponse
from market_mind_ai.agents.decision_agent import DecisionAgent
from market_mind_ai.services.exporter import ReportExporterService

router = APIRouter(prefix="/export", tags=["Report Exporter"])

decision_agent = DecisionAgent()

@router.get("/pdf/{ticker}")
def download_pdf_report(ticker: str):
    dec = decision_agent.analyze(ticker)
    pdf_bytes = ReportExporterService.export_decision_to_pdf(dec)
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename=MarketMind_{ticker.upper()}_Report.pdf"}
    )

@router.get("/csv/{ticker}")
def download_csv_report(ticker: str):
    dec = decision_agent.analyze(ticker)
    csv_str = ReportExporterService.export_decision_to_csv(dec)
    return PlainTextResponse(
        content=csv_str,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=MarketMind_{ticker.upper()}_Report.csv"}
    )
