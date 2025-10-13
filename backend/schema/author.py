from typing import Optional, List
from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    role: Optional[str] = None
    email: Optional[str] = None


class AuthorCreate(AuthorBase):
    password: str


class AuthorUpdate(BaseModel):
    name: Optional[str] = None
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    role: Optional[str] = None
    email: Optional[str] = None


class AuthorRead(AuthorBase):
    id: int

    class Config:
        orm_mode = True
