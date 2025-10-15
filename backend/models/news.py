# from __future__ import annotations # Puedes mantenerlo
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped 
from sqlalchemy import func
from .news_tag import NewsTag

if TYPE_CHECKING:
    from .author import Author
    from .category import Category
    from .comment import Comment
    from .tag import Tag

class News(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    slug: str
    summary: Optional[str] = None
    content: str
    image_url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, # Valor inicial
        sa_column_kwargs={"onupdate": func.now()} # Auto-actualiza en DB
    )
    is_featured: bool = Field(default=False)
    views: int = Field(default=0)

    author_id: Optional[int] = Field(default=None, foreign_key="author.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")

    author: Mapped[Optional["Author"]] = Relationship(back_populates="news")
    category: Mapped[Optional["Category"]] = Relationship(back_populates="news")
    comments: Mapped[List["Comment"]] = Relationship(back_populates="news")
    tags: Mapped[List["Tag"]] = Relationship(back_populates="news", link_model= NewsTag)