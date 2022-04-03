import cv2

path='Aditya 2.0.jpeg'

facecascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread(path)
imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces=facecascade.detectMultiScale(imgGray,1.1,5)
# print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)

cv2.imshow('Face Detection', img)

cv2.waitKey(0)