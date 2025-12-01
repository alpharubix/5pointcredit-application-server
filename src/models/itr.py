from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime, timezone
from ..database import Base

class ITR(Base):
    __tablename__ = "itr_records"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False, index=True)
    
    # ITR specific fields
    acknowledgement_number = Column(String, nullable=False)
    date_of_filing = Column(String)
    assessment_year = Column(String, nullable=False)
    pan = Column(String, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String)
    filed_under_section = Column(String)
    report_title = Column(String)
    section = Column(String)
    description = Column(String)
    gross_turnover = Column(Numeric(15, 2))
    taxable_total_income = Column(Numeric(15, 2))
    total_taxes_paid = Column(Numeric(15, 2))
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)