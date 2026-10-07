import cv2
import numpy as np


def bitwise_operations(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, mask1 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    _, mask2 = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    bitwise_and = cv2.bitwise_and(mask1, mask2)
    bitwise_or = cv2.bitwise_or(mask1, mask2)
    bitwise_xor = cv2.bitwise_xor(mask1, mask2)
    bitwise_not = cv2.bitwise_not(mask1)

    return mask1, mask2, bitwise_and, bitwise_or, bitwise_xor, bitwise_not