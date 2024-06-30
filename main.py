import capture_pic
import convert_to_gray_morph
import preprocess_image
import convert_text


def main():
	capture_pic.capture_pic()
	convert_to_gray_morph.convert_to_gray_morph()
	preprocess_image.preprocess_image()
	convert_text.convert_text()


main()
