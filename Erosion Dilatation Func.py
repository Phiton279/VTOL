from __future__ import print_function
import cv2
import numpy as np
import argparse
import imutils

def nothing(x):
    pass

def erosion(frame,elem,kern):
    erosion_type = 0
    if elem == 0:
        erosion_type = cv2.MORPH_RECT
    elif elem == 1:
        erosion_type = cv2.MORPH_CROSS
    elif elem == 2:
        erosion_type = cv2.MORPH_ELLIPSE
    element = cv2.getStructuringElement(erosion_type,(2*kern+1,2*kern+1),(kern,kern))
    res = cv2.erode(frame,element)

    return res

def dilatation(frame,elem,kern):
    dialtation_type = 0
    if elem == 0:
        dilatation_type = cv2.MORPH_RECT
    elif elem == 1:
        dilatation_type = cv2.MORPH_CROSS
    elif elem == 2:
        dilatation_type = cv2.MORPH_ELLIPSE
    element = cv2.getStructuringElement(dilatation_type,(2*kern+1,2*kern+1),(kern,kern))
    res = cv2.dilate(frame,element)

    return res

cap = cv2.VideoCapture(0)
cv2.namedWindow('Frame')
cv2.createTrackbar('Element','Frame',0,2,nothing)
cv2.createTrackbar('Kernel','Frame',0,21,nothing)

while(cap.isOpened):
    _,frame = cap.read()

    elem = cv2.getTrackbarPos('Element','Frame')
    kern = cv2.getTrackbarPos('Kernel','Frame')
    
    frame = erosion(frame,elem,kern)
    frame = dilatation(frame,elem,kern)
    frame = dilatation(frame,elem,kern)
    frame = erosion(frame,elem,kern)
    #frame = imutils.resize(frame, width=600)
    cv2.imshow('Frame',frame)

    k = cv2.waitKey(5) & 0xFF 
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
