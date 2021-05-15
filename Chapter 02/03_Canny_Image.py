import cv2
# Canny -> Edge Detector

img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")

imgCanny = cv2.Canny(img, 100, 100)
# higher the value - lower the edges
# Try the below
# imgCannyNew = cv2.Canny(img, 150, 200)

cv2.imshow("Canny Picture", imgCanny)
# cv2.imshow("Canny (Less) Picture", imgCannyNew)

cv2.waitKey(0)