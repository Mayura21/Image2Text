import cv2


def preprocess_image():
    # Read the image
    gray = cv2.imread('Images/gray.jpg', cv2.IMREAD_GRAYSCALE)

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
