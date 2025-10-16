from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from backend.schema.news import NewsCreate, NewsRead, NewsUpdate
from backend.dependencies.auth_dependencies import require_role
from backend.services.news_service import (
    get_all_news,
    get_news_by_id,
    create_news,
    update_news,
    delete_news,
)
from backend.config.db import get_session

router = APIRouter(prefix="/news", tags=["News"])


@router.get("/", response_model=List[NewsRead])
def list_news(session: Session = Depends(get_session)):
    return get_all_news(session)


@router.get("/{news_id}", response_model=NewsRead)
def read_news(news_id: int, session: Session = Depends(get_session)):
    news = get_news_by_id(session, news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news


@router.post("/", response_model=NewsRead, status_code=status.HTTP_201_CREATED)
def create_news_item(
        data: NewsCreate, 
        session: Session = Depends(get_session),
        current_user = Depends(require_role(["Admin", "Periodista"]))
        ):
    return create_news(session, data)


@router.put("/{news_id}", response_model=NewsRead)
def update_news_item(news_id: int, data: NewsUpdate, session: Session = Depends(get_session)):
    return update_news(session, news_id, data)


@router.delete("/{news_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_news_item(news_id: int, session: Session = Depends(get_session)):
    delete_news(session, news_id)
