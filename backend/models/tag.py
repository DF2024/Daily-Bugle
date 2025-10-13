from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from .news_tag import NewsTag
from .news import News


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    slug: str

    news: List["News"] = Relationship(back_populates="tags", link_model=NewsTag)