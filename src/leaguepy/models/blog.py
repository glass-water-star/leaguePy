from typing import Optional, List
from pydantic import BaseModel


class Blog(BaseModel):
    blogId: int
    title: str
    summary: str
    urlHtml: str
    createdOn: int
    lastUpdated: int
    featured: bool
    imageUrl: str
    halfImageUrl: str


class BlogsResponse(BaseModel):
    __root__: List[Blog]
