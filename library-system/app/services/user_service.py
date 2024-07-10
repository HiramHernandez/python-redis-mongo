from app.models import User
from app.config import user_collection
from bson import ObjectId

__all__ = ('user_service',)


class UserService:
    async def create_user(self, user_data: dict) -> dict:
        book = User(**user_data)
        result = await user_collection.insert_one(book.dict(by_alias=True))
        return await user_collection.find_one({"_id": result.inserted_id})

    async def get_all_users(self) -> list:
        books = await user_collection.find().to_list(1000)
        return books

    async def get_user_by_id(self, user_id: str) -> dict:
        return await user_collection.find_one({"_id": ObjectId(user_id)})

    async def update_user(self, book_id: str, user_data: dict) -> dict:
        await user_collection.update_one({"_id": ObjectId(book_id)}, {"$set": user_data})
        return await user_collection.find_one({"_id": ObjectId(book_id)})

    async def delete_user(self, user_id: str) -> dict:
        delete_result = await user_collection.delete_one({"_id": ObjectId(user_id)})
        if delete_result.deleted_count == 1:
            return {"message": "User deleted successfully"}
        return None

user_service = UserService()