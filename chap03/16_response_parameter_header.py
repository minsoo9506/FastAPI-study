from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def custom_header(response: Response):
    response.headers["Custom-header"] = "custom header value"
    return {"hello": "world"}


# http GET http://localhost:8000/

# 결과
# HTTP/1.1 200 OK
# content-length: 17
# content-type: application/json
# custom-header: custom header value
# date: Thu, 19 Jan 2023 12:52:13 GMT
# server: uvicorn
# {
#     "hello": "world"
# }
