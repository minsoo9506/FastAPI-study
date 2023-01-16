# TIL

## chaper 03
### FastAPI
- `Starlette` (low-level ASGI web framework)과 `pydantic`(data validation library)으로 구현된 프레임워크

### Uvicorn
- libuv를 기반으로 하여 cython으로 구현된 `uvloop`와 http parser `httptools`를 사용하는 ASGI web server

### python 비동기
- 주피터노트북으로 공부 후 정리

### reference
- [Uvicorn 소개](https://chacha95.github.io/2021-01-16-python6/)
- [uvicon, fastapi 비동기 메커니즘 이해](https://m.blog.naver.com/pjt3591oo/222772705407)

### endpoint
- 간단하게 구현 가능 [`.py`](./chap03/01_first_endpoint.py)
- uvicorn으로 로컬서버을 띄운다.
    - `uvicorn 01_first_endpoint:app`명령어를 이용
- `localhost:8000:docs`를 가면 아래와 같은 화면을 볼 수 있고 api를 웹으로 다룰 수 있다. (FastAPI에서 제공)

<details>
<summary>이미지</summary>

![docs](./images/docs.png)

</details>

### path parameter
- path parameter를 type hint를 이용하여 제약을 줄 수 있다.
    - 자료형 [`.py`](./chap03/02_path_parameters_base.py)
    - enum과 클래스를 이용한 제약 [`.py`](./chap03/03_path_parameters_enum.py)
    - FastAPI에서 제공하는 `Path`이용 [`.py`](./chap03/04_path_parameters_Path.py)