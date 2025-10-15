from sqlmodel import Session, select
from backend.models.role import Role
from backend.schema.role import RoleCreate


def create_role(db: Session, role_data: RoleCreate):
    role = Role(**role_data.dict())
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


def get_roles(db: Session):
    return db.exec(select(Role)).all()


def get_role_by_id(db: Session, role_id: int):
    return db.get(Role, role_id)


def delete_role(db: Session, role_id: int):
    role = db.get(Role, role_id)
    if role:
        db.delete(role)
        db.commit()
        return True
    return False
