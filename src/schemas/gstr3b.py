from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime
from typing import Optional
from decimal import Decimal

class GSTR3BCreate(BaseModel):
    customer_id: int
    year: str
    period: str
    gstin: str
    legal_name: str
    trade_name: Optional[str] = None
    arn: Optional[str] = None
    date_of_arn: Optional[str] = None
    section: Optional[str] = None
    headers: Optional[str] = None
    details: Optional[str] = None
    sub_details: Optional[str] = None
    nature_of_supplies: Optional[str] = None
    total_taxable_value: Optional[Decimal] = None
    integrated_tax: Optional[Decimal] = None
    central_tax: Optional[Decimal] = None
    state_ut_tax: Optional[Decimal] = None
    cess: Optional[Decimal] = None
    inter_state_supplies: Optional[Decimal] = None
    intra_state_supplies: Optional[Decimal] = None

    @field_validator('year', 'period', 'gstin', 'legal_name')
    @classmethod
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Required field cannot be empty')
        return v.strip()

    @field_validator('gstin')
    @classmethod
    def validate_gstin(cls, v):
        v = v.strip()
        if len(v) != 15:
            raise ValueError('GSTIN must be 15 characters')
        return v.upper()

class GSTR3BResponse(BaseModel):
    # --- Custom Status Fields (Not in DB) ---
    status: str = "success"
    message: str = "GSTR-3B details saved successfully"


    # IDs
    id: int
    customer_id: int

    # Basic Info (Required)
    year: str
    period: str
    gstin: str
    legal_name: str

    # Details (Optional/Nullable in DB)
    trade_name: Optional[str] = None
    arn: Optional[str] = None
    date_of_arn: Optional[str] = None
    section: Optional[str] = None
    headers: Optional[str] = None
    details: Optional[str] = None
    sub_details: Optional[str] = None
    nature_of_supplies: Optional[str] = None

    # Financials (Decimal for currency precision)
    total_taxable_value: Optional[Decimal] = None
    integrated_tax: Optional[Decimal] = None
    central_tax: Optional[Decimal] = None
    state_ut_tax: Optional[Decimal] = None
    cess: Optional[Decimal] = None
    inter_state_supplies: Optional[Decimal] = None
    intra_state_supplies: Optional[Decimal] = None

    # Timestamps (Ensure these exist in your SQLAlchemy model too)
    created_at: datetime
    updated_at: datetime

    # Pydantic V2 Config
    model_config = ConfigDict(from_attributes=True)

