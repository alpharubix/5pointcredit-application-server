from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from ..models.bank_statement import BankStatement
from ..schemas.bank_statement import BankStatementCreate

def create_bank_statement(db: Session, data: BankStatementCreate):
    try:
        record = BankStatement(**data.model_dump())
        db.add(record)
        db.commit()
        db.refresh(record)
        return record
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Duplicate record")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def get_all_bank_statements(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(BankStatement).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def get_by_customer(db: Session, customer_id: int):
    try:
        records = db.query(BankStatement).filter(BankStatement.customer_id == customer_id).all()
        if not records:
            raise HTTPException(status_code=404, detail="No records found")
        return records
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")