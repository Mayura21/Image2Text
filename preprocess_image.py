import cv2
import numpy as np


def preprocess_image(img_path='Images/gray.jpg'):
    # Read the image
    gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    # gray = cv2.imread('Images/morph.jpg', cv2.IMREAD_GRAYSCALE)

    kernel_size=5
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('Images/morph.jpg', gray)
    cv2.imshow('Morph Image', gray)

    '''
    # Apply binary thresholding
    threshold_value = 128  # You can change this value as needed
    _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the  binary images
    cv2.imshow('Binary Image', binary_image)
	'''
    # Apply Gaussian blur to smoothen the image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # blur = cv2.medianBlur(gray, 5)
    # blur =  cv2.bilateralFilter(gray, 9, 75, 75)

    # Apply adaptive thresholding to binarize the image
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 255, 2)

    # Perform morphological operations to remove small noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    cv2.imwrite('Images\\preprocessed_img.jpg', opening)
    cv2.imshow('Preprocessed img', opening)


import cv2
import numpy as np


def img_prepreprocessing():
	# Load the image
	image = cv2.imread('Images/img.jpeg')
	image = cv2.resize(image, (600, 600))

	# Check if the image is loaded successfully
	if image is None:
	    print("Error: Could not read the image.")
	else:
	    # 1. Grayscale Conversion
	    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	    
	    # 2. Gaussian Blurring
	    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
	    
	    # 3. Thresholding
	    _, binary_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY)
	    
	    # 4. Edge Detection
	    edges = cv2.Canny(blurred_image, 100, 200)
	    
	    # 5. Dilation and Erosion
	    kernel = np.ones((5, 5), np.uint8)
	    dilated_image = cv2.dilate(binary_image, kernel, iterations=1)
	    eroded_image = cv2.erode(dilated_image, kernel, iterations=1)
	    
	    # 6. Resizing
	    resized_image = cv2.resize(eroded_image, (300, 300))
	    
	    # 7. Normalization
	    # normalized_image = cv2.normalize(resized_image, None, 0, 255, cv2.NORM_MINMAX)
	    normalized_image = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX)
	    
	    # 8. Histogram Equalization (for grayscale images)
	    equalized_image = cv2.equalizeHist(gray_image)
	    
	    # Display the results
	    # cv2.imshow('Original Image', image)
	    # cv2.imshow('Grayscale Image', gray_image)
	    # cv2.imshow('Blurred Image', blurred_image)
	    # cv2.imshow('Binary Image', binary_image)
	    # cv2.imshow('Edges', edges)
	    # cv2.imshow('Dilated Image', dilated_image)
	    # cv2.imshow('Eroded Image', eroded_image)
	    # cv2.imshow('Resized Image', resized_image)
	    cv2.imshow('Normalized Image', normalized_image)
	    # cv2.imshow('Equalized Image', equalized_image)
	    cv2.imwrite('edge.jpg', normalized_image)
	    
	    # Wait until a key is pressed
	    cv2.waitKey(0)
	    
	    # Destroy all OpenCV windows
	    cv2.destroyAllWindows()


# img_prepreprocessing()
