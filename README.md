# Additional TIL
- FastAPI
    - `Starlette` (low-level ASGI web framework)과 `pydantic`(data validation library)으로 구현된 프레임워크
- Uvicorn
    - libuv를 기반으로 하여 cython으로 구현된 `uvloop`와 http parser `httptools`를 사용하는 ASGI web server

### python 비동기
- 주피터노트북으로 공부 후 정리

### reference
- [Uvicorn 소개](https://chacha95.github.io/2021-01-16-python6/)
- [uvicon, fastapi 비동기 메커니즘 이해](https://m.blog.naver.com/pjt3591oo/222772705407)

# [Chapter 03](./chap03/) Developing a RESTful API with FASTAPI
1. Handling request parameters
    - endpoint
    - path parameter
    - query parameter
    - request body
    - Form data and File upload
    - headers and cookies
    - request object
2. Customizing the response
    - path operation parameters
    - reponse parameter
    - setting the status code dynamically
3. Raising HTTP errors
4. Building a custom response
    - using the `response_class` parameter
    - custom reponse

# [Chapter 04](./chap04/) Managing Pydantic Data Models in FastAPI
1. Defining models and their field types with Pydantic
    - standard field types
    - optional fields and default values
    - field validation
    - dynamic default values
    - validating email addresses and URLs with pydantic type
2. Creating model variations with class inheritance
3. Adding custom data validation with Pydantic
    - applying validation at a field level
    - applying validation at an object level
    - applying validation before pydantic parsing
4. Working with Pydantic objects
    - converting an object into a dictionary
    - updating an instance with a partial one

# [Chapter 05](./chap05/) Dependency Injections in FastAPI
1. What is dependency injection?
2. Creating and using a function dependency
    - get an object or raise a 404 error
3. Creating and using a parameterized dependency with a class
    - use class methods as dependencies
4. Using dependencies at a path, router, and global level

# [Chapter 06](./chap06/) Databases and Asynchronous ORMs
1. An overview of relational and NoSQL databases
2. Communicating with a SQL database with SQLAlchemy
3. Communicating with a SQL database with Tortoise ORM
4. Communicating with a MongoDB database using Motor