from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

TRANSLATIONS = {
    "en": {
        "title": "SME Financial Health – Investor Report",
        "health_score": "Health Score",
        "credit_rating": "Credit Rating",
        "risks": "Financial Risks",
        "insights": "AI Recommendations",
    },
    "hi": {
        "title": "एसएमई वित्तीय स्वास्थ्य – निवेशक रिपोर्ट",
        "health_score": "स्वास्थ्य स्कोर",
        "credit_rating": "क्रेडिट रेटिंग",
        "risks": "वित्तीय जोखिम",
        "insights": "एआई सिफारिशें",
    },
    "ta": {
        "title": "எஸ்எம்இ நிதி ஆரோக்கியம் – முதலீட்டாளர் அறிக்கை",
        "health_score": "ஆரோக்கிய மதிப்பெண்",
        "credit_rating": "கடன் மதிப்பீடு",
        "risks": "நிதி ஆபத்துகள்",
        "insights": "ஏஐ பரிந்துரைகள்",
    }
}

def generate_pdf(result, lang="en", filename="investor_report.pdf"):
    t = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(t["title"], styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph(
        f"<b>{t['health_score']}:</b> {result['health_score']}", styles["Normal"]
    ))
    story.append(Paragraph(
        f"<b>{t['credit_rating']}:</b> {result['credit_rating']}", styles["Normal"]
    ))

    story.append(Spacer(1, 12))
    story.append(Paragraph(f"<b>{t['risks']}:</b>", styles["Heading2"]))
    for r in result["risks"]:
        story.append(Paragraph(f"- {r}", styles["Normal"]))

    story.append(Spacer(1, 12))
    story.append(Paragraph(f"<b>{t['insights']}:</b>", styles["Heading2"]))
    story.append(Paragraph(result["ai_insights"], styles["Normal"]))

    doc.build(story)
    return filename
