from __future__ import annotations

from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_name: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_approved: bool = Field(default=False)

    news_id: Optional[int] = Field(default=None, foreign_key="news.id")
    news: Optional["News"] = Relationship(back_populates="comments")