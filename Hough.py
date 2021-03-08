#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:56:42 2021

@author: yousefbm
"""
from pyimagesearch.centroidtracker import CentroidTracker

from fofo import fofo
import cv2
i =1
max = 0
final = 0
import numpy as np
cap = cv2.VideoCapture('Live 8665-4.mp4')
out = cv2.VideoWriter('Live 8665-HOUGH2.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1280,720))

ret, frame = cap.read()
fgbg = cv2.createBackgroundSubtractorKNN()
max2=0
check = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #img_gray = cv2.GaussianBlur(gray, (7, 7), 0)
    #med = cv2.medianBlur(fgmask, 9)
    ret,thresh1 = cv2.threshold(fgmask,30,255,cv2.THRESH_BINARY)
    thresh2 = cv2.medianBlur(thresh1, 15)
    kernel = np.ones((5,5),np.uint8)
    thresh3 = cv2.dilate(thresh2,kernel,iterations = 2)
    thresh4 = cv2.morphologyEx(thresh3, cv2.MORPH_CLOSE, kernel)
    #crop the frame for ROI
    #roi = med[130:500, 100:1200]
    thresh5 = cv2.medianBlur(thresh4, 3)
    thresh5 = thresh5[200:500, 200:1100]
    gray = gray[200:500, 200:1100]
    im_thresh_gray = cv2.bitwise_or(gray, thresh5)
    circles = cv2.HoughCircles(im_thresh_gray,cv2.HOUGH_GRADIENT,1,10,
                               param1=50,param2=11,minRadius=1,maxRadius=30)
    

    
    if circles is not None :
        
        circola = np.uint16(np.around(circles))
        max1= len(circola[0,:])
        if max1 != max2:
            print(max1)
            final = max1 + final
        
            for i in circola[0,:]:
            
                cv2.circle(frame,(i[0]+200,i[1]+200),i[2],(0,255,0),2)
    # draw the center of the circle
                cv2.circle(frame,(i[0]+200,i[1]+200),2,(0,0,255),3)
                max2=max1
            
        
            
            
        
        
    

    # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #check =check+1
    text = "Particle Count {}".format(final)
    cv2.putText(frame, text, (600, 100 ),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    cv2.imshow('frame',frame)
    out.write(frame)
    #cv2.imwrite('kang'+str(i)+'.jpg',frame)
    i+=1
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
            
        
    # draw the outer circle
            
        
        
        
    
out.release()
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()