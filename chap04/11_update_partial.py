from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str


class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostPublic(PostBase):
    id: int


class PostDB(PostBase):
    id: int
    nb_views: int = 0


class DummyDatabase:
    posts: Dict[int, PostDB] = {}


db = DummyDatabase()

app = FastAPI()


@app.patch("/posts/{id}", response_model=PostPublic)
async def partial_update(id: int, post_update: PostPartialUpdate):
    try:
        post_db = db.posts[id]
        updated_fields = post_update.dict(exclude_unset=True)  # 유저가 보낸 부분만 dict로 보냄
        updated_post = post_db.copy(
            update=updated_fields
        )  # 해당하는 부분을 update(수정)하여 dict 복사
        db.posts[id] = updated_post
        return updated_post
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
