from sqlmodel import Session, select
from backend.models.category import Category
from backend.schema.category import CategoryCreate, CategoryUpdate

def get_all_categories(db: Session):
    return db.exec(select(Category)).all()

def get_category_by_id(db: Session, category_id: int):
    return db.get(Category, category_id)

def create_category(db: Session, category_data: CategoryCreate):
    category = Category(**category_data.dict())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(db: Session, category_id: int, category_data: CategoryUpdate):
    category = db.get(Category, category_id)
    if not category:
        return None
    for key, value in category_data.dict(exclude_unset=True).items():
        setattr(category, key, value)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.get(Category, category_id)
    if not category:
        return False
    db.delete(category)
    db.commit()
    return True
