from pydantic import BaseModel ,EmailStr, Field

class UserCreate(BaseModel) : 
    username : str =  Field(...,min_length=3,max_length = 50)
    email : EmailStr #IT ENSURES PROPER EMIAL FORMATTING 
    password : str = Field(...,min_length=8) #,max_length= 72
#the user schema for the response model
class User(BaseModel) : 
    id : int
    username : str 
    email : EmailStr
    class Config : 
        orm_mode  =True
class Admin(BaseModel) : 
    id : int
    username: str 
    email : EmailStr
    is_admin : bool 
    class Config : 
        orm_mode = True
class UserLogin(BaseModel) : 
    email : EmailStr
    password : str 

class AdminCreate(BaseModel) : 
    username : str =  Field(...,min_length=3,max_length = 50)
    email : EmailStr #IT ENSURES PROPER EMIAL FORMATTING 
    password : str = Field(... ,min_length=8) #,max_length= 72 ,
    is_admin : bool = True

#user token for the session token verification
class Token(BaseModel) : 
    access_token : str 
    token_type: str



