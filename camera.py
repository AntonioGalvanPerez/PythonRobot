import time
import cv2 as cv
from ThreadedWebcam import ThreadedWebcam
from UnthreadedWebcam import UnthreadedWebcam

FPS_SMOOTHING = 0.9

minH = 0; minS =  81; minV =  92
maxH = 180; maxS = 255; maxV = 255


fps = 0; prev = 0

# Uncomment below to use the slower webcam
capture = ThreadedWebcam() # UnthreadedWebcam()
capture.start()

params = cv.SimpleBlobDetector_Params()
detector = cv.SimpleBlobDetector_create(params)
fs = cv.FileStorage("params.yaml", cv.FILE_STORAGE_READ)
if not fs.isOpened():
        print("No params")
        exit(1)
detector.read(fs.root())
fs.release()


def updateValues():
    
    minH = 0; minS =  81; minV =  92
    maxH = 180; maxS = 255; maxV = 255


    fps = 0; prev = 0
    now = time.time()
    fps = (fps*FPS_SMOOTHING + (1/(now - prev))*(1.0 - FPS_SMOOTHING))
    prev = now

    frame = capture.read()

    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(frame_hsv, (minH, minS, minV), (maxH, maxS, maxV))

    keypoints = detector.detect(mask)
    frame_with_keypoints = cv.drawKeypoints(frame, keypoints, None, color = (0, 255, 0), flags = cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv.putText(frame_with_keypoints, "FPS: {:.1f}".format(fps), (5, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))
    cv.putText(frame_with_keypoints, "{} blobs".format(len(keypoints)), (5, 35), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

    #cv.imshow("Mask", mask)
    #cv.imshow("Capture", frame_with_keypoints)
    i = 0
    xPosition = 0.0
    size = 0.0
         
    for keypoints in keypoints:
        xPosition = keypoints.pt[0]
        size = keypoints.size
        i+= 1
        time.sleep(.3)
    
    c = cv.waitKey(1)
    
    return (xPosition, size, i)
    #if c == 27 or c == ord('q') or c == ord('Q'): # Esc or Q
     #   capture.stop()
       # exit(0)


#def getXPosition():
 #   global xPosition
  #  updateValues()
   # return xPosition

#def getSize():
   # global size
   # updateValues()
   # return size

#def getCount():
   # global count
    #updateValues()
    #return count
