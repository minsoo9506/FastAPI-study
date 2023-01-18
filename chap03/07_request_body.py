from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/users")
async def create_user(name: str = Body(...), age: int = Body(...)):
    return {"name": name, "age": age}
