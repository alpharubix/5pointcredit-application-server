from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.customer import Customer
from ..schemas.customer import CustomerCreate

def create_customer(db: Session, data: CustomerCreate) -> Customer:
    # 1. Check Logic
    if db.query(Customer).filter(Customer.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email exists")

    # 2. DB Operation
    new_customer = Customer(**data.model_dump())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    
    # 3. Return RAW SQLALCHEMY OBJECT
    return new_customer


def get_all_customers(db: Session):
    return db.query(Customer).all()