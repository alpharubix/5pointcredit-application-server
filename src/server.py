from typing import List, Annotated
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}