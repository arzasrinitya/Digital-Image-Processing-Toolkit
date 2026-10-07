import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_fft(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    fft = np.fft.fft2(gray)

    fft_shift = np.fft.fftshift(fft)

    magnitude = 20 * np.log(np.abs(fft_shift) + 1)

    plt.imshow(magnitude, cmap="gray")
    plt.title("FFT Frequency Spectrum")
    plt.axis("off")
    plt.show()