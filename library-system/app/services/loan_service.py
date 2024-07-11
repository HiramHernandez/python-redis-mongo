from app.models import Loan
from app.config import loan_collection
from bson import ObjectId

__all__ = ('loan_service',)


class LoanService:
    async def create_loan(self, loan_data: dict) -> dict:
        loan = Loan(**loan_data)
        result = await loan_collection.insert_one(loan.dict(by_alias=True))
        return await loan_collection.find_one({"_id": result.inserted_id})

    async def get_all_loans(self) -> list:
        loans = await loan_collection.find().to_list(1000)
        return loans

    async def get_loan_by_id(self, loan_id: str) -> dict:
        return await loan_collection.find_one({"_id": ObjectId(loan_id)})

    async def update_loan(self, loan_id: str, loan_data: dict) -> dict:
        await loan_collection.update_one({"_id": ObjectId(loan_id)}, {"$set": loan_data})
        return await loan_collection.find_one({"_id": ObjectId(loan_id)})

    async def delete_loan(self, loan_id: str) -> dict:
        delete_result = await loan_collection.delete_one({"_id": ObjectId(loan_id)})
        if delete_result.deleted_count == 1:
            return {"message": "Loan deleted successfully"}
        return None

loan_service = LoanService()