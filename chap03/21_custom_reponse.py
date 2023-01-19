from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/xml")
async def get_xml():
    content = """
        hello world
    """
    return Response(content=content, media_type="application/xml")


# http GET http://localhost:8000/xml
# 결과
# HTTP/1.1 200 OK
# content-length: 25
# content-type: application/xml
# date: Thu, 19 Jan 2023 13:56:41 GMT
# server: uvicorn
#
#         hello world
