import cv2
import numpy as np

# Dialating a Eroded Image == Original Image ? --> Result : Not Working as thought

img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")
kernel = np.ones( (5,5), np.uint8)

imgEroded = cv2.erode(img, kernel, iterations = 1)
imgDialation = cv2.dilate(imgEroded, kernel, iterations = 1)

cv2.imshow("Dialation Picture", imgDialation)
cv2.imshow("Eroded Picture", imgEroded)

cv2.waitKey(0)