import io

import numpy as np
from PIL import Image
from skimage import color, img_as_float


def bytes_to_image_bin(image_bytes: bytes) -> np.ndarray:
    image_file = Image.open(io.BytesIO(image_bytes))
    image = np.asarray(
        img_as_float(color.rgb2gray(np.array(image_file))), dtype=np.float64
    )

    return image < 0.5


def bin_to_image(image_bin: np.ndarray) -> Image:
    return Image.fromarray((image_bin * 255).astype(np.uint8))


def image_to_stream(image: Image, format: str) -> io.BytesIO:
    image_stream = io.BytesIO()
    image.save(image_stream, format=format)
    image_stream.seek(0)

    return image_stream
