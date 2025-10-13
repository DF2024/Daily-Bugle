from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from app.schemas.author import AuthorCreate, AuthorRead, AuthorUpdate
from app.services.author_service import (
    get_all_authors,
    get_author_by_id,
    create_author,
    update_author,
    delete_author,
)
from config.db import SessionDep

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.get("/", response_model=List[AuthorRead])
def list_authors(session: Session = SessionDep):
    return get_all_authors(session)


@router.get("/{author_id}", response_model=AuthorRead)
def read_author(author_id: int, session: Session = SessionDep):
    author = get_author_by_id(session, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/", response_model=AuthorRead, status_code=status.HTTP_201_CREATED)
def create_author_item(data: AuthorCreate, session: Session = SessionDep):
    return create_author(session, data)


@router.put("/{author_id}", response_model=AuthorRead)
def update_author_item(author_id: int, data: AuthorUpdate, session: Session = SessionDep):
    return update_author(session, author_id, data)


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author_item(author_id: int, session: Session = SessionDep):
    delete_author(session, author_id)