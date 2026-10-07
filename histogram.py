import cv2
import matplotlib.pyplot as plt


def histogram_equalization(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)

    return gray, equalized


def show_histograms(gray, equalized):
    plt.figure()

    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title("Original Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.figure()

    plt.hist(equalized.ravel(), 256, [0, 256])
    plt.title("Equalized Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.show()