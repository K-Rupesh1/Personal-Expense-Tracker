from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from app.api.expenses import create_expense
from app.api.auth import router as auth_router
from app.api.expenses import router as expense_router
#from app.database.dbconnection import session,engine
from app.database import dbmodels
from pydantic import BaseModel
from datetime import date



app = FastAPI(title="Personal-Expense-Tracker")

# Creating DB connection
#dbmodels.Base.metadata.create_all(bind=engine)
    
    
class Users(BaseModel):
    id:int
    age:int
    name:str
    task:str
    


#Adding another row into expense table
@app.post("/expense1")
def expense1():
    result=create_expense()
    return result


#users table
@app.post("/users")
def User_Data(user=Users,
              #db:Session=Depends(get_db)
):
    new_user=dbmodels.users(
        id=user.id,
        age=user.age,
        name=user.name,
        task=user.task
    )
    """db.add(new_user)
    db.commit()
    db.refresh(new_user)"""
    return {
        "message": "user data updated successfully",
        "id":user.id,
        "age":user.age,
        "name":user.name,
        "task":user.task
    }
    
    

# authentication router method
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)
# Expenses rourter method
app.include_router(
    expense_router,
    prefix="/api/expenses",
    tags=["Authentication"]
)

@app.get("/")
def home():
    return {"Status": "OK"}
