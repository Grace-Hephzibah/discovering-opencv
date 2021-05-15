import cv2
import numpy as np

img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")
kernel = np.ones( (5,5), np.uint8)
# unit8 = Unsigned + INTeger + 8bit

imgDialation = cv2.dilate(img, kernel, iterations = 1)
# Higher iteration = Thicker Pen

cv2.imshow("Dialation Picture", imgDialation)

cv2.waitKey(0)