from sqlalchemy import Column, Integer, String, DateTime
from ..database import Base
from datetime import datetime, timezone


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String,unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    pan = Column(String, unique=True, index=True, nullable=False)
    gstin = Column(String, unique=True, index=True, nullable=False)
    

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

