from typing import Dict, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str


class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]


class DummyDatabase:
    posts: Dict[int, Post] = {}


db = DummyDatabase()
db.posts = {
    1: Post(id=1, title="Post 1", content="Content 1"),
    2: Post(id=2, title="Post 2", content="Content 2"),
}


app = FastAPI()

# 해당하는 id의 post가 있으면 찾고 아니면 404 return
async def get_post_or_404(id: int) -> Post:
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/posts/{id}")
async def get(post: Post = Depends(get_post_or_404)):
    return post


@app.delet("posts/{id}")
async def delete(post: Post = Depends(get_post_or_404)):
    db.posts.pop(post.id)
