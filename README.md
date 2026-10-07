# Digital Image Processing Toolkit

A Python-based toolkit that applies different image-processing techniques to analyze, enhance, and extract features from images.

## Features

- Mean Filtering
- Median Filtering
- Gaussian Filtering
- Canny Edge Detection
- Sobel Edge Detection
- Histogram Equalization
- Hough Line Transform
- Fast Fourier Transform (FFT)
- RGB Channel Manipulation
- Bitwise Operations
- Morphological Operations
- Haar Cascade Face Detection

## Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib

## Project Structure

```text
digital-image-processing-toolkit/
│
├── images/
│   └── input.jpg
│
├── filters.py
├── edges.py
├── histogram.py
├── hough.py
├── frequency.py
├── rgb.py
├── bitwise.py
├── morphology.py
├── face_detection.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

## How to Run
1. Clone the repository
git clone <your-repository-url>
2. Open the project folder
cd digital-image-processing-toolkit
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows PowerShell:

venv\Scripts\Activate.ps1
5. Install the required libraries
pip install -r requirements.txt
6. Run the toolkit
python main.py
## Usage

After running the program, a menu is displayed.

The user can select different image-processing operations such as filtering, edge detection, histogram equalization, FFT, morphology, Hough line detection, RGB channel analysis, bitwise operations, and face detection.

The selected operation is applied to the input image and the processed result is displayed.

## Input Image

The toolkit uses an image stored inside the images folder.

images/input.jpg
## Purpose

This project demonstrates practical applications of digital image processing using Python and OpenCV, including image enhancement, feature extraction, frequency-domain analysis, morphological processing, and object detection.