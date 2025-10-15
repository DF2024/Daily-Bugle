from http.client import HTTPException
from sqlmodel import Session, select
from backend.models.user import User
from backend.auth import auth
from backend.schema.users import UserCreate, UserUpdate 

def get_all_users(db : Session): 
    return db.exec(select(User)).all()

def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)

def create_users(db: Session, user_data: UserCreate):
    statament = select(User).where(User.username == user_data.username)
    existing_user = db.exec(statament).first()

    if existing_user:
        raise HTTPException(status_code = 400, detail = "El usuario ya existe")
    
    hashed_pw = auth.hash_password(user_data.password)
    new_user = User(
        username = user_data.username,
        email = user_data.email,
        password_hash = hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = db.get(User, user_id)
    if not user:
        return None
    
    if key == "password":
        value = auth.hash_password(value)

    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.get(User, user_id)
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
