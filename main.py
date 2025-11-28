from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/count")
async def count():
    return {"total_count": 0000000000}

@app.get("/user")
async def set_data():
    return {"username": "Suraj Gupta"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

