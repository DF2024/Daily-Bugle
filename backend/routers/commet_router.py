from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from app.schemas.comment import CommentCreate, CommentRead, CommentUpdate
from app.services.comment_service import (
    get_comments_by_news,
    create_comment,
    update_comment,
    delete_comment,
)
from app.database import get_session

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.get("/news/{news_id}", response_model=List[CommentRead])
def list_comments(news_id: int, session: Session = Depends(get_session)):
    return get_comments_by_news(session, news_id)


@router.post("/", response_model=CommentRead, status_code=status.HTTP_201_CREATED)
def create_comment_item(data: CommentCreate, session: Session = Depends(get_session)):
    return create_comment(session, data)


@router.put("/{comment_id}", response_model=CommentRead)
def update_comment_item(comment_id: int, data: CommentUpdate, session: Session = Depends(get_session)):
    return update_comment(session, comment_id, data)


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment_item(comment_id: int, session: Session = Depends(get_session)):
    delete_comment(session, comment_id)
