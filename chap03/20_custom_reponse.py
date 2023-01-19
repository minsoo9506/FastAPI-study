from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI()

html_val = """
<html>
    <head> Hello World </head>
</html>
"""


@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return html_val


@app.get("/text", response_class=PlainTextResponse)
async def get_text():
    return "Hello World"


# http GET http://localhost:8000/html
# 결과
# HTTP/1.1 200 OK
# content-length: 47
# content-type: text/html; charset=utf-8
# date: Thu, 19 Jan 2023 13:51:06 GMT
# server: uvicorn
# <html>
#     <head> Hello World </head>
# </html>

# http GET http://localhost:8000/text
# 결과
# HTTP/1.1 200 OK
# content-length: 11
# content-type: text/plain; charset=utf-8
# date: Thu, 19 Jan 2023 13:51:10 GMT
# server: uvicorn
# Hello World
