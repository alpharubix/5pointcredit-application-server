from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.bank_statement import BankStatementCreate, BankStatementResponse
from ..controllers import bank_statement as controller

router = APIRouter(prefix="/bank-statements", tags=["bank-statements"])

@router.post("/", response_model=BankStatementResponse, status_code=201)
def create(data: BankStatementCreate, db: Session = Depends(get_db)):
    return controller.create_bank_statement(db, data)

@router.get("/", response_model=list[BankStatementResponse])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return controller.get_all_bank_statements(db, skip, limit)

@router.get("/customer/{customer_id}", response_model=list[BankStatementResponse])
def get_by_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.get_by_customer(db, customer_id)