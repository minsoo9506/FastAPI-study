import asyncio

import httpx
import pytest
import pytest_asyncio
from app import app
from asgi_lifespan import LifespanManager
from fastapi import status


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def test_client():  # request를 만들어서 app에 보내기 위한 HTTPX client instance
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://app.io") as test_client:
            yield test_client


@pytest.mark.asyncio  # asynchronous test는 해당 데코레이터가 필요
async def test_hello_world(test_client: httpx.AsyncClient):
    response = await test_client.get("/")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json == {"hello": "world"}
