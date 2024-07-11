from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import BookSchema, BookResponse
from app.services.book_service import book_service

__all__ = ('books_router',)

books_router = APIRouter(
    prefix="/api/books",
    tags=["books"]
)

@books_router.post("", response_description="Add new book", response_model=BookResponse)
async def create_book(book: BookSchema):
    created_book = await book_service.create_book(book.dict())
    return created_book

@books_router.get("", response_description="List all books", response_model=List[BookResponse])
async def list_books():
    books = await book_service.get_all_books()
    return books

@books_router.get("/{id}", response_description="Get a single book", response_model=BookResponse)
async def show_book(id: str):
    book = await book_service.get_book_by_id(id)
    if book:
        return book
    raise HTTPException(status_code=404, detail=f"Book {id} not found")

@books_router.put("/{id}", response_description="Update a book", response_model=BookResponse)
async def update_book(id: str, book: BookSchema):
    updated_book = await book_service.update_book(id, book.dict())
    if updated_book:
        return updated_book
    raise HTTPException(status_code=404, detail=f"Book {id} not found")

@books_router.delete("/{id}", response_description="Delete a book")
async def delete_book(id: str):
    result = await book_service.delete_book(id)
    if result:
        return result
    raise HTTPException(status_code=404, detail=f"Book {id} not found")
