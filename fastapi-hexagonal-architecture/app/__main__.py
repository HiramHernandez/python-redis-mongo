import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import uvicorn
from fastapi import FastAPI
from app.adapters.api.endpoints import users, auth

app = FastAPI()

app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])

@app.get("/")
def index():
    return "Hello Worl!!!"

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)