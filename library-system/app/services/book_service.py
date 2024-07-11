from app.models import Book
from app.config import book_collection
from bson import ObjectId

__all__ = ('book_service',)


class BookService:
    async def create_book(self, book_data: dict) -> dict:
        book = Book(**book_data)
        book.available_copies = book.total_copies
        result = await book_collection.insert_one(book.dict(by_alias=True))
        return await book_collection.find_one({"_id": result.inserted_id})

    async def get_all_books(self) -> list:
        books = await book_collection.find().to_list(1000)
        return books

    async def get_book_by_id(self, book_id: str) -> dict:
        return await book_collection.find_one({"_id": ObjectId(book_id)})

    async def update_book(self, book_id: str, book_data: dict) -> dict:
        await book_collection.update_one({"_id": ObjectId(book_id)}, {"$set": book_data})
        return await book_collection.find_one({"_id": ObjectId(book_id)})

    async def update_available_copies(self, book_id: str) -> None:
        book = await self.get_book_by_id(book_id)
        copies =  book['available_copies'] - 1
        book['available_copies'] = copies
        await self.update_book(book_id, book)
    
    async  def is_available_to_load(self, book_id: str) -> bool:
        book = await book_collection.find_one( {"_id": ObjectId(book_id)}, {"available_copies": 1})
        return True if book and book.get("available_copies", 0) >= 1 else False

    async def delete_book(self, book_id: str) -> dict:
        delete_result = await book_collection.delete_one({"_id": ObjectId(book_id)})
        if delete_result.deleted_count == 1:
            return {"message": "Book deleted successfully"}
        return None

book_service = BookService()