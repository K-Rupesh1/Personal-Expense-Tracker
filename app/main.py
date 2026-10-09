from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.database.dbconnection import session,engine
from app.database import dbmodels


dbmodels.Base.metadata.create_all(bind=engine)
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


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
