from fastapi import APIRouter
# create a model to add new expense
from datetime import date


from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.dbconnection import session


from app.database import dbmodels

router=APIRouter()
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
class ExpenseCreate(BaseModel):
    id:int
    title:str
    amount:int
    category:str
    expense_date:date
    
@router.post("/expense")
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db)
):
    new_expense = dbmodels.Expense(
        id=expense.id,
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        expense_date=expense.expense_date
    )
    db.add(new_expense)       # Add record to session
    db.commit()               # Save changes to database
    db.refresh(new_expense)


    return {
        "message": "Expense inserted successfully",
        "id": new_expense.id,
        "title": new_expense.title,
        "amount": new_expense.amount,
        "category": new_expense.category,
        "expense_date" :new_expense.expense_date
    }

'''POST	/api/expenses	Add a new expense
GET	/api/expenses	Get all expenses
GET	/api/expenses/{expense_id}	Get one expense
PUT	/api/expenses/{expense_id}	Update expense
DELETE	/api/expenses/{expense_id}	Delete expense
'''
