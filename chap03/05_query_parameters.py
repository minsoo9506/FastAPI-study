from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def get_user(page: int = 1, size: int = 1):
    return {"page": page, "size": size}


# uvicorn으로 서버을 실행하고
# http "http://localhost:8000/users?page=5&size=5" 명령어로 보낼 때
# ? 뒤에 나오는 것들이 query parameter
