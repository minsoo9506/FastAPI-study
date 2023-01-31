# chap 10

## 1. Setting and using environment variables
- pydantic과 `.env`와 같은 파일을 이용한다. [`.py`](./app/)
    - `.env`같은 경우는 git에 올리면 안되는 내용들이 많을 것이다.
- 아래처럼 `Config`의 `env_file`에 경로를 작성해서 사용한다.
```python
from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    environment: str
    database_url: str

    class Config:
        env_file = ".env"

```

## 2. Managin python dependencies
- requirements.txt를 직접 관리한다. `pip freaze`하면 모든 패키지가 다되서 불필요하다.

## 3. Deploying a FastAPI application on a serverless platform
- 다양한 serverless 플랫폴들이 있고 어렵지 않게 이를 이용하여 배포할 수 있다.

## 4. Deploying a FastAPI application with Docker
- [`Dockerfile`](./Dockerfile)

## 5. Deploying a FastAPI application on a traditional server