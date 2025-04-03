import cv2 as cv
import numpy as np

img=cv.imread('photo.jpg')
cv.imshow('squirrel',img)

blank= np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])



cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

merged=cv.merge([b,g,r])
cv.imshow('merged',merged)

cv.waitKey(0)