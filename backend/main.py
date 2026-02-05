from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pandas as pd
import os

from backend.financial_engine import financial_health_score
from backend.risk_engine import detect_risks
from backend.credit_engine import credit_rating
from backend.ai_insights import generate_insights
from backend.forecast_engine import forecast_cash_flow
from backend.report_engine import generate_pdf

app = FastAPI(title="Financial Health AI")

# ✅ CORS — allow ALL during hackathon
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LATEST_RESULT = {}

@app.post("/analyze")
async def analyze_financials(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file, encoding="latin1")

        if df.empty:
            raise HTTPException(status_code=400, detail="Empty CSV")

        df.columns = [c.strip().lower() for c in df.columns]

        required = {"assets", "liabilities", "revenue", "expenses", "cash_flow"}
        if not required.issubset(df.columns):
            raise HTTPException(
                status_code=400,
                detail=f"Missing columns: {required - set(df.columns)}"
            )

        data = df.iloc[0].to_dict()

        score = financial_health_score(data)
        avg_score = df.apply(
            lambda r: financial_health_score(r.to_dict()), axis=1
        ).mean()

        risks = detect_risks(data)
        insights = generate_insights(data, risks, score)
        rating, reason = credit_rating(score)
        forecast = forecast_cash_flow(data["cash_flow"])

        products = []
        if rating in ["A", "B"]:
            products = [
                "Working Capital Loan (NBFC)",
                "Invoice Discounting",
                "Short-Term Business Credit Line"
            ]

        result = {
            **data,
            "health_score": round(score, 2),
            "average_health_score": round(avg_score, 2),
            "credit_rating": rating,
            "rating_reason": reason,
            "risks": risks,
            "ai_insights": insights,
            "forecast": forecast,
            "recommended_products": products
        }

        global LATEST_RESULT
        LATEST_RESULT = result

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/report/pdf")
def download_report():
    if not LATEST_RESULT:
        raise HTTPException(status_code=400, detail="No report generated yet")

    file = generate_pdf(LATEST_RESULT)
    return FileResponse(file, media_type="application/pdf", filename=file)
