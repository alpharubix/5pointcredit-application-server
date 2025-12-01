from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime, timezone
from ..database import Base

class GSTR3B(Base):
    __tablename__ = "gstr3b_records"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False, index=True)
    
    # GSTR-3B specific fields
    year = Column(String, nullable=False)
    period = Column(String, nullable=False)
    gstin = Column(String, nullable=False)
    legal_name = Column(String, nullable=False)
    trade_name = Column(String)
    arn = Column(String)
    date_of_arn = Column(String)
    section = Column(String)
    headers = Column(String)
    details = Column(String)
    sub_details = Column(String)
    nature_of_supplies = Column(String)
    total_taxable_value = Column(Numeric(15, 2))
    integrated_tax = Column(Numeric(15, 2))
    central_tax = Column(Numeric(15, 2))
    state_ut_tax = Column(Numeric(15, 2))
    cess = Column(Numeric(15, 2))
    inter_state_supplies = Column(Numeric(15, 2))
    intra_state_supplies = Column(Numeric(15, 2))
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)