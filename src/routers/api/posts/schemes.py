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
    
    