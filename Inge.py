import capture_pic
import convert_to_gray
import preprocess_image
import convert_text


def main():
	capture_pic.capture_pic()
	convert_to_gray.convert_to_gray()
	preprocess_image.preprocess_image()
	convert_text.convert_text()


main()
