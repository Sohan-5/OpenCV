import cv2 as cv
import numpy as np

img=cv.imread('cbd.jpg')
#img=cv.resize(img,(0,0),fx=0.5,fy=0.5)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners=cv.goodFeaturesToTrack(gray,100,0.01,10)
corners=np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv.circle(img,(x,y),5,(255,0,0),-1)
    

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
            c1=tuple(corners[i][0])
            c2=tuple(corners[j][0])
            color=tuple(map(lambda x :int(x),np.random.randint(0,255,size=3)))
            cv.line(img,c1,c2,color,1)

cv.imshow('Circled',img)
cv.waitKey(0)
cv.destroyAllWindows()    
    