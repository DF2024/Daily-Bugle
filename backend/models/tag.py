from __future__ import annotations

from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from .news_tag import NewsTag


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    slug: str

    news: List["News"] = Relationship(back_populates="tags", link_model=NewsTag)