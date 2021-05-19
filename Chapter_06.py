import cv2
import numpy as np
import My_OpenCV_Functions as cv

img = cv2.imread("resources/girl.jpg")

# Horizontal Stacking of Images
imgHor = np.hstack((img, img))

# Vertical Stacking of Images
imgVer = np.vstack((img, img))

# Stack the images through self built function
imgStack = cv.stackImages(0.5, ([img,img,img],[img,img,img]))

# Displaying the images
cv2.imshow("Horizontal Stack", imgHor)
cv2.imshow("Vertical Stack", imgVer)
cv2.imshow("Full Stack", imgStack)
cv2.waitKey(0)