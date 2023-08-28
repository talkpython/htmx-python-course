from typing import Optional

from pydantic import BaseModel


class Video(BaseModel):
    id: str
    title: str
    url: str
    author: str
    views: int
    category: Optional[str] = None
