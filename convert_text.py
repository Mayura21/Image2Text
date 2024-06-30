import cv2
import pytesseract


# Initialize the Tesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\mayur\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 3 --psm 6'  # Tesseract configuration options


def convert_text(img_path='Images/preprocessed_img.jpg'):
	opening = cv2.imread(img_path)

    # Perform OCR on the grayscale frame
	text = pytesseract.image_to_string(opening, config=custom_config)

	print("Text:")
	print()
	print(text)
	cv2.waitKey(0)


# convert_text()
