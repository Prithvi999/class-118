import cv2


img = cv2.imread("boy.jpg")
#to read the file

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#changing the image into gray image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#which is going to help detect the faces; classifies the faces
faces = face_cascade.detectMultiScale(gray)
#scaling the image. finding the different types of gray shades
print(faces)


for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
             
cv2.imshow('img',img)
cv2.waitKey(0)



