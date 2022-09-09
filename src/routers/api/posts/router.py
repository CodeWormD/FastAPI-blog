from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import posts
from db.database import get_db

from .schemes import (
    PostResponseScheme,
    CreatePostScheme,
    DeletePostScheme,
    OkResponseScheme,
    UpdatePostScheme)


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
    return posts.create_post(
        db,
        group_id=data.group_id,
        title=data.title,
        text=data.text
    )

@router.get('/', response_model=PostResponseScheme)
def get_post(
    db: Session = Depends(get_db),
    *,
    post_id: int = Query(None)
):
    return posts.get_post(
        db,
        post_id=post_id
    )

@router.get('/all', response_model=List[PostResponseScheme])
def get_post_all(
    db: Session = Depends(get_db)
):
    return posts.get_post_all(db)

@router.delete('/', response_model=OkResponseScheme)
def delete_post(
    db: Session = Depends(get_db),
    *,
    data: DeletePostScheme
):
    post = posts.get_post(db, data.id)
    posts.delete_post(db, post)
    return{'ok': True}

@router.patch('/', response_model=PostResponseScheme)
def update_post(
    db: Session = Depends(get_db),
    *,
    data: UpdatePostScheme
):
    post = posts.get_post(db, data.id)
    if data.group_id or data.text or data.title:
        post.group_id = data.group_id
        post.text = data.text
        post.title = data.title

    return posts.update_post(db, post)
