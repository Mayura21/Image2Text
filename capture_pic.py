import cv2


def capture_pic():
    # Open the video file
    cap = cv2.VideoCapture(0)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Loop to process each frame of the video
    while True:
        # Capture frame-by-frame
        ret, img = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("End of video.")
            break

        
        # Display the image
        cv2.imshow('Captured_image', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Save the image
            cv2.imwrite('Images/inge_img.jpg', img)
            break

    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

