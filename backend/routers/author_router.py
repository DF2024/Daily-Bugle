from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from backend.schema.author import AuthorCreate, AuthorRead, AuthorUpdate
from backend.services.author_service import (
    get_all_authors,
    get_author_by_id,
    create_author,
    update_author,
    delete_author,
)
from backend.config.db import get_session

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.get("/", response_model=List[AuthorRead])
def list_authors(session: Session = Depends(get_session)):
    return get_all_authors(session)


@router.get("/{author_id}", response_model=AuthorRead)
def read_author(author_id: int, session: Session = Depends(get_session)):
    author = get_author_by_id(session, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/", response_model=AuthorRead, status_code=status.HTTP_201_CREATED)
def create_author_item(data: AuthorCreate, session: Session = Depends(get_session)):
    return create_author(session, data)


@router.put("/{author_id}", response_model=AuthorRead)
def update_author_item(author_id: int, data: AuthorUpdate, session: Session = Depends(get_session)):
    return update_author(session, author_id, data)


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author_item(author_id: int, session: Session = Depends(get_session)):
    delete_author(session, author_id)