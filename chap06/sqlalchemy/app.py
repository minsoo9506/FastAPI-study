from typing import List, Mapping, Tuple, cast

from databases import Database
from fastapi import Depends, FastAPI, HTTPException, Query, status

from chap06.sqlalchemy.database import get_database, sqlalchemy_engine
from chap06.sqlalchemy.models import (CommentCreate, CommentDB, PostCreate,
                                      PostDB, PostPartialUpdate, PostPublic,
                                      comments, metadata, posts)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await get_database().connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event("shutdown")
async def shutdown():
    await get_database().disconnect()


async def pagination(
    skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_post_or_404(
    id: int, database: Database = Depends(get_database)
) -> PostPublic:
    select_post_query = posts.select().where(
        posts.c.id == id
    )  # posts table에서 id라는 컬럼을 의미
    raw_post = await database.fetch_one(
        select_post_query
    )  # query의 결과가 최대 row 1개 일때, fetch_one 사용

    if raw_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    select_post_comments_query = comments.select().where(comments.c.id == id)
    raw_comments = await database.fetch_all(
        select_post_comments_query
    )  # query의 결과가 여러개의 row일 때, fetch_all 사용
    comments_list = [CommentDB(**comment) for comment in raw_comments]

    return PostPublic(**raw_post, comments=comments_list)


@app.get("/posts")
async def list_posts(
    pagination: Tuple[int, int] = Depends(pagination),
    database: Database = Depends(get_database),
) -> List[PostDB]:
    skip, limit = pagination
    select_query = posts.select().offset(skip).limit(limit)
    rows = await database.fetch_all(select_query)

    results = [PostDB(**row) for row in rows]
    return results


# 해당 id의 post 가져오기
@app.get("posts/{id}", response_model=PostPublic)
async def get_post(post: PostPublic = Depends(get_post_or_404)) -> PostPublic:
    return post


# post 만들기
@app.post("/posts", response_model=PostPublic, status_code=status.HTTP_201_CREATED)
async def create_post(
    post: PostCreate, database: Database = Depends(get_database)
) -> PostPublic:
    insert_query = posts.insert().values(post.dict())
    post_id = await database.execute(insert_query)  # id를 eturn 값으로 가짐

    post_db = await get_post_or_404(post_id, database)

    return post_db


# post update
@app.patch("posts/{id}", response_model=PostPublic)
async def update_post(
    post_update: PostPartialUpdate,
    post: PostPublic = Depends(get_post_or_404),
    database: Database = Depends(get_database),
) -> PostPublic:
    update_query = (
        posts.update()
        .where(posts.c.id == post.id)
        .values(post_update.dict(exclude_unset=True))
    )
    await database.execute(update_query)

    post_db = await get_post_or_404(post.id, database)

    return post_db


# post 삭제
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post: PostPublic = Depends(get_post_or_404),
    database: Database = Depends(get_database),
):
    delete_query = posts.delete().where(posts.c.id == post.id)
    await database.execute(delete_query)


# comment
@app.post("/comments", response_model=CommentDB, status_code=status.HTTP_201_CREATED)
async def create_comment(
    comment: CommentCreate, database: Database = Depends(get_database)
) -> CommentDB:
    select_post_query = posts.select().where(posts.c.id == comment.post_id)
    post = await database.fetch_one(select_post_query)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Post {comment.post_id} does not exist",
        )

    insert_query = comments.insert().values(comment.dict())
    comment_id = await database.execute(insert_query)

    select_query = comments.select().where(comments.c.id == comment_id)
    raw_comment = cast(Mapping, await database.fetch_one(select_query))

    return CommentDB(**raw_comment)
