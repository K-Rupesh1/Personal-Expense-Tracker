from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# User  Registration
class UserRegistration(BaseModel):
    user_name:str
    email: str
    password: str
# User Login
class UserLogin(BaseModel):
    email: str
    password:str
class UserLoginResponse(BaseModel):
    token:str
    type:str

# User Logout
# class UserLogout(BaseModel):
#     email: str
#     password:str
#current User
# class CurrentUser(BaseModel):
#     name:str
#     email:str
    
# Changed Password
class ChangePassword(BaseModel):
    email: str
    old_password: str
    new_password: str