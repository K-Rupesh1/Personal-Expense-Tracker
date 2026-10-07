from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# User  Registration
class UserRegistration(BaseModel):
    userid: str
    Email: str
    Password: str
# User Login
class UserLogin(BaseModel):
    Email: str
    Password:str

# User Logout
class UserLogout(BaseModel):
    Email: str
    Password:str
#current User
class CurrentUser(BaseModel):
    Name:str
    Email:str
    
# Changed Password
class ChangePassword(BaseModel):
    Email: str
    OldPassword: str
    NewPassword: str
    
    
#Register
@router.post("/register")
def user_registration(user: UserRegistration):
    return {
        "Status": "Ok",
        "Message": "User Registration Successful",
        "UserName": user.userid,
        "Email": user.Email
    }

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
@router.post("/logout")
def User_Logout(user:UserLogout):
    return{
        "Email":user.Email,
        "Password":user.Password,
        "Status":"OK",
        "Message":"Logout Successfull"
    }
    

# Current User
@router.get("/user")
def get_current_user(user:CurrentUser):
    return {
        "UserName": user.Name,
        "Email": user.Email,
        "Status": "Active"
    }
    
# Change Password
@router.put("/changepassword")
def change_password(data: ChangePassword):
    return {
        "Status": "OK",
        "Message": "Password changed successfully",
        "Email": data.Email
    }