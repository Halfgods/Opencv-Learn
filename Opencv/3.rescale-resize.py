import cv2 as cv
# For images
frame = cv.imread('pictures/cat.jpg')
def rescaleFrame(frame , scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] *scale)
    dimension = (width,height)
    
    return cv.resize(frame,dimension , interpolation=cv.INTER_AREA)
cv.imshow("Image" , frame)
cv.waitKey(0)



# For Videos
def rescaleFrame(frame , scale = 0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] *scale)
    dimension = (width,height)
    
    return cv.resize(frame,dimension , interpolation= cv.INTER_AREA)

capture =cv.VideoCapture('videos/video2.mp4')  # for webcam put 0
try :
    while True:
        isTrue , frame = capture.read()   #reads frame by frame 
        frame_resized = rescaleFrame(frame)
        cv.imshow('Video', frame)
        cv.imshow('Video', frame_resized)
        
        if cv.waitKey(20) & 0xFF ==ord('q'):    # ord wala key press kro and u can quit the window
            break
except Exception as e:
    print("uh oh",e)
capture.release()
cv.destroyAllWindows()


"""capture.set method (for videos only)"""
capture =cv.VideoCapture(0)  # for webcam put 0

def ChangeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
    
try :
    while True:
        isTrue , frame = capture.read()   #reads frame by frame 
        ChangeRes(3,3)
        cv.imshow('Video', frame)
        
        if cv.waitKey(20) & 0xFF ==ord('q'):    # ord wala key press kro and u can quit the window
            break
except Exception as e:
    print("uh oh",e)
capture.release()
cv.destroyAllWindows()


import cv2 as cv
# For images
frame = cv.imread('pictures/cat.jpg')
def rescaleFrame(frame , scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] *scale)
    dimension = (width,height)
    
    return cv.resize(frame,dimension , interpolation=cv.INTER_AREA)
cv.imshow("Image" , frame)
cv.waitKey(0)



# For Videos
def rescaleFrame(frame , scale = 0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] *scale)
    dimension = (width,height)
    
    return cv.resize(frame,dimension , interpolation= cv.INTER_AREA)

capture =cv.VideoCapture('videos/video2.mp4')  # for webcam put 0
try :
    while True:
        isTrue , frame = capture.read()   #reads frame by frame 
        frame_resized = rescaleFrame(frame)
        cv.imshow('Video', frame)
        cv.imshow('Video', frame_resized)
        
        if cv.waitKey(20) & 0xFF ==ord('q'):    # ord wala key press kro and u can quit the window
            break
except Exception as e:
    print("uh oh",e)
capture.release()
cv.destroyAllWindows()


"""capture.set method (for videos only)"""
capture =cv.VideoCapture(0)  # for webcam put 0

def ChangeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
    
try :
    while True:
        isTrue , frame = capture.read()   #reads frame by frame 
        ChangeRes(3,3)
        cv.imshow('Video', frame)
        
        if cv.waitKey(20) & 0xFF ==ord('q'):    # ord wala key press kro and u can quit the window
            break
except Exception as e:
    print("uh oh",e)
capture.release()
cv.destroyAllWindows()


