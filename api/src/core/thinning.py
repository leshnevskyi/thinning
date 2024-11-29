from typing import Literal

import numpy as np
from core.hilditch import hilditch_thin
from skimage import morphology


def thin_image_bin(
    image_bin: np.ndarray, algo: Literal["zhang-suen", "hilditch"] = "hilditch"
) -> np.ndarray:
    """
    Thin a binary image.

    Args:
        image (np.ndarray): Input binary image.
        algo (Literal["zhang-suen", "hilditch"], optional): Thinning algorithm. The `"zhang-suen"` is implemented in `skimage`.

    Returns:
        np.ndarray: Thinned binary image.
    """
    return (
        hilditch_thin(image_bin) if algo == "hilditch" else morphology.thin(image_bin)
    )
