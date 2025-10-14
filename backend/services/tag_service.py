from sqlmodel import Session, select
from backend.models.tag import Tag
from backend.schema.tag import TagCreate, TagUpdate

def get_all_tags(db: Session):
    return db.exec(select(Tag)).all()

def get_tag_by_id(db: Session, tag_id: int):
    return db.get(Tag, tag_id)

def create_tag(db: Session, tag_data: TagCreate):
    tag = Tag(**tag_data.dict())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def update_tag(db: Session, tag_id: int, tag_data: TagUpdate):
    tag = db.get(Tag, tag_id)
    if not tag:
        return None
    for key, value in tag_data.dict(exclude_unset=True).items():
        setattr(tag, key, value)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def delete_tag(db: Session, tag_id: int):
    tag = db.get(Tag, tag_id)
    if not tag:
        return False
    db.delete(tag)
    db.commit()
    return True
