import cv2
import pytesseract


# Initialize the Tesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\mayur\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 3 --psm 6'  # Tesseract configuration options


def extract_text_from_video():
    # Open the video file
    cap = cv2.VideoCapture(0)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Loop to process each frame of the video
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("End of video.")
            break

        
        # Display the frame
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            convert(frame)
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


def convert(frame):
    frame = cv2.imread('Images/Inge6.jpg')
    frame = cv2.imread('Images/img.jpeg')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Images/gray.jpg', gray)
    preprocessing()


def preprocessing():
    # Read the image
    gray = cv2.imread('Images/gray.jpg', cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur to smoothen the image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # blur = cv2.medianBlur(gray, 5)
    # blur =  cv2.bilateralFilter(gray, 9, 75, 75)

    # Apply adaptive thresholding to binarize the image
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 255, 2)

    # Perform morphological operations to remove small noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # Perform OCR on the grayscale frame
    text = pytesseract.image_to_string(opening, config=custom_config)

    print("Text:")
    print(text)
    cv2.imshow('img', opening)
    cv2.waitKey(0)


if __name__ == "__main__":
    extract_text_from_video()
