from sqlalchemy.orm import Session
from typing import List
from db.models import Post, Group


def create_post(
    db: Session,
    group_id: int,
    title: str,
    text: str) -> Post:
    
    post = Post(
        group_id=group_id,
        title=title,
        text=text
    )
    db.add(post)
    db.commit()
    db.refresh(post)

    return post

def get_post(
    db: Session,
    post_id: int
) -> Post:
    return db.query(Post).where(Post.id == post_id).first()

def get_post_all(
    db: Session
) -> List[Post]:
    return db.query(Post).all()

def delete_post(
    db: Session,
    post: Post
) -> None:
    db.delete(post)
    db.commit()

def update_post(
    db: Session,
    post: Post
) -> Post:
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
