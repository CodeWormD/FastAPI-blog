from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import posts
from db.database import get_db

from .schemes import PostResponseScheme, CreatePostScheme


router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@router.post('/', response_model=PostResponseScheme)
def create_post(
    db: Session = Depends(get_db),
    *,
    data: CreatePostScheme
):
    post = posts.create_post(
        db,
        group_id=data.group_id,
        title=data.title,
        text=data.text
    )
    return post

@router.get('/', response_model=PostResponseScheme)
def get_post(
    db: Session = Depends(get_db),
    *,
    post_id: int = Query(None)
):
    post = posts.get_post(
        db,
        post_id=post_id
    )
    return post