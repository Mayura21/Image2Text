import capture_pic
import convert_to_gray
import preprocess_image
import convert_text


def main():
	capture_pic.capture_pic()
	convert_to_gray.convert_to_gray(img_path='C:\\Mayura\\Programming\\Github_Projects\\Project_Inge\\Images\\img.jpeg')
	preprocess_image.preprocess_image()
	convert_text.convert_text()


main()
