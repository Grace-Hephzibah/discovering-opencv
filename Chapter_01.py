import cv2

# print("Package Imported")

## VIDEO

# Storing the video in a variable
cap = cv2.VideoCapture("resources/city.mp4")

# Displaying it in the output window as a series of images
while True:
    success, img = cap.read()
    cv2.imshow("Video Console", img)

    # Making the video console screen to end when the letter 'q' is pressed
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

## IMAGES

# Storing the image in a variable
# img = cv2.imread("resources/girl.jpg")

# Displaying the variable with the image in a window called "Output Window"
# cv2.imshow("Output Window", img)

# The output window does not last long for view. So,
# cv2.waitKey(0)
# 0 -> Infinite until window is closed
# any other positive value is milli second ( Ex. 1000 = 1s )
