import pytesseract
from PIL import Image

def image_to_text(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
        return text

if __name__ == "__main__":
    image_path = "C:\\Mayura\\Programming\\Github_Projects\\Project_Inge\\Inge4.jpg"  # Replace this with the path to your image
    extracted_text = image_to_text(image_path)
    print("Extracted Text:")
    print(extracted_text)
