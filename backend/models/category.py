from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from .news import News


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    slug: str
    description: Optional[str] = None
    image_url: Optional[str] = None

    news: List["News"] = Relationship(back_populates="category")