from pydantic import BaseModel


class GroupResponseScheme(BaseModel):
    id: int
    name: str
    
    class Config:
        orm_mode = True


class CreateGroupScheme(BaseModel):
    name: str
    
    