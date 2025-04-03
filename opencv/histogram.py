import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('photo.jpg')
cv.imshow('squirrel',img)


blank=np.zeros(img.shape[:2],dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,255,-1)
cv.imshow('Mask',mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image',masked)

cv.waitKey(0)