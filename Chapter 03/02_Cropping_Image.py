import cv2
import numpy as np

img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")

# To print Image Size
print(img.shape)

# Output Format
# (462, 623, 3) --> they denote (height, width, channels - BGR)

# Cropping the image
imgCropped = img[0:100, 200:480]

# Output format
# img[0:100, 200:480] --> <source>[height_start : height_end, width_start : width_end]
# HEIGHT --> y axis and the WIDTH --> x axis

# Displaying the Image
cv2.imshow("Image", img)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)