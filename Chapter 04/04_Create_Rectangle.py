import cv2
import numpy as np

# For creating Black Image
img = np.zeros( (512, 512, 3), np.uint8)


# To color the whole image
img[:] = (0, 255, 0)

# To draw the rectangle
cv2.rectangle(img, (0,0), (250,350), (0,0,255), 2)
# img -> the sourece
# (0,0) -> Starting Point
# (300, 300) -> Ending Point
# (0, 255, 0) -> Colour
# 3 -> Thickness

# cv2.FILLED -> Colours the whole region
# |--> Must be used at the Thickness Parameter

cv2.imshow("Output Window", img)
cv2.waitKey(0)