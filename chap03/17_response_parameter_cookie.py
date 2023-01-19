from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def custom_cookie(reponse: Response):
    reponse.set_cookie(
        key="cookie-name", value="cookie-value", max_age=86400
    )  # 86400초 동안 valid
    return {"hello": "world"}


# http GET http://localhost:8000/

# 결과
# HTTP/1.1 200 OK
# content-length: 17
# content-type: application/json
# date: Thu, 19 Jan 2023 12:56:27 GMT
# server: uvicorn
# set-cookie: cookie-name=cookie-value; Max-Age=86400; Path=/; SameSite=lax
# {
#     "hello": "world"
# }
