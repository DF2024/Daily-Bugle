from sqlmode import SQLModel, Field
from typing import Optional
from datetime import datetime
from pydantic import EmailStr

#id
#name
#bio
#photo_url
#role
#email
#password_hash


class authors(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    name : str = Field(default = None)
    bio : Optional[str] = Field(default = None)
    photo_url : Optional[str] = Field(default = None)
    role : str = Field(default = None)
    email : EmailStr = Field(default = None)