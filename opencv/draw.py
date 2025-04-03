import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3),dtype='uint8')
""" img=cv.imread('93kbphoto.jpg')
cv.imshow('snow',img) """
cv.imshow('Blank',blank)

#Paint
blank[200:300,300:400]=0,255,0
cv.imshow('Green',blank)

#Draw rectangle
cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED) 
cv.imshow('Rectangle',blank)

#circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
cv.imshow('Circle',blank)

#line
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow('Line',blank)

#write text
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)