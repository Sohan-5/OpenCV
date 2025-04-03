import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()
    
    img=np.zeros(frame.shape,np.uint8)
    width=int(cap.get(3))
    height=int(cap.get(4))
    
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_red=np.array([90,50,50])
    upper_red=np.array([130,255,255])
    
    mask=cv.inRange(hsv,lower_red,upper_red)
    result=cv.bitwise_and(frame,frame,mask=mask)
    
    
    cv.imshow('frame',result)
    cv.imshow('mask',mask)
    
    if cv.waitKey(1)==ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()    

#COLOR CONVERTER

# >>> green = np.uint8([[[0,255,0 ]]])
# >>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# >>> print hsv_green
# BGR_color=np.uint8([[[0,128,0]]])
# hsv=cv.cvtColor(BGR_color,cv.COLOR_BGR2HSV)
# print(hsv)

# hsv=np.uint8([[[130,25,255]]])
# bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
# print(bgr)


# RGB_color=np.uint8([[[0,128,0]]])
# BGR_color=cv.cvtColor(RGB_color,cv.COLOR_RGB2BGR)
# print(RGB_color)

# #BLUE
# ray([90,50,50])
# ray([130,255,255])