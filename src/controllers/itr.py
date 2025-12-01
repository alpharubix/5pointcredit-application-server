from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from ..models.itr import ITR
from ..schemas.itr import ITRCreate

def create_itr(db: Session, data: ITRCreate):
    try:
        record = ITR(**data.model_dump())
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

def get_all_itr(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(ITR).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def get_by_customer(db: Session, customer_id: int):
    try:
        records = db.query(ITR).filter(ITR.customer_id == customer_id).all()
        if not records:
            raise HTTPException(status_code=404, detail="No records found")
        return records
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")