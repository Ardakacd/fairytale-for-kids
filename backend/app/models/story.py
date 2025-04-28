from pydantic import BaseModel
from typing import List
from datetime import datetime

class Page(BaseModel):
    text: str
    imageUrl: str

class StoryCreate(BaseModel):
    prompt: str

class Story(BaseModel):
    id: str
    title: str
    prompt: str
    pages: List[Page]
    createdAt: datetime 