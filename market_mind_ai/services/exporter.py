import csv
import io
import pandas as pd
from typing import Dict, Any, List
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from market_mind_ai.models.agent_schemas import DecisionOutput

class ReportExporterService:
    """
    Export Service generating PDF, Excel, and CSV research reports.
    """

    @classmethod
    def export_decision_to_pdf(cls, decision: DecisionOutput) -> bytes:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        styles = getSampleStyleSheet()
        story = []
        
        # Title & Header
        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=22, textColor=colors.HexColor('#0F172A'), spaceAfter=10)
        story.append(Paragraph(f"MarketMind AI — Investment Intelligence Report", title_style))
        story.append(Paragraph(f"<b>Ticker:</b> {decision.ticker} | <b>Recommendation:</b> {decision.recommendation} | <b>Confidence:</b> {decision.confidence}%", styles['Normal']))
        story.append(Spacer(1, 15))
        
        # Summary Table
        table_data = [
            ["Metric", "Value"],
            ["Recommendation", decision.recommendation],
            ["Overall AI Score", f"{decision.overall_ai_score} / 100"],
            ["Target Price", f"${decision.target_price:.2f}"],
            ["Stop Loss", f"${decision.stop_loss:.2f}"],
            ["Entry Range", decision.entry_range],
            ["Suggested Holding Period", decision.suggested_holding_period],
            ["Risk Level", decision.risk_level]
        ]
        
        t = Table(table_data, colWidths=[200, 300])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E293B')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8FAFC')),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0'))
        ]))
        story.append(t)
        story.append(Spacer(1, 15))
        
        # Scores Breakdown
        story.append(Paragraph("<b>Agent Scores Breakdown:</b>", styles['Heading2']))
        story.append(Paragraph(f"• Technical Analysis: {decision.technical_score}/100 — {decision.technical_why}", styles['Normal']))
        story.append(Paragraph(f"• Fundamental Analysis: {decision.fundamental_score}/100 — {decision.fundamental_why}", styles['Normal']))
        story.append(Paragraph(f"• Market Sentiment: {decision.sentiment_score}/100 — {decision.sentiment_why}", styles['Normal']))
        story.append(Paragraph(f"• Risk Volatility: {decision.risk_score}/100 — {decision.risk_why}", styles['Normal']))
        story.append(Spacer(1, 15))
        
        # Rationale Narrative
        story.append(Paragraph("<b>Investment Rationale:</b>", styles['Heading2']))
        story.append(Paragraph(decision.reasoning, styles['Normal']))
        story.append(Spacer(1, 10))
        
        story.append(Paragraph("<b>Thesis Invalidation Triggers:</b>", styles['Heading2']))
        story.append(Paragraph(decision.what_could_invalidate, styles['Normal']))
        story.append(Spacer(1, 10))
        
        story.append(Paragraph("<b>Known Analysis Limitations:</b>", styles['Heading2']))
        story.append(Paragraph(decision.known_limitations, styles['Normal']))
        
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()

    @classmethod
    def export_decision_to_csv(cls, decision: DecisionOutput) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Metric", "Value"])
        writer.writerow(["Ticker", decision.ticker])
        writer.writerow(["Recommendation", decision.recommendation])
        writer.writerow(["Confidence (%)", decision.confidence])
        writer.writerow(["Overall AI Score", decision.overall_ai_score])
        writer.writerow(["Target Price ($)", decision.target_price])
        writer.writerow(["Stop Loss ($)", decision.stop_loss])
        writer.writerow(["Entry Range", decision.entry_range])
        writer.writerow(["Holding Period", decision.suggested_holding_period])
        writer.writerow(["Technical Score", decision.technical_score])
        writer.writerow(["Fundamental Score", decision.fundamental_score])
        writer.writerow(["Sentiment Score", decision.sentiment_score])
        writer.writerow(["Risk Score", decision.risk_score])
        writer.writerow(["Reasoning", decision.reasoning])
        writer.writerow(["Invalidation Triggers", decision.what_could_invalidate])
        return output.getvalue()
