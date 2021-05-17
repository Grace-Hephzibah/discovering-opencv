import cv2
import numpy as np

img = np.zeros( (512, 512, 3), np.uint8)
img[:] = (100, 100, 100)

# To draw a circle
cv2.circle(img, (400,50), 30, (255, 255, 0), 5)
# img -> the sourece
# (400,50) -> Center Point
# 30 -> Radius
# (0, 255, 0) -> Colour
# 3 -> Thickness

cv2.imshow("Output Window", img)
cv2.waitKey(0)