from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from core.thinning import thin_image_bin
from utils.image import bin_to_image, bytes_to_image_bin, image_to_stream

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


@app.post("/image-thinning")
async def thin_image(file: UploadFile):
    image_bytes = await file.read()
    image_bin = bytes_to_image_bin(image_bytes)
    thinned_image = bin_to_image(thin_image_bin(image_bin))

    return StreamingResponse(
        image_to_stream(thinned_image, "png"), media_type="image/png"
    )


def main():
    import uvicorn

    uvicorn.run("api:app", host="localhost", port=8000, reload=True)
