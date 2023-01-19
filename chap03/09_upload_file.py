from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/file")
async def get_file(file: UploadFile = File(...)):
    return {"file_name": file.name, "content_type": file.content_type}
