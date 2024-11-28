import io

import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


@app.post("/image-thinning")
async def upload_image(file: UploadFile):
    image_bytes = await file.read()
    return StreamingResponse(io.BytesIO(image_bytes), media_type=file.content_type)


def main():
    uvicorn.run("api:app", host="localhost", port=8000, reload=True)
