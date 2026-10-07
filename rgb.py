import cv2


def split_rgb_channels(image):
    blue, green, red = cv2.split(image)

    return blue, green, red