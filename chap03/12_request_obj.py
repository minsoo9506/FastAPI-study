from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def get_req_obj(req: Request):
    return {"path": req.url.path}
