from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from app.api.auth import router as auth_router
from app.database.dbconnection import session,engine
from app.database import dbmodels
from pydantic import BaseModel
from datetime import date



app = FastAPI(title="Personal-Expense-Tracker")

# Creating DB connection
dbmodels.Base.metadata.create_all(bind=engine)
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
# create a model to add new expense
class ExpenseCreate(BaseModel):
    id:int
    title:str
    amount:int
    category:str
    expense_date:date
    
    
class Users(BaseModel):
    id:int
    age:int
    
#Creating a End point
@app.post("/expense")
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



    return {
        "message": "Expense inserted successfully",
        "id": new_expense.id,
        "title": new_expense.title,
        "amount": new_expense.amount,
        "category": new_expense.category,
        "expense_date" :new_expense.expense_date
    }

#Adding another row into expense table
@app.post("/expense1")
def expense1():
    result=create_expense()
    return result


#users table
@app.post("/users")
def User_Data(user=Users,
              db:Session=Depends(get_db)
):
    new_user=dbmodels.users(
        id=user.id,
        age=user.age
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": "user data updated successfully",
        "id":user.id,
        "age":user.age
    }
    
    

# authentication router method
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)
# Expenses rourter method
app.include_router(
    auth_router,
    prefix="/api/expenses",
    tags=["Authentication"]
)

@app.get("/")
def home():
    return {"Status": "OK"}
