from sqlmodel import Session, select
from backend.models.author import Author
from backend.schema.author import AuthorCreate, AuthorUpdate

def get_all_authors(db: Session):
    return db.exec(select(Author)).all()

def get_author_by_id(db: Session, author_id: int):
    return db.get(Author, author_id)

def create_author(db: Session, author_data: AuthorCreate):
    author = Author(**author_data.dict())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

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
