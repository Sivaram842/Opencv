import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8' )
cv.imshow('Blank',blank)

# .. point the image a certain color
# blank[:] = 0,255,0
# cv.imshow("Green",blank)


# .. Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow("Rectangle",blank)


#.. Draw a Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow("Circle",blank)


# .. Draw a line
cv.line(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow("Line",blank)


# write text
cv.putText(blank,'Hello',(250,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255),thickness=4)
cv.imshow('Text',blank)

cv.waitKey(0)