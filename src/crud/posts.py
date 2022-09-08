from sqlalchemy.orm import Session

from db.models import Post


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
):
    return db.query(Post).where(Post.id == post_id).first()
