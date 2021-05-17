import cv2
import numpy as np

# For creating Black Image
img = np.zeros( (512, 512) )

cv2.imshow("Output Window", img)
cv2.waitKey(0)