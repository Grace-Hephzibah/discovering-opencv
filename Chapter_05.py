# Importing the Packages
import cv2
import numpy as np

# Importing the Image
img = cv2.imread("resources/cards.jpg")

# Dealing with cards
# Poker size is 63.5mm X 88.9mm
width, height = 254, 356

# Creating the Points
pts1 = np.float32([ [224,93] , [430, 137] , [164, 378] , [370, 424] ])
pts2 = np.float32([ [0,0], [width, 0] , [0, height], [width, height] ])

# Transformation Matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Displaying the Image
cv2.imshow("Warp Perspective", imgOutput)
cv2.imshow("Original Image", img)
cv2.waitKey(0)