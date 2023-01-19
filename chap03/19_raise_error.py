from fastapi import Body, FastAPI, HTTPException, status

app = FastAPI()


@app.post("/password")
async def check_password(password: str = Body(...), password_confirm: str = Body(...)):
    if password != password_confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "msg": "Passwords don't match",
                "hints": ["Check the capslock", "Check one more time"],
            },
        )
    return {"msg": "Passwords match"}


# http POST http://localhost:8000/password password=123 password_confirm=123
# 결과
# HTTP/1.1 200 OK
# content-length: 25
# content-type: application/json
# date: Thu, 19 Jan 2023 13:39:33 GMT
# server: uvicorn
# {
#     "msg": "Passwords match"
# }

# http POST http://localhost:8000/password password=123 password_confirm=1244
# 결과
# HTTP/1.1 400 Bad Request
# content-length: 95
# content-type: application/json
# date: Thu, 19 Jan 2023 13:40:04 GMT
# server: uvicorn
# {
#     "detail": {
#         "hints": [
#             "Check the capslock",
#             "Check one more time"
#         ],
#         "msg": "Passwords don't match"
#     }
# }
