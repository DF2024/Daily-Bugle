from http.client import HTTPException
from sqlmodel import Session, select
from backend.models.author import Author
from backend.auth import auth
from backend.schema.author import AuthorCreate, AuthorUpdate

def get_all_authors(db: Session):
    return db.exec(select(Author)).all()

def get_author_by_id(db: Session, author_id: int):
    return db.get(Author, author_id)

def create_author(db: Session, author_data: AuthorCreate):
    statament = select(Author).where(Author.name == author_data.name)
    existing_author = db.exec(statament).first()

    if existing_author:
        raise HTTPException(status_code  = 400, detail = "El autor ya existe")
    
    hashed_pw = auth.hash_password(author_data.password)
    new_author = Author(
        name = author_data.name,
        bio = author_data.bio,
        photo_url = author_data.photo_url,
        role = author_data.role,
        email = author_data.email,
        password_hash = hashed_pw
    )

    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

def update_author(db: Session, author_id: int, author_data: AuthorUpdate):
    author = db.get(Author, author_id)
    if not author:
        return None
    for key, value in author_data.dict(exclude_unset=True).items():
        setattr(author, key, value)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def delete_author(db: Session, author_id: int):
    author = db.get(Author, author_id)
    if not author:
        return False
    db.delete(author)
    db.commit()
    return True
