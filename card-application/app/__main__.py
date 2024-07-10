import sys
from pathlib import Path

# Agregar la raíz del proyecto al sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from fastapi import FastAPI
import uvicorn
from app.config import engine, settings
from app.routers import *
from app import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(card_router)
app.include_router(transaction_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
