from sqlmodel import SQLModel
from pydantic import EmailStr

#id
#name
#bio
#photo_url
#role
#email
#password_hash

class AuthorCreate(SQLModel):
    name : str
    email : EmailStr
    bio : str
    photo_url : str
    role : str
    password: str

class AuthorLogin(SQLModel):
    name : str
    password : str

class AuthorResponse(SQLModel):
    id: int
    name: str
    email: EmailStr

class AuthorUpdate(SQLModel):
    name : str
    email : str