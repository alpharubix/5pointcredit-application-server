from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.customer import CustomerCreate, CustomerResponse
from ..controllers import customer as repo

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/", response_model=CustomerResponse)
def create(data: CustomerCreate, db: Session = Depends(get_db)):
    return repo.create_customer(db, data)


@router.get("/", response_model=list[CustomerResponse])
def list_all(db: Session = Depends(get_db)):
    return repo.get_all_customers(db)