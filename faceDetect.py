import cv2 as cv


img = cv.imread('Photos/lady.jpg')
cv.imshow('Lady',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Lady',gray)


haar_Cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_Cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3)
print(f'Number of faces found = {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+h),(0,255,0),thickness=3)


cv.imshow('face detection',img)


cv.waitKey(0)