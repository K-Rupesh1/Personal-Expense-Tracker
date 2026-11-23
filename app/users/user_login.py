from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database import dbmodels
from app.schemas import ChangePassword, UserLogin,UserRegistration
from app.database.dbconnection import session_start
from fastapi.params import Depends
from pwdlib import PasswordHash
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

router=APIRouter()

#Getting DB DATA
def get_db():
    db=session_start()
    try :
        yield db
    finally :
        db.close()
    




#REGISTER
@router.post("/register")
def user_register(user: UserRegistration,
                      db:Session=Depends(get_db)):
    try:
        password_hash=PasswordHash.recommended()
        hashed_password=password_hash.hash(user.password)
        print(hashed_password)
        registration=dbmodels.Users(
        user_name=user.user_name,
        email=user.email,
        password=hashed_password)
        print("object created")
        
        db.add(registration)
        print("registration added into db")
        db.commit()
        print("db committed")
        db.refresh(registration)
        
        return {
            "Status": "Ok",
            "Message": "User Registration Successful",
            "UserName": user.user_name,
            "Email": user.email,
            "Password":user.password
        }
    except SQLAlchemyError as e:
        db.rollback()
        print("Actual database error:", e)
        raise HTTPException(status_code=500,detail="Error at database connection")
        

#Login
@router.post("/login")
def user_login(user:UserLogin):
    return{
        "Email":user.Email,
        "Password":user.Password,
        "Status":"OK",
        "Message":"Login Successfull"
        
    }
    
#Login
# @router.post("/logout")
# def User_Logout(user:UserLogout):
#     return{
#         "Email":user.Email,
#         "Password":user.Password,
#         "Status":"OK",
#         "Message":"Logout Successfull"
#     }
    

# # Current User
# @router.get("/user")
# def get_current_user(user:CurrentUser):
#     return {
#         "UserName": user.Name,
#         "Email": user.Email,
#         "Status": "Active"
#     }
    
# Change Password
@router.put("/changepassword")
def change_password(data: ChangePassword):
    return {
        "Status": "OK",
        "Message": "Password changed successfully",
        "Email": data.Email
    }