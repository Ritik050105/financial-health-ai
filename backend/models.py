from sqlalchemy import Column, Integer, Float, String
from backend.database import Base

class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id = Column(Integer, primary_key=True, index=True)
    assets = Column(Float)
    liabilities = Column(Float)
    revenue = Column(Float)
    expenses = Column(Float)
    cash_flow = Column(Float)
    credit_rating = Column(String)
