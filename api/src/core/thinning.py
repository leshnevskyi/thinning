from typing import Literal

import numpy as np
from skimage import morphology

from core.hilditch import hilditch_thin


def thin_image_bin(
    image_bin: np.ndarray, method: Literal["default", "hilditch"] = "hilditch"
) -> np.ndarray:
    """Thin a binary image.

    Args:
        image (np.ndarray): Input binary image.
        method (Literal["default", "hilditch"], optional): Thinning method. The `"default"` one uses thinning method from `skimage`.

    Returns:
        np.ndarray: Thinned binary image.
    """
    return (
        hilditch_thin(image_bin) if method == "hilditch" else morphology.thin(image_bin)
    )
