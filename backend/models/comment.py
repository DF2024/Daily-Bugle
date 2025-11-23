from typing import Optional, TYPE_CHECKING
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped 

if TYPE_CHECKING:
    from .news import News

class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    author_name: str
    author_email: Optional[str] = None
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    news_id: Optional[int] = Field(default=None, foreign_key="news.id")
    news: Mapped[Optional["News"]] = Relationship(back_populates="comments")
