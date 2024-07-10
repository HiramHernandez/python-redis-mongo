import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from fastapi import FastAPI
import uvicorn
from app.routers import books, users, loans

app = FastAPI()

app.include_router(users.users_router)
app.include_router(books.books_router)
app.include_router(loans.loans_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
