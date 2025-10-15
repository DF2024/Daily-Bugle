# from __future__ import annotations # Puedes mantenerlo
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped 
from .news_tag import NewsTag

if TYPE_CHECKING:
    from .news import News


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    news: Mapped[List["News"]] = Relationship(back_populates="tags", link_model=NewsTag)
