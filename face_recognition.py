import numpy as np
import cv2 as cv

haar_Cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ramprasad', 'Sivaram', 'Supriya']
# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\LENOVO\OneDrive\Desktop\faces_train\Sivaram\IMG-20250530-WA0023.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray Prasad', gray)

#detect the face in the image
faces_rect = haar_Cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]


    label , confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with confidence : {confidence}')

    cv.putText(img, str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,255),thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h),(0,255,255),thickness=2)


cv.imshow('Detected Face',img)

cv.waitKey(0)


