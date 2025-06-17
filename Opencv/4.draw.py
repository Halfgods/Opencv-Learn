<<<<<<< HEAD
import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype = 'uint8')
# blank[200:250 , 200:250] = 0,0,255
# blank[:] = 255,0,0
cv.rectangle(blank,(blank.shape[0]//2 , blank.shape[1]//2) , (400,400),(255,0,0), thickness=-1)
cv.circle(blank,(255,255) , 40 , (0,255,0) , thickness=-1)
cv.line(blank,(0,0),(blank.shape[0]//2 , blank.shape[1]//2) , (0,0,255),thickness=3)
cv.putText(blank,'Hello' , (250,250) , cv.FONT_HERSHEY_TRIPLEX, 2 , (255,255,255) , thickness=1)
cv.imshow("test", blank)
=======
import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype = 'uint8')
# blank[200:250 , 200:250] = 0,0,255
# blank[:] = 255,0,0
cv.rectangle(blank,(blank.shape[0]//2 , blank.shape[1]//2) , (400,400),(255,0,0), thickness=-1)
cv.circle(blank,(255,255) , 40 , (0,255,0) , thickness=-1)
cv.line(blank,(0,0),(blank.shape[0]//2 , blank.shape[1]//2) , (0,0,255),thickness=3)
cv.putText(blank,'Hello' , (250,250) , cv.FONT_HERSHEY_TRIPLEX, 2 , (255,255,255) , thickness=1)
cv.imshow("test", blank)
>>>>>>> 4e12cabbdd49b83263e1e42630ef03e2abd0bc1f
cv.waitKey(0)