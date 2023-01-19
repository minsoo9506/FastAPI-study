from fastapi import FastAPI, status
from pydantic import BaseModel


class Post(BaseModel):
    title: str


app = FastAPI()


@app.post("/post", status_code=status.HTTP_201_CREATED)
async def creat_post(post: Post):
    return post
