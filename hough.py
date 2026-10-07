import cv2
import numpy as np


def detect_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    lines = cv2.HoughLinesP(
        edges,
        1,
        np.pi / 180,
        threshold=80,
        minLineLength=50,
        maxLineGap=10
    )

    result = image.copy()

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.flatten()

            cv2.line(
                result,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

    return edges, result