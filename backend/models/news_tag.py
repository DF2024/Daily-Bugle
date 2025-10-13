from sqlmodel import SQLModel, Field


class NewsTag(SQLModel, table=True):
    news_id: int = Field(foreign_key="news.id", primary_key=True)
    tag_id: int = Field(foreign_key="tag.id", primary_key=True)
