from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime, timezone
from ..database import Base

class BankStatement(Base):
    __tablename__ = "bank_statements"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False, index=True)
    
    # Bank statement specific fields
    company_name = Column(String, nullable=False)
    account_type = Column(String, nullable=False)
    scheme = Column(String)
    account_no = Column(String, nullable=False)
    customer_bank_id = Column(String)
    ifsc_code = Column(String, nullable=False)
    micr_code = Column(String)
    nominee_registered = Column(String)
    ckyc_number = Column(String)
    tran_date = Column(String)
    value_date = Column(String)
    transaction_particulars = Column(String)
    chq_no = Column(String)
    amount = Column(Numeric(15, 2))
    dr_cr = Column(String)
    balance = Column(Numeric(15, 2))
    branch_name = Column(String)
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)