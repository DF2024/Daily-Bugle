from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from app.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate
from app.services.category_service import (
    get_all_categories,
    get_category_by_id,
    create_category,
    update_category,
    delete_category,
)
from config.db import SessionDep

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryRead])
def list_categories(session: Session = Depends(SessionDep)):
    return get_all_categories(session)


@router.get("/{category_id}", response_model=CategoryRead)
def read_category(category_id: int, session: Session = Depends(SessionDep)):
    category = get_category_by_id(session, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category_item(data: CategoryCreate, session: Session = Depends(SessionDep)):
    return create_category(session, data)


@router.put("/{category_id}", response_model=CategoryRead)
def update_category_item(category_id: int, data: CategoryUpdate, session: Session = Depends(SessionDep)):
    return update_category(session, category_id, data)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category_item(category_id: int, session: Session = Depends(SessionDep)):
    delete_category(session, category_id)
