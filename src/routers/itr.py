from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.itr import ITRCreate, ITRResponse
from ..controllers import itr as controller

router = APIRouter(prefix="/itr", tags=["itr"])

@router.post("/", response_model=ITRResponse, status_code=201)
def create(data: ITRCreate, db: Session = Depends(get_db)):
    return controller.create_itr(db, data)

@router.get("/", response_model=list[ITRResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return controller.get_all_itr(db, skip, limit)

# @router.get("/customer/{customer_id}", response_model=list[ITRResponse])
# def get_by_customer(customer_id: int, db: Session = Depends(get_db)):
#     return controller.get_by_customer(db, customer_id)