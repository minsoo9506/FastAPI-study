from fastapi import FastAPI, Path

app = FastAPI()


# @app.get("/users/{id}")
# async def get_user(id: int = Path(..., ge=1)): # ... 은 여기서 필수적으로 적어야함을 의미
#     return {"id": id}

# @app.get("/license/{number}")
# async def get_license_number(number: str = Path(..., min_length=6, max_length=6)):
#     return {"number": number}


@app.get("/license/{number}")
async def get_license_number(number: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"number": number}
