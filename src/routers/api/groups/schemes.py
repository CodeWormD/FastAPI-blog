from pydantic import BaseModel
from typing import Optional
from ..posts.schemes import PostResponseScheme


class GroupResponseScheme(BaseModel):
    id: int
    name: str
    posts: list[PostResponseScheme] | None = None
    
    class Config:
        orm_mode = True


class CreateGroupScheme(BaseModel):
    name: str


class UpdateGroupScheme(BaseModel):
    id: int
    name: Optional[str] = None


class OkResponseScheme(BaseModel):
    ok: bool


class DeleteGroupScheme(BaseModel):
    id: int