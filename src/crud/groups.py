from sqlalchemy.orm import Session
from typing import List
from db.models import Group


def create_group(
    db: Session,
    name: str,
) -> Group:
    
    group = Group(
        name=name,

    )
    db.add(group)
    db.commit()
    db.refresh(group)

    return group

def get_group(
    db: Session,
    id: int
) -> Group:
    return db.query(Group).where(Group.id == id).first()

def get_groups_all(
    db: Session
) -> List[Group]:
    return db.query(Group).all()

def patch_group(
    db: Session,
    group: Group
) -> Group:
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

def delete_group(
    db: Session,
    group: Group
) -> None:
    db.delete(group)
    db.commit()
    
