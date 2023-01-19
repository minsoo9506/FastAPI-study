from fastapi import FastAPI, Response, status
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    nb_views: int = 100


# dummy db
posts = {1: Post(title="hello", nb_views=100)}

app = FastAPI()


@app.put("/post/{id}")
async def update_or_create(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
        posts[id] = post
    return posts[id]


# http PUT http://localhost:8000/post/1 title='minsoo'
# 결과
# HTTP/1.1 200 OK
# content-length: 32
# content-type: application/json
# date: Thu, 19 Jan 2023 13:14:58 GMT
# server: uvicorn
# {
#     "nb_views": 100,
#     "title": "hello"
# }

# http PUT http://localhost:8000/post/2 title='minsoo'
# 결과
# HTTP/1.1 201 Created -> 원하는 결과가 잘 나왔다.
# content-length: 33
# content-type: application/json
# date: Thu, 19 Jan 2023 13:16:58 GMT
# server: uvicorn
# {
#     "nb_views": 100,
#     "title": "minsoo"
# }
