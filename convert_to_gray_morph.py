import cv2
import numpy as np


def convert_to_gray_morph():
    # frame = cv2.imread('Images/inge_img.jpg.jpg')
    frame = cv2.imread('Images/img.jpeg')
    frame = cv2.resize(frame, (800, 800))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Images/gray.jpg', gray)
    cv2.imshow('Gray Image', gray)

    kernel_size=5
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    morph = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('Images/morph.jpg', morph)
    cv2.imshow('Morph Image', morph)
