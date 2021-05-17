import cv2
import numpy as np

# For creating channel
img = np.zeros( (512, 512, 3), np.uint8 )

# To colour the image
img[:]  = 255, 0, 0 # BGR Format
# It can also be given as
# img[200:300, 200:500] -> img[height range : width range]

cv2.imshow("Output Window", img)
cv2.waitKey(0)