import cv2
import numpy as np
import My_OpenCV_Functions as cv

def empty(a):
    pass

# Creating a Window with Trackbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# Continously running a loop to see changes in real time
while True:
    # Stroing the Image in te variable and creating a HSV Image
    img = cv2.imread("resources/flower.jpg")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # Taking the Min and Max values of the TrackBars in real time
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # Printing the value for reference
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    # Creating a Mask Image
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    # Creating a Stack Image for Easy Reference
    imgStack = cv.stackImages(0.08,([img,imgHSV],[mask,imgResult]))
    cv2.imshow("Stacked Images", imgStack)
    cv2.waitKey(1)