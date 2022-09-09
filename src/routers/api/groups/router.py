from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud import groups
from db.database import get_db

from .schemes import (
    GroupResponseScheme, CreateGroupScheme, UpdateGroupScheme,
    OkResponseScheme, DeleteGroupScheme)


router = APIRouter(
    prefix='/groups',
    tags=['groups']
)


@router.post('/', response_model=GroupResponseScheme)
def create_group(
    db: Session = Depends(get_db),
    *,
    data: CreateGroupScheme
):
    return groups.create_group(
        db,
        name=data.name
    )

@router.get('/', response_model=GroupResponseScheme)
def get_group(
    db: Session = Depends(get_db),
    *,
    id: int = Query(None)
):
    return groups.get_group(
        db,
        id=id
    )

@router.get('/all', response_model=List[GroupResponseScheme])
def get_group(
    db: Session = Depends(get_db)
):
    return groups.get_groups_all(db)

@router.patch('/', response_model=GroupResponseScheme)
def update_group(
    db: Session = Depends(get_db),
    *,
    data: UpdateGroupScheme
):
    
    group = groups.get_group(db, data.id)
    if data.name:
        group.name = data.name
    return groups.patch_group(db, group)

@router.delete('/', response_model=OkResponseScheme)
def delete_group(
    db: Session = Depends(get_db),
    *,
    data: DeleteGroupScheme
):
    group = groups.get_group(db, data.id)
    groups.delete_group(db, group)
    return{'ok': True}