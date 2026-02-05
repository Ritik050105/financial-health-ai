from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def generate_pdf(result, filename="investor_report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(
        "<b>SME Financial Health Assessment – Investor Report</b>",
        styles["Title"]
    ))
    story.append(Spacer(1, 14))

    fields = [
        ("Health Score", result.get("health_score")),
        ("Credit Rating", result.get("credit_rating")),
        ("Rating Insight", result.get("rating_reason")),
        ("Revenue", result.get("revenue")),
        ("Expenses", result.get("expenses")),
        ("Cash Flow", result.get("cash_flow")),
    ]

    for label, value in fields:
        story.append(
            Paragraph(f"<b>{label}:</b> {value}", styles["Normal"])
        )
        story.append(Spacer(1, 8))

    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>AI Recommendations</b>", styles["Heading2"]))
    story.append(Spacer(1, 6))
    story.append(
        Paragraph(result.get("ai_insights", ""), styles["Normal"])
    )

    doc.build(story)
    return filename
