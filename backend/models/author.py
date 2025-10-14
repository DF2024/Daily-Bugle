from __future__ import annotations

from typing import Optional, List
from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship


class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    role: Optional[str] = None
    email: Optional[EmailStr] = None
    password_hash: Optional[str] = None

    news: List["News"] = Relationship(back_populates="author")