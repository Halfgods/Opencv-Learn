
import cv2 as cv
capture = cv.VideoCapture(0)  
'''WebCam'''
while True:
    isTrue , frame = capture.read()
    flip = cv.flip(frame,1)
    cv.imshow("Video" , flip)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    
capture.release()

import cv2 as cv
capture = cv.VideoCapture('videos/video1.mp4')  
'''WebCam'''
while True:
    isTrue , frame = capture.read()
    flip = cv.flip(frame,1)
    cv.imshow("Video" , flip)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    
capture.release()

cv.destroyAllWindows()