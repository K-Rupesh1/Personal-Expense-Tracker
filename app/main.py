from fastapi import FastAPI
from api.auth import router as auth_router

app = FastAPI(title="Personal-Expense-Tracker")

# authentication router method
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)


@app.get("/")
def home():
    return {"Status": "OK"}
