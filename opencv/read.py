import cv2 as cv

#reading images

img=cv.imread('93kbphoto.jpg')

cv.imshow('93kbphoto',img)



#rescale & resize

""" def changeRes(width,height):
#live video
    capture.set(3,width)
    capture.set(4,height)
 """
def rescaleFrame(frame,scale=0.75):
    #images,videos,livevids
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)

cv.waitKey(0)

#reading video

#capture = cv.ViddeoCapture('')

#while True:
#    isTrue,frame= capture.read()

 #   frame_resize=rescaleFrame(frame)

 #   cv.imshow('',frame)
  #  cv.imshow('',frame_resize)

  #  if cv.waitkey(20) & 0xff==ord('d'):
   #     break

#capture.release()
#cv.destroyAlWindows()  