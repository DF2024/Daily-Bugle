from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List
from app.schemas.tag import TagCreate, TagRead, TagUpdate
from app.services.tag_service import (
    get_all_tags,
    create_tag,
    update_tag,
    delete_tag,
)
from config.db import SessionDep

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.get("/", response_model=List[TagRead])
def list_tags(session: Session = SessionDep):
    return get_all_tags(session)


@router.post("/", response_model=TagRead, status_code=status.HTTP_201_CREATED)
def create_tag_item(data: TagCreate, session: Session = SessionDep):
    return create_tag(session, data)


@router.put("/{tag_id}", response_model=TagRead)
def update_tag_item(tag_id: int, data: TagUpdate, session: Session = SessionDep):
    return update_tag(session, tag_id, data)


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag_item(tag_id: int, session: Session = SessionDep):
    delete_tag(session, tag_id)
