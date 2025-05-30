import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('park',img)

#translation
def translation(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# x --> right
# y --> down
# -y --> up

translated = translation(img, 100, 100)
cv.imshow('Translated',translated)


#Rotation

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2, height//2)

    rotMat= cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions=(width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45, rotPoint=(0,0))
cv.imshow('Rotated',rotated)    


#Resizing

resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized',resized)

#Flipping

fliped= cv.flip(img, 0)
cv.imshow('Fliped',fliped)

#cropping

cropped  = img[200:400,400:500]
cv.imshow('Cropped',cropped)


cv.waitKey(0)