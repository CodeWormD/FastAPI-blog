from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PostResponseScheme(BaseModel):
    id: int
    group_id: Optional[int] = None
    title: str
    text: str
    date: datetime
    
    class Config:
        orm_mode = True


class CreatePostScheme(BaseModel):
    title: str
    text: str
    group_id: Optional[int] = None


class DeletePostScheme(BaseModel):
    id: int


class OkResponseScheme(BaseModel):
    ok: bool


class UpdatePostScheme(BaseModel):
    id: int
    group_id: Optional[int] = None
    title: Optional[str] = None
    text: Optional[str] = None