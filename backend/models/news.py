from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from models import Author, Category, Comment, Tag

class News(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    slug: str
    summary: Optional[str] = None
    content: str
    image_url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    is_featured: bool = Field(default=False)
    views: int = Field(default=0)

    author_id: Optional[int] = Field(default=None, foreign_key="author.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")

    author: Optional["Author"] = Relationship(back_populates="news")
    category: Optional["Category"] = Relationship(back_populates="news")
    comments: List["Comment"] = Relationship(back_populates="news")
    tags: List["Tag"] = Relationship(back_populates="news", link_model="NewsTag")
