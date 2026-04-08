from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    title: Optional[str] = None
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        orm_mode = True


class TitleRequest(BaseModel):
    content: str


class TitleResponse(BaseModel):
    title: str