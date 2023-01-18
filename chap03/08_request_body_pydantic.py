from fastapi import Body, FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.get("/users")
async def create_user(user: User):
    return user
