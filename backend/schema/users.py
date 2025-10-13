from sqlmodel import SQLModel
from pydantic import EmailStr

#name
#email
#password
#role

class UserCreate(SQLModel):
    name : str
    email : EmailStr
    password : str
    role : str


class UserLogin(SQLModel):
    name : str
    password: str

class UserResponse(SQLModel):
    id: int
    name: str
    email: EmailStr
    role : str

class Token(SQLModel):
    access_token: str
    token_type: str