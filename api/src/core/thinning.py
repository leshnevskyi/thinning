import numpy as np
from skimage import morphology


def thin_image_bin(image_bin: np.ndarray) -> np.ndarray:
    """Thin a binary image.

    Args:
        image (np.ndarray): Input binary image.

    Returns:
        np.ndarray: Thinned binary image.
    """
    return morphology.thin(image_bin)
