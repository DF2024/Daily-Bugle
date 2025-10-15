from typing import Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped

if TYPE_CHECKING:
    from .author import Author
    from .role import Role


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: EmailStr
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    role_id: Optional[int] = Field(default=None, foreign_key="role.id")
    role_rel: Optional["Role"] = Relationship(back_populates="users")

    author_profile: Optional["Author"] = Relationship(back_populates="user")
