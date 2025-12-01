from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime
from typing import Optional
from decimal import Decimal

class ITRCreate(BaseModel):
    customer_id: int
    acknowledgement_number: str
    date_of_filing: Optional[str] = None
    assessment_year: str
    pan: str
    name: str
    address: Optional[str] = None
    filed_under_section: Optional[str] = None
    report_title: Optional[str] = None
    section: Optional[str] = None
    description: Optional[str] = None
    gross_turnover: Optional[Decimal] = None
    taxable_total_income: Optional[Decimal] = None
    total_taxes_paid: Optional[Decimal] = None

    @field_validator('acknowledgement_number', 'assessment_year', 'pan', 'name')
    @classmethod
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Required field cannot be empty')
        return v.strip()

    @field_validator('pan')
    @classmethod
    def validate_pan(cls, v):
        v = v.strip().upper()
        if len(v) != 10:
            raise ValueError('PAN must be 10 characters')
        return v

class ITRResponse(BaseModel):
    id: int
    customer_id: int
    acknowledgement_number: str
    assessment_year: str
    pan: str
    name: str
    taxable_total_income: Optional[Decimal]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)