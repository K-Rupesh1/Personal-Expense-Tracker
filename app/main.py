from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
#from app.database.dbconnection import session,engine
from app.database import dbmodels
from app.users.user_login import router as auth_router
from app.users.user_login import router as expense_router
from pydantic import BaseModel
from datetime import date



app = FastAPI(title="Personal-Expense-Tracker")

# Creating DB connection
#dbmodels.Base.metadata.create_all(bind=engine)
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
