import cv2 as cv
import numpy as np

img=cv.imread('photo.jpg')
cv.imshow('squirrel',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#Laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

cv.imshow('Soblex',sobelx)
cv.imshow('Sobley',sobely)
cv.imshow('Soble combined',combined_sobel)

canny=cv.Canny(img,150,175)
cv.imshow('Edges',canny)


cv.waitKey(0)