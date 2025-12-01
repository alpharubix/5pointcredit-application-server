from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime
from typing import Optional
from decimal import Decimal

class BankStatementCreate(BaseModel):
    customer_id: int
    company_name: Optional[str] = None
    account_type: Optional[str] = None
    scheme: Optional[str] = None
    account_no: str
    customer_bank_id: Optional[str] = None
    ifsc_code: Optional[str] = None
    micr_code: Optional[str] = None
    nominee_registered: Optional[str] = None
    ckyc_number: Optional[str] = None
    tran_date: Optional[str] = None
    value_date: Optional[str] = None
    transaction_particulars: Optional[str] = None
    chq_no: Optional[str] = None
    amount: Optional[Decimal] = None
    dr_cr: Optional[str] = None
    balance: Optional[Decimal] = None
    branch_name: Optional[str] = None

    @field_validator('account_no')
    @classmethod
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Account number is required')
        return v.strip()

    @field_validator('dr_cr')
    @classmethod
    def validate_dr_cr(cls, v):
        if v and v.strip().upper() not in ['DR', 'CR', 'DEBIT', 'CREDIT']:
            raise ValueError('DR/CR must be DR, CR, DEBIT, or CREDIT')
        return v.strip().upper() if v else None

class BankStatementResponse(BaseModel):
    id: int
    customer_id: int
    account_no: str
    tran_date: Optional[str]
    transaction_particulars: Optional[str]
    amount: Optional[Decimal]
    dr_cr: Optional[str]
    balance: Optional[Decimal]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)