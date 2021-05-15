import cv2

img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# COLOR_BGR2GRAY =
# (COLOR_ -> Color change to) + (BGR -> RGB is written like this in py) + (2 -> to) + (GRAY -> gray scale)

cv2.imshow("Original Picture", img)
cv2.imshow("Gray Scale Picture", imgGray)

cv2.waitKey(0)