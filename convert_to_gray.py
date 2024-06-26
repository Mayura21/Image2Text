import cv2


def convert_to_gray(img_path='Images/img.jpg'):
    # frame = cv2.imread('Images/inge_img.jpg.jpg')
    frame = cv2.imread(img_path)
    frame = cv2.resize(frame, (800, 800))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Images/gray.jpg', gray)
    cv2.imshow('Gray Image', gray)
