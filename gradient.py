import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Lalacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
SobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
SobelY = cv.Sobel(gray, cv.CV_64F, 0 , 1)
combined_sobel = cv.bitwise_or(SobelX,SobelY)


cv.imshow('SobelX',SobelX)
cv.imshow('SobelY',SobelY)
cv.imshow('Combined',combined_sobel)


cv.waitKey(0)