from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from backend.schema.users import UserCreate, UserRead, UserUpdate
from backend.services.user_service import (
    get_all_users,
    get_user_by_id,
    create_users,
    update_user,
    delete_user,
)
from backend.config.db import get_session

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserRead])
def list_users(session: Session = Depends(get_session)):
    return get_all_users(session)


@router.get("/{users_id}", response_model=UserRead)
def read_users(users_id: int, session: Session = Depends(get_session)):
    users = get_user_by_id(session, users_id)
    if not users:
        raise HTTPException(status_code=404, detail="Author not found")
    return users


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_users_item(data: UserCreate, session: Session = Depends(get_session)):
    return create_users(session, data)


@router.put("/{users_id}", response_model=UserRead)
def update_users_item(users_id: int, data: UserUpdate, session: Session = Depends(get_session)):
    return update_user(session, users_id, data)


@router.delete("/{users_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_users_item(users_id: int, session: Session = Depends(get_session)):
    delete_user(session, users_id)