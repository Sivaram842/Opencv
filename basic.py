import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('CatImage',img)

# Converting to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#Blur

blur= cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade

canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)

#Dilating a Image

dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated',dilated)

#Eroding

eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

#Resize

resized = cv.resize(img, (500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)


#Cropping

cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)