import cv2

img = cv2.imread("resources/girl.jpg")

faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 0), 2)

cv2.imshow("Original Picture", img)

cv2.waitKey(0)