from typing import Optional
from pydantic import BaseModel


class TagBase(BaseModel):
    name: str
    slug: str


class TagCreate(TagBase):
    pass


class TagUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None


class TagRead(TagBase):
    id: int

    class Config:
        orm_mode = True
