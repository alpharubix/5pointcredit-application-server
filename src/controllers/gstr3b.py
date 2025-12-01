from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException
from ..models.gstr3b import GSTR3B
from ..schemas.gstr3b import GSTR3BCreate

def create_gstr3b(db: Session, data: GSTR3BCreate):
    try:
        record = GSTR3B(**data.model_dump())
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


def get_by_customer(db: Session, customer_id: int):
    try:
        records = db.query(GSTR3B).filter(GSTR3B.customer_id == customer_id).all()
        if not records:
            raise HTTPException(status_code=404, detail="No records found")
        return records
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


def get_all_gstr3b(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GSTR3B).offset(skip).limit(limit).all()

