from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from .role import RoleRead


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    role_id: Optional[int] = None  # Se asigna un rol al crear el usuario


class UserRead(UserBase):
    id: int
    created_at: datetime
    role_name: Optional[str] = None # Incluye datos del rol
    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role_id: Optional[int] = None
