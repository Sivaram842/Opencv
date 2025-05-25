import cv2 as cv
 
image = cv.imread('Photos/cat.jpg') 
cv.imshow('Cat',image)

def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(image)
cv.imshow('Cat Image',resized_image)
#Reading videos

def changeResolution(width, height):
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame=capture.read()

    frame_resized= rescaleFrame(frame, scale=0.2)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break 

capture.release()
cv.destroyAllWindows()