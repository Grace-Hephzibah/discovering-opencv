import cv2
import numpy as np

# Erosion is the opposite of Dialation

img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")
kernel = np.ones( (5,5), np.uint8)
# unit8 = Unsigned + INTeger + 8bit

imgEroded = cv2.erode(img, kernel, iterations = 1)
# Higher iteration = Thicker Pen

cv2.imshow("Eroded Picture", imgEroded)

cv2.waitKey(0)