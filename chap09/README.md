# chap 09

## 1. Introduction to unit testing with pytest
- pytest를 이용한 unittest [`.py`](./01_intro_unittest.py)
    - 함수의 경우 `test_`로 시작하는 함수를 만들고 `assert`를 이용
- pytest `@pytest.mark.prameterize` [`.py`](./02_intro_unittest%20_parametrize.py)
- pytest `@pytest.fixture` [`.py`](./03_intro_unittest_fixture.py)
    - 중복코드를 줄일 수 있다

## 2. Setting up the testing tools for FastAPI with HTTPX
- `https`, `asgi-lifespan`, `pytest-asyncio`를 이용하여 asynchronous test

## 3. Writing tests for REST API endpoints
- 예시코드 [`.py`](./rest_api_test/)
## 4. Writing tests for WebSocket endpoints
- 예시코드 [`.py`](./websocket_test/)