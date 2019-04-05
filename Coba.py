import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

while (cap.isOpened):
    
    ret,frame = cap.read()

    blurred = cv2.GaussianBlur(frame,(15,15),0)
    hsv = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

    lower = np.array([160,0,0])
    upper = np.array([180,255,255])

    kernelO = np.ones((10,10))
    kernelC = np.ones((20,20))

    mask = cv2.inRange(hsv,lower,upper)
    mask = cv2.erode(mask,kernelO, iterations=1)
    mask = cv2.dilate(mask,kernelO, iterations=1)
    mask = cv2.dilate(mask,kernelO, iterations=1)
    mask = cv2.erode(mask,kernelO, iterations=1)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelO)
    mask2 = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernelC)
    
    res = cv2.bitwise_and(frame, frame, mask = mask)
    res = cv2.medianBlur(res, 5)
    
    cv2.imshow('Frame',frame)
    cv2.imshow('HSV',hsv)
    cv2.imshow('MASK',mask)
    cv2.imshow('MASK2',mask2)
    cv2.imshow('RES',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27 :
        break

cv2.destroyAllWindows()
cap.release()
