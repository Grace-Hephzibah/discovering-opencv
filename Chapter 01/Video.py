import cv2

## VIDEO

# Storing the video in a variable
cap = cv2.VideoCapture("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/city.mp4")

# Displaying it in the output window as a series of images
while True:
    success, img = cap.read()
    cv2.imshow("Video Console", img)

    # Making the video console screen to end when the letter 'q' is pressed
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break