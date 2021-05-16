import cv2

# Original Image
# img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/girl.jpg")

# Black and White Image
img = cv2.imread("C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/lion.jpg")

# imgFun = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) -> B to R and vice versa
# imgFun = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) -> Thermal color
# imgFun = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) -> Full Sunlight Blur view
# imgFun = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ) -> Made all the colors dull

# Black and white Image to Color. Possible? - Not yet
imgFun = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

cv2.imshow("Original Picture", img)
cv2.imshow("Playing Picture", imgFun)
# Not working

cv2.waitKey(0)''