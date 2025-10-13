from typing import Optional
from datetime import datetime
from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: EmailStr
    password_hash: str
    role: str = Field(default="reporter")
    created_at: datetime = Field(default_factory=datetime.utcnow)
