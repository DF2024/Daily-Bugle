from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from backend.config.db import get_session
from backend.services.role_service import (
    create_role, get_roles, get_role_by_id, delete_role
)
from backend.schema.role import RoleCreate, RoleRead

router = APIRouter(prefix="/roles", tags=["Roles"])


@router.post("/", response_model=RoleRead)
def create_new_role(role: RoleCreate, db: Session = Depends(get_session)):
    return create_role(db, role)


@router.get("/", response_model=list[RoleRead])
def list_roles(db: Session = Depends(get_session)):
    return get_roles(db)


@router.get("/{role_id}", response_model=RoleRead)
def get_role(role_id: int, db: Session = Depends(get_session)):
    role = get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.delete("/{role_id}")
def remove_role(role_id: int, db: Session = Depends(get_session)):
    if not delete_role(db, role_id):
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted"}
