from pydantic import BaseModel

class FinancialInput(BaseModel):
    revenue: float
    expenses: float
    assets: float
    liabilities: float
    cash_flow: float
