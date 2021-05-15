import cv2
# import numpy as np

img = cv2.imread("resources/girl.jpg")
# kernel = np.ones( (5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
'''imgBlur = cv2.GaussianBlur(img, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(img, kernel, iterations = 1)
imgEroded = cv2.erode(img, kernel, iterations = 1)
'''
# cv2.imshow("Original Picture", img)
cv2.imshow("Gray Scale Picture", imgGray)
# cv2.imshow("Blur Picture", imgBlur)
# cv2.imshow("Canny Picture", imgCanny)
# cv2.imshow("Dialation Picture", imgDialation)
# cv2.imshow("Eroded Picture", imgEroded)

cv2.waitKey(0)