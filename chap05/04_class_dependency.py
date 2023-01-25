from typing import Tuple

from fastapi import Depends, FastAPI, Query


class Pagination:
    def __init__(self, max_limit: int = 100):
        self.max_limit = max_limit

    async def __call__(
        self, skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)
    ) -> Tuple[int, int]:
        capped_limit = min(self.max_limit, limit)
        return (skip, capped_limit)


pagination = Pagination(max_limit=50)

app = FastAPI()


@app.get("/")
async def list_item(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}
