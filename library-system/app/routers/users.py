from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import UserSchema, UserResponse
from app.services.user_service import user_service

users_router = APIRouter(tags=["users"])

@users_router.post("/", response_description="Add new user", response_model=UserResponse)
async def create_user(user: UserSchema):
    created_user = await user_service.create_user(user.dict())
    return created_user

@users_router.get("/", response_description="List all users", response_model=List[UserResponse])
async def list_users():
    users = await user_service.get_all_users()
    return users

@users_router.get("/{id}", response_description="Get a single user", response_model=UserResponse)
async def show_user(id: str):
    user = await user_service.get_user_by_id(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail=f"User {id} not found")

@users_router.put("/{id}", response_description="Update a user", response_model=UserResponse)
async def update_user(id: str, user: UserSchema):
    updated_user = await user_service.update_user(id, user.dict())
    if updated_user:
        return updated_user
    raise HTTPException(status_code=404, detail=f"User {id} not found")

@users_router.delete("/{id}", response_description="Delete a user")
async def delete_user(id: str):
    result = await user_service.delete_user(id)
    if result:
        return result
    raise HTTPException(status_code=404, detail=f"User {id} not found")
