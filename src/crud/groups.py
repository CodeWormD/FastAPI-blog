from sqlalchemy.orm import Session

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
):
    return db.query(Group).where(Group.id == id).first()
