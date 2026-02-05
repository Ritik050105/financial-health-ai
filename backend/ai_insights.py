import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "tinyllama"


def _ollama_available():
    try:
        r = requests.get("http://localhost:11434", timeout=2)
        return r.status_code == 200
    except Exception:
        return False


def generate_insights(data, risks, score):
    """
    Generates SME-friendly financial recommendations.
    Uses Ollama if available, otherwise falls back to rules.
    """

    # ---------- TRY OLLAMA ----------
    if _ollama_available():
        prompt = f"""
You are a financial advisor for SMEs.

Assets: {data.get("assets")}
Liabilities: {data.get("liabilities")}
Revenue: {data.get("revenue")}
Expenses: {data.get("expenses")}
Cash Flow: {data.get("cash_flow")}

Health Score: {score}
Risks: {risks}

Give 2–3 short, practical recommendations.
"""

        payload = {
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(OLLAMA_URL, json=payload, timeout=20)
            response.raise_for_status()
            return response.json().get("response", "").strip()
        except Exception:
            pass  # fall back safely

    # ---------- FALLBACK (RULE-BASED) ----------
    insights = []

    if score < 60:
        insights.append(
            "Reduce operating expenses and closely monitor cash flow."
        )

    if data.get("liabilities", 0) > data.get("assets", 0):
        insights.append(
            "Consider restructuring debt or improving capital reserves."
        )

    if not risks:
        insights.append(
            "No critical financial risks detected. Maintain current discipline."
        )

    if not insights:
        insights.append(
            "Focus on improving profitability and maintaining liquidity buffers."
        )

    return " ".join(insights)
