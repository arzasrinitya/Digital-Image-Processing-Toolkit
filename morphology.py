import cv2
import numpy as np


def morphological_operations(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    kernel = np.ones((5, 5), np.uint8)

    erosion = cv2.erode(binary, kernel, iterations=1)

    dilation = cv2.dilate(binary, kernel, iterations=1)

    opening = cv2.morphologyEx(
        binary,
        cv2.MORPH_OPEN,
        kernel
    )

    closing = cv2.morphologyEx(
        binary,
        cv2.MORPH_CLOSE,
        kernel
    )

    return binary, erosion, dilation, opening, closing