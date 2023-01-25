from typing import Optional

from fastapi import Depends, FastAPI, Header, HTTPException, status

app = FastAPI()


def secret_header(secret_header: Optional[str] = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)


@app.get(
    "/protected-route", dependencies=[Depends(secret_header)]
)  # 여러 개의 dependency를 넣을 수 있다, return 값이 없어서 데코레이터에 넣을 수 있다
async def protected_route():
    return {"hello": "world"}
