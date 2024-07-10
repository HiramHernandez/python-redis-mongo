# app/schemas.py

from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field):
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid ObjectId: {v}")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema, model_field) -> dict:
        """
        Generates a custom json schema for ObjectId,
        telling Pydantic that the type is string with UUID format.
        """
        return {"type": "string", "format": "uuid"}

class BookSchema(BaseModel):
    title: str
    author: str
    total_copies: int
    available_copies: int

class BookResponse(BookSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserSchema(BaseModel):
    name: str
    email: str

class UserResponse(UserSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class LoanSchema(BaseModel):
    user_id: PyObjectId
    book_id: PyObjectId
    loan_date: str
    return_date: Optional[str]

class LoanResponse(LoanSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
