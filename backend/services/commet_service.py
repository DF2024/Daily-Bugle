from sqlmodel import Session, select
from backend.models.comment import Comment
from backend.schema.comment import CommentCreate, CommentUpdate

def get_comments_by_news(db: Session, news_id: int):
    return db.exec(select(Comment).where(Comment.news_id == news_id)).all()

def get_comment_by_id(db: Session, comment_id: int):
    return db.get(Comment, comment_id)

def create_comment(db: Session, comment_data: CommentCreate):
    comment = Comment(**comment_data.dict())
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def update_comment(db: Session, comment_id: int, comment_data: CommentUpdate):
    comment = db.get(Comment, comment_id)
    if not comment:
        return None
    for key, value in comment_data.dict(exclude_unset=True).items():
        setattr(comment, key, value)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def delete_comment(db: Session, comment_id: int):
    comment = db.get(Comment, comment_id)
    if not comment:
        return False
    db.delete(comment)
    db.commit()
    return True
