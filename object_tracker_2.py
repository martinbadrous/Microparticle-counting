# USAGE
# python object_tracker.py --prototxt deploy.prototxt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
from pyimagesearch.centroidtracker import CentroidTracker
#from imutils.video import VideoStream
import numpy as np
import argparse
#import imutils
import time
import cv2
#from r.trackableobject import TrackableObject
#from pyimagesearch import TrackableObject
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
# ap.add_argument("-p", "--prototxt", required=True,
#     help="path to Caffe 'deploy' prototxt file")
# ap.add_argument("-m", "--model", required=True,
#     help="path to Caffe pre-trained model")
i=1
ap.add_argument("-c", "--confidence", type=float, default=0.5,
    help="minimum probability to filter weak detections")
args = vars(ap.parse_args())
proto ="/home/mscv/simple-object-tracking/deploy.prototxt"
model ="/home/mscv/simple-object-tracking/res10_300x300_ssd_iter_140000.caffemodel"
# initialize our centroid tracker and frame dimensions
ct = CentroidTracker()
(H, W) = (None, None)
totalDown = 0
totalUp = 0
# load our serialized model from disk
print("[INFO] loading model...")
#net = cv2.dnn.readNetFromCaffe(proto, model)
coco=0
# initialize the video stream and allow the camera sensor to warmup
print("[INFO] starting video stream...")
vs = cv2.VideoCapture('Live 8585-38.mp4')
out = cv2.VideoWriter('Live 8585-Contour.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1280,720))

max=0
time.sleep(2.0)
dsize = (640, 360)
ret, frame = vs.read()
fgbg = cv2.createBackgroundSubtractorKNN()
# loop over the frames from the video stream
while True:
    # read the next frame from the video stream and resize it
    ret, frame = vs.read()
    #frame = np.asarray(frame)
    
    #frame = cv2.resize(frame, dsize)
    rects = []
    fgmask = fgbg.apply(frame)
    fgmask = cv2.equalizeHist(fgmask)
    ret,thresh1 = cv2.threshold(fgmask,1,255,cv2.THRESH_BINARY)
    median = cv2.medianBlur(thresh1,7)
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(median,kernel,iterations = 1)
    opening = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
    blur = cv2.GaussianBlur(opening,(5,5),0)
    blur1 = cv2.blur(blur,(5,5))
    #im_bw = cv2.cvtColor(blur1, cv2.COLOR_RGB2GRAY)
    #ret,thresh1 = cv2.threshold(blur1,1,255,cv2.THRESH_BINARY)
    #gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(blur1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    idx =0 

    # loop over the detections
    for cnt in contours:
        
        box = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        if area<500:
            break
        x,y,w,h = cv2.boundingRect(cnt)
        box = (x,y,x+h,y+w)
        rects.append(box)#.astype("int"))
        box = (x,y,h,w)

            # draw a bounding box surrounding the object so we can
            # visualize it
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(200,0,0),2)    
        (startX, startY, endX, endY) = box
        cv2.rectangle(frame, box,(255, 0, 0), 2)
        
        
        

    # if the frame dimensions are None, grab them
    if W is None or H is None:
        (H, W) = frame.shape[:2]
    
    

    # construct a blob from the frame, pass it through the network,
    # obtain our output predictions, and initialize the list of
    # bounding box rectangles
#     blob = cv2.dnn.blobFromImage(frame, 1.0, (W, H),
#         (104.0, 177.0, 123.0))
#     net.setInput(blob)
#     detections = net.forward()
    
        # filter out weak detections by ensuring the predicted
        # probability is greater than a minimum threshold
        
            # compute the (x, y)-coordinates of the bounding box for
            # the object, then update the bounding box rectangles list
            

    # update our centroid tracker using the computed set of bounding
    # box rectangles
    objects = ct.update(rects)
    cv2.line(frame, (W//2, 0), (W//2, H), (0, 255, 255), 2)
    # loop over the tracked objects
    for (objectID, centroid) in objects.items():
        # draw both the ID of the object and the centroid of the
        # object on the output frame
        text = "ID {}".format(objectID)
        cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.circle(frame, (int(x-w/2), int(y-h/2)), 4, (0, 255, 0), -1)
        # direction = centroid[1]-640
        # if centroid[0] < H // 2:
        #     coco=coco+1
        if max < objectID:
            max = objectID
        else :continue
        #cv2.imwrite('kang'+str(i)+'.jpg',frame)
        i+=1 
    text = "Particle Count {}".format(max)
    cv2.putText(frame, text, (600, 100 ),
            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        
    
            
            
    
    
    out.write(frame)

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
vs.release()
out.release()

# do a bit of cleanup
cv2.destroyAllWindows()
