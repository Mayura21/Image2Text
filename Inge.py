from PIL import Image
import cv2
import read_img
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\mayur\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'


read_img.main()

# img = 'Inge4.jpg'
# img = 'img.jpeg'
img = 'cap.jpg'


def show_img(path):
	img = cv2.imread(path)
	screen_width = 800
	screen_height = 600

	resized_image = cv2.resize(img, (screen_width, screen_height))
	
	cv2.imshow('img', resized_image)
	cv2.waitKey(0)


def img2text(img):
	text = pytesseract.image_to_string('img.jpg')
	return text


show_img(img)
text = img2text(img)
print(text)
