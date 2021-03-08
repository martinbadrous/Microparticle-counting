#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:41:46 2021

@author: mscv
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:56:42 2021

@author: yousefbm
"""
from pyimagesearch.centroidtracker import CentroidTracker

import cv2
i =1
max = 0
ct = CentroidTracker()
coco_counter=0
final = 0
import numpy as np
cap = cv2.VideoCapture('Live 8585-38.mp4')
out = cv2.VideoWriter('Live 8585-HOUGH.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1280,720))

ret, frame = cap.read()
fgbg = cv2.createBackgroundSubtractorKNN()
max2=0
check = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    coco_counter = coco_counter +1
    rects = []
    fgmask = fgbg.apply(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #img_gray = cv2.GaussianBlur(gray, (7, 7), 0)
    #med = cv2.medianBlur(fgmask, 9)
    ret,thresh1 = cv2.threshold(fgmask,30,255,cv2.THRESH_BINARY)
    thresh2 = cv2.medianBlur(thresh1, 27)
    kernel = np.ones((7,7),np.uint8)
    thresh3 = cv2.dilate(thresh2,kernel,iterations = 3)
    thresh4 = cv2.morphologyEx(thresh3, cv2.MORPH_OPEN, kernel)
    #crop the frame for ROI
    #roi = med[130:500, 100:1200]
    thresh5 = cv2.blur(thresh4, (5,5))
    thresh5 = thresh5[200:500, 200:1100]
    gray = gray[200:500, 200:1100]
    im_thresh_gray = cv2.bitwise_or(gray, thresh5)
    circles = cv2.HoughCircles(im_thresh_gray,cv2.HOUGH_GRADIENT,1,40,
                               param1=60,param2=5,minRadius=15,maxRadius=20)
    

    
    if circles is not None and coco_counter>10 :
        
        circola = np.uint16(np.around(circles))
        max1= len(circola[0,:])
        if max1 != max2:
            print(max1)
            final = max1 + final
        
            for i in circola[0,:]:
                
                box = (i[0]-i[2],i[1]-i[2],i[0]-i[2]+2*i[2],i[1]-i[2]+2*i[2])
                
                rects.append(box)
            
                cv2.circle(frame,(i[0]+200,i[1]+200),i[2],(0,255,0),2)
    # draw the center of the circle
                cv2.circle(frame,(i[0]+200,i[1]+200),2,(0,0,255),3)
                max2=max1
            
        
            
            
        
        
    
    objects = ct.update(rects)
    for (objectID, centroid) in objects.items():
        
        # draw both the ID of the object and the centroid of the
        # object on the output frame
        text = "ID {}".format(objectID)
        cv2.putText(frame, text, (centroid[0] + 200, centroid[1] + 200),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        #cv2.circle(frame, (int(x-w/2), int(y-h/2)), 4, (0, 255, 0), -1)
        # direction = centroid[1]-640
        # if centroid[0] < H // 2:
        #     coco=coco+1
        if max < objectID:
            max = objectID
        else :continue
        #cv2.imwrite('kang'+str(i)+'.jpg',frame)
        i+=1 
    text = "Particle Count: {}".format(max)
    cv2.putText(frame, text, (600, 100 ),
            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #check =check+1
    
    cv2.imshow('frame',frame)
    
    out.write(frame)
    #cv2.imwrite('kang'+str(i)+'.jpg',im_thresh_gray)
    i=1+i
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
            
        
    # draw the outer circle
            
        
        
        
    
out.release()
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()