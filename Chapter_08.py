import cv2
import numpy as np
import My_OpenCV_Functions as cv

path = 'resources/shapes.png'
img = cv2.imread(path)

cv.getContours(img, 1)