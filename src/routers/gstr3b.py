from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.gstr3b import GSTR3BCreate, GSTR3BResponse
from ..controllers import gstr3b as repo

router = APIRouter(prefix="/gstr3b", tags=["gstr3b"])

@router.get("/", response_model=list[GSTR3BResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return repo.get_all_gstr3b(db, skip, limit)


@router.post("/", response_model=GSTR3BResponse, status_code=201)
def create(data: GSTR3BCreate, db: Session = Depends(get_db)):
    return repo.create_gstr3b(db, data)


@router.get("/customer/{customer_id}", response_model=list[GSTR3BResponse])
def get_by_customer(customer_id: int, db: Session = Depends(get_db)):
    return repo.get_by_customer(db, customer_id)