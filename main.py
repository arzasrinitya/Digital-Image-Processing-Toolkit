import cv2

from filters import mean_filter, median_filter, gaussian_filter
from edges import canny_edge_detection, sobel_edge_detection
from histogram import histogram_equalization, show_histograms
from hough import detect_lines
from frequency import show_fft
from rgb import split_rgb_channels
from bitwise import bitwise_operations
from morphology import morphological_operations
from face_detection import detect_faces


image = cv2.imread("images/input.jpg")


while True:

    print("\n===== DIGITAL IMAGE PROCESSING TOOLKIT =====")
    print("1. Mean Filter")
    print("2. Median Filter")
    print("3. Gaussian Filter")
    print("4. Canny Edge Detection")
    print("5. Sobel Edge Detection")
    print("6. Histogram Equalization")
    print("7. Hough Line Transform")
    print("8. FFT")
    print("9. RGB Channels")
    print("10. Bitwise Operations")
    print("11. Morphological Operations")
    print("12. Face Detection")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        result = mean_filter(image)
        cv2.imshow("Mean Filter", result)

    elif choice == "2":
        result = median_filter(image)
        cv2.imshow("Median Filter", result)

    elif choice == "3":
        result = gaussian_filter(image)
        cv2.imshow("Gaussian Filter", result)

    elif choice == "4":
        result = canny_edge_detection(image)
        cv2.imshow("Canny Edge Detection", result)

    elif choice == "5":
        result = sobel_edge_detection(image)
        cv2.imshow("Sobel Edge Detection", result)

    elif choice == "6":
        gray, equalized = histogram_equalization(image)
        cv2.imshow("Original Grayscale", gray)
        cv2.imshow("Histogram Equalized", equalized)
        show_histograms(gray, equalized)

    elif choice == "7":
        edges, result = detect_lines(image)
        cv2.imshow("Hough Edges", edges)
        cv2.imshow("Hough Lines", result)

    elif choice == "8":
        show_fft(image)

    elif choice == "9":
        blue, green, red = split_rgb_channels(image)
        cv2.imshow("Blue Channel", blue)
        cv2.imshow("Green Channel", green)
        cv2.imshow("Red Channel", red)

    elif choice == "10":
        results = bitwise_operations(image)

        cv2.imshow("Mask 1", results[0])
        cv2.imshow("Mask 2", results[1])
        cv2.imshow("AND", results[2])
        cv2.imshow("OR", results[3])
        cv2.imshow("XOR", results[4])
        cv2.imshow("NOT", results[5])

    elif choice == "11":
        results = morphological_operations(image)

        cv2.imshow("Binary", results[0])
        cv2.imshow("Erosion", results[1])
        cv2.imshow("Dilation", results[2])
        cv2.imshow("Opening", results[3])
        cv2.imshow("Closing", results[4])

    elif choice == "12":
        result, count = detect_faces(image)

        cv2.imshow("Face Detection", result)
        print("Faces detected:", count)

    elif choice == "0":
        print("Exiting toolkit...")
        break

    else:
        print("Invalid choice!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()