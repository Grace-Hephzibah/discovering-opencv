import cv2
import numpy as np

# For creating Black Image
img = np.zeros( (512, 512, 3), np.uint8)


# To color the whole image
img[:] = (255, 0, 0)

# To create line
cv2.line(img, (0,0), (300,300), (0,255,0), 3)

# img -> the sourece
# (0,0) -> Starting Point
# (300, 300) -> Ending Point
# (0, 255, 0) -> Colour
# 3 -> Thickness

cv2.imshow("Output Window", img)
cv2.waitKey(0)