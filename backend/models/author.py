# from __future__ import annotations # Puedes mantenerlo
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped 

if TYPE_CHECKING:
    from .news import News

class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    role: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None

    news: Mapped[List["News"]] = Relationship(back_populates="author")
    
