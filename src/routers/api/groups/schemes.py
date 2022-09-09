from pydantic import BaseModel
from typing import Optional

class GroupResponseScheme(BaseModel):
    id: int
    name: str
    
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