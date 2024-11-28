import numpy as np


def count_black_neighbors(image_bin: np.ndarray, x: int, y: int):
    """
    Count the number of black (non-zero) neighboring pixels.

    Args:
        image_bin (np.ndarray): Binary input image
        x (int): X-coordinate of the pixel
        y (int): Y-coordinate of the pixel

    Returns:
        int: Number of black neighboring pixels
    """

    neighbors = [
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    ]

    count = 0
    for nx, ny in neighbors:
        # Check if a neighbor is within image bounds and is a black pixel
        if (
            0 <= nx < image_bin.shape[0]
            and 0 <= ny < image_bin.shape[1]
            and image_bin[nx, ny] > 0
        ):
            count += 1

    return count


def connectivity_number(image_bin: np.ndarray, x: int, y: int):
    """
    Calculate the connectivity number of a pixel.

    Args:
        image_bin (np.ndarray): Binary input image
        x (int): X-coordinate of the pixel
        y (int): Y-coordinate of the pixel

    Returns:
        int: Connectivity number of the pixel
    """

    # Define 8-neighborhood (P2 to P9)
    neighbors = [
        (x - 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
        (x + 1, y),
        (x + 1, y - 1),
        (x, y - 1),
        (x - 1, y - 1),
    ]

    # Count transitions from 0 to 1
    transitions = 0
    for i in range(8):
        curr = neighbors[i]
        next = neighbors[(i + 1) % 8]

        # Check if within bounds
        if (
            0 <= curr[0] < image_bin.shape[0]
            and 0 <= curr[1] < image_bin.shape[1]
            and 0 <= next[0] < image_bin.shape[0]
            and 0 <= next[1] < image_bin.shape[1]
        ):
            # Check transition from background to foreground
            if image_bin[curr[0], curr[1]] == 0 and image_bin[next[0], next[1]] > 0:
                transitions += 1

    return transitions


def hilditch_thin(image_bin: np.ndarray):
    """
    Perform Hilditch thinning algorithm on a binary image.

    Args:
        image_bin (np.ndarray): Binary input image (0 for background, non-zero for foreground).

    Returns:
        np.ndarray: Thinned binary image.
    """

    # Create a copy of the binary image to modify
    thinned_bin = image_bin.copy()
    height, width = thinned_bin.shape

    # Continue until no more changes
    changed = True
    while changed:
        changed = False
        marked_pxs = []

        # Iterate through all pixels
        for x in range(1, height - 1):
            for y in range(1, width - 1):
                # Only process foreground pixels
                if thinned_bin[x, y] == 0:
                    continue

                # Hilditch thinning conditions
                conditions = [
                    # Condition 1: 2 ≤ B(P1) ≤ 6
                    2 <= count_black_neighbors(thinned_bin, x, y) <= 6,
                    # Condition 2: Connectivity number is 1
                    connectivity_number(thinned_bin, x, y) == 1,
                    # Condition 3: At least one of P2, P4, P6 is white
                    thinned_bin[x - 1, y] == 0
                    or thinned_bin[x, y + 1] == 0
                    or thinned_bin[x + 1, y] == 0,
                    # Condition 4: At least one of P4, P6, P8 is white
                    thinned_bin[x, y + 1] == 0
                    or thinned_bin[x + 1, y] == 0
                    or thinned_bin[x, y - 1] == 0,
                ]

                # Mark pixel for removal if all conditions are met
                if all(conditions):
                    marked_pxs.append((x, y))
                    changed = True

        # Remove marked pixels
        for x, y in marked_pxs:
            thinned_bin[x, y] = 0

    return thinned_bin
