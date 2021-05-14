import cv2

## IMAGES

# Storing the image in a variable
img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")

# Displaying the variable with the image in a window called "Output Window"
cv2.imshow("Output Window", img)

# The output window does not last long for view. So,
cv2.waitKey(0)
# 0 -> Infinite until window is closed
# any other positive value is milli second ( Ex. 1000 = 1s )