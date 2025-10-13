from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class NewsBase(BaseModel):
    title: str
    slug: str
    summary: Optional[str] = None
    content: str
    image_url: Optional[str] = None
    is_featured: bool = False


class NewsCreate(NewsBase):
    category_id: Optional[int] = None
    author_id: Optional[int] = None


class NewsUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    image_url: Optional[str] = None
    is_featured: Optional[bool] = None
    category_id: Optional[int] = None


class NewsRead(NewsBase):
    id: int
    views: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    category_id: Optional[int] = None
    author_id: Optional[int] = None

    class Config:
        orm_mode = True
