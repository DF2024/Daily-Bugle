from http.client import HTTPException
from sqlmodel import Session, select
from backend.models.user import User
from backend.auth import auth
from backend.schema.users import UserCreate, UserUpdate, UserRead 

def get_all_users(db : Session): 
    users = db.exec(select(User)).all()
    result = []
    for user in users:
        role_name = user.role_rel.name if user.role_rel else None
        result.append(UserRead(
            id=user.id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            role_name=role_name 
        )) 
    return result 

def get_user_by_id(db: Session, user_id: int):
    user = db.get(User, user_id)
    if not user:
        return None
    return UserRead(
        id=user.id,
        username=user.username,
        email=user.email,
        created_at=user.created_at,
        role_name=user.role_rel.name if user.role_rel else None
    )

def create_users(db: Session, user_data: UserCreate):
    statament = select(User).where(User.username == user_data.username)
    existing_user = db.exec(statament).first()

    if existing_user:
        raise HTTPException(status_code = 400, detail = "El usuario ya existe")
    
    hashed_pw = auth.hash_password(user_data.password)
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_pw,
        role_id=user_data.role_id,
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
