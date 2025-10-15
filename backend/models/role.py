from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from sqlalchemy.orm import Mapped 


class Role(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    description: Optional[str] = None

    users : Mapped[List["User"]] = Relationship(back_populates = "role_rel")

