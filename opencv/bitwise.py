import cv2 as cv
import numpy as np

blank= np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectange',rectangle)
cv.imshow('Circle',circle)

#bitwise
bitwise_and=cv.bitwise_and(rectangle,circle)
bitwise_or=cv.bitwise_or(rectangle,circle)
bitwise_xor=cv.bitwise_xor(rectangle,circle)
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('bitwise and',bitwise_and)
cv.imshow('bitwise or',bitwise_or)
cv.imshow('bitwise xor',bitwise_xor)
cv.imshow('bitwise not',bitwise_not)


cv.waitKey(0)