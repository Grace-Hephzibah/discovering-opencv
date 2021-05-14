import cv2

# print("Package Imported")

## IMAGES

# img = cv2.imread("resources/girl.jpg")
# cv2.imshow("Output Window", img)
# cv2.waitKey(0)

## VIDEO

# Storing the video in a variable
# cap = cv2.VideoCapture("resources/city.mp4")

# Displaying it in the output window as a series of images
'''
while True:
    success, img = cap.read()
    cv2.imshow("Video Console", img)

    # Making the video console screen to end when the letter 'q' is pressed
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
'''

## WEBCAM

# 0 refers to the default webcam. If more than 1 webcam is used, use the ID of the webcam
# cap = cv2.VideoCapture(0)

# Altering the properties
'''
cap.set(3, 640) # 3 -> width
cap.set(4, 480) # 4 -> height
cap.set(10, 10) # 10 -> brightness
'''

# Displaying it in the output window as a series of images
'''
while True:
    success, img = cap.read()
    cv2.imshow("Video Console", img)

    # Making the video console screen to end when the letter 'q' is pressed
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
'''