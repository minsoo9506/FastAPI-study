from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.params import Depends
from fastapi.security import APIKeyHeader

# hard coding
API_TOKEN = "SECRET_API_TOKEN"

app = FastAPI()

api_key_header = APIKeyHeader(name="TOKEN")  # name은 header에 있는 것을 의미
# 1. header에서 TOKEN의 값을 찾는 역할
# 2. TOKEN값을 넣지 않으면 이용할 수 없게 하는 역할


@app.get("/protected-route")
async def protected_route(token: str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return {"hello": "world"}
