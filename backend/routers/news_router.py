from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from app.schemas.news import NewsCreate, NewsRead, NewsUpdate
from app.services.news_service import (
    get_all_news,
    get_news_by_id,
    create_news,
    update_news,
    delete_news,
)
from config.db import SessionDep

router = APIRouter(prefix="/news", tags=["News"])


@router.get("/", response_model=List[NewsRead])
def list_news(session: Session = SessionDep):
    return get_all_news(session)


@router.get("/{news_id}", response_model=NewsRead)
def read_news(news_id: int, session: Session = SessionDep):
    news = get_news_by_id(session, news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news


@router.post("/", response_model=NewsRead, status_code=status.HTTP_201_CREATED)
def create_news_item(data: NewsCreate, session: Session = SessionDep):
    return create_news(session, data)


@router.put("/{news_id}", response_model=NewsRead)
def update_news_item(news_id: int, data: NewsUpdate, session: Session = SessionDep):
    return update_news(session, news_id, data)


@router.delete("/{news_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_news_item(news_id: int, session: Session = SessionDep):
    delete_news(session, news_id)
