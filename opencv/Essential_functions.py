import cv2 as cv

img=cv.imread('93kbphoto.jpg')
cv.imshow('snow',img)

#grayscale

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('BLur',blur)

#edge cascode
canny=cv.Canny(img,125,175)
cv.imshow('Edges',canny)

#dilating
dilated=cv.dilate(canny,(7,7),iterations=1)
cv.imshow('Dilated',dilated)

#eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resize',resized)

#cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)