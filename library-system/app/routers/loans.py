from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import LoanSchema, LoanResponse
from app.services.loan_service import loan_service

loans_router = APIRouter(tags=["loans"])

@loans_router.post("/", response_description="Add new loan", response_model=LoanResponse)
async def create_loan(loan: LoanSchema):
    created_loan = await loan_service.create_loan(loan.dict())
    return created_loan

@loans_router.get("/", response_description="List all loans", response_model=List[LoanResponse])
async def list_loans():
    loans = await loan_service.get_all_loans()
    return loans

@loans_router.get("/{id}", response_description="Get a single loan", response_model=LoanResponse)
async def show_loan(id: str):
    loan = await loan_service.get_loan_by_id(id)
    if loan:
        return loan
    raise HTTPException(status_code=404, detail=f"Loan {id} not found")

@loans_router.put("/{id}", response_description="Update a loan", response_model=LoanResponse)
async def update_loan(id: str, loan: LoanSchema):
    updated_loan = await loan_service.update_loan(id, loan.dict())
    if updated_loan:
        return updated_loan
    raise HTTPException(status_code=404, detail=f"Loan {id} not found")

@loans_router.delete("/{id}", response_description="Delete a loan")
async def delete_loan(id: str):
    result = await loan_service.delete_loan(id)
    if result:
        return result
    raise HTTPException(status_code=404, detail=f"Loan {id} not found")
