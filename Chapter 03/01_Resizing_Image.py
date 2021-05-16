import cv2
import numpy as np

img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")

# To print Image Size
print(img.shape)

# Output Format
# (462, 623, 3) --> they denote (height, width, channels - BGR)

# Resizing the image
imgResize = cv2.resize(img, (200, 200))

# Output Format
# (img, (200, 200)) --> they denote (source, (width, height))

# Displaying the Image
cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.waitKey(0)