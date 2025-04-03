import cv2 as cv

img=cv.imread('photo.jpg')
cv.imshow('squirrel',img)

#averaging
average=cv.blur(img,(5,5))
cv.imshow('Average',average)

gauss=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('BLur',gauss)

median=cv.medianBlur(img,7)
cv.imshow('Median',median)

bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)