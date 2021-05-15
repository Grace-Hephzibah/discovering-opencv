import cv2

img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")

imgBlur = cv2.GaussianBlur(img, (7,7), 0)
# (7,7) -> is called kernel
# Must contain only odd numbers
# It is matrix

cv2.imshow("Blur Picture", imgBlur)

cv2.waitKey(0)