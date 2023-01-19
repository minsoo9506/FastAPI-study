from fastapi import FastAPI
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    private: int


# dummy db
# 그런데 private는 reponse content 노출을 안하고 싶다!
posts = {1: Post(title="hello", private=100)}

# response model
class Model(BaseModel):
    title: str


app = FastAPI()


@app.get("/post/{id}", response_model=Model)
async def get_post(id: int):
    return posts[id]
