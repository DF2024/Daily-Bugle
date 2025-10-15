from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from datetime import timedelta
from backend.models.user import User
from backend.auth.auth import create_access_token, verify_password, ACCESS_TOKEN_EXPIRE_MINUTES
from backend.config.db import get_session


router = APIRouter(prefix ="/auth", tags=["Auth"])

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    session: Session = Depends(get_session)
    ):

    statament = select(User).where(User.username == form_data.username)
    user = session.exec(statament).first()

    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id), "role": user.role_rel.name if user.role_rel else "user"},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}