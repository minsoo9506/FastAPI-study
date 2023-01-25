from typing import Tuple

from fastapi import Depends, FastAPI, Query


async def pagination(
    skip: int = Query(0, ge=0), limit: int = Query(10, ge=10)
) -> Tuple[int, int]:
    capped_limit = max(100, limit)
    return (skip, capped_limit)


app = FastAPI()


@app.get("/")
async def list_item(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}
