import uvicorn
from fastapi import FastAPI
from src.routers import customer, gstr3b, itr, bank_statement
from src.database import engine
from src.models.customer import Base as CustomerBase
from src.models.gstr3b import Base as GSTR3BBase
from src.models.itr import Base as ITRBase
from src.models.bank_statement import Base as BankStatementBase

CustomerBase.metadata.create_all(bind=engine)
GSTR3BBase.metadata.create_all(bind=engine)
ITRBase.metadata.create_all(bind=engine)
BankStatementBase.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(customer.router)
app.include_router(gstr3b.router)
app.include_router(itr.router)
app.include_router(bank_statement.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
