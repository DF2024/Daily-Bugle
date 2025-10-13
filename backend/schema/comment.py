from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class CommentBase(BaseModel):
    user_name: str
    content: str


class CommentCreate(CommentBase):
    news_id: int


class CommentUpdate(BaseModel):
    content: Optional[str] = None
    is_approved: Optional[bool] = None


class CommentRead(CommentBase):
    id: int
    created_at: datetime
    is_approved: bool
    news_id: int

    class Config:
        orm_mode = True
