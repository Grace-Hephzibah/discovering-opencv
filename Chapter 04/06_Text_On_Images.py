import cv2
import numpy as np

img = np.zeros( (512, 512, 3), np.uint8)
img[:] = (255, 0, 0)

# Text on images
cv2.putText(img, "OPENCV", (300,100), cv2.FONT_ITALIC, 1, (0,150,0), 1)
# img -> the sourece
# "OPENCV" -> Text
# (300, 100) -> Origin of Text
# cv2.FONT_... -> Font [... -> means that the IDE will show the fonts available in OPENCV]
# 1 -> Scale
# (0, 150, 0) -> Colour
# 1 -> Thickness

cv2.imshow("Output Window", img)
cv2.waitKey(0)