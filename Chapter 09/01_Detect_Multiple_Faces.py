import cv2

# Art images or Graphics images dont work that good
# img = cv2.imread("Multiple_Faces_art.jpg") -> identified only one face

# Real people images work well
img = cv2.imread("Team.webp")

path = "C:/Users/mgrac/Documents/GitHub/OpenCV-Python/resources/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 0), 2)

cv2.imshow("Original Picture", img)

cv2.waitKey(0)