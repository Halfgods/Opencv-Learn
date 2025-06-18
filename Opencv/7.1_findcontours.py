import cv2 as cv
"""1: Preprocessing"""
# real  = cv.imread('pictures/abc.jpg')
# gray = cv.cvtColor(real , cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray , (7,7) , 0)
# ret , thresh  = cv.threshold(blur , 127 , 255  , cv.THRESH_BINARY)
# retw , tresh = cv.threshold(blur , 0 , 255 , cv.THRESH_BINARY + cv.THRESH_OTSU)
# cv.imshow("Window" , thresh)
# cv.waitKey(0)

"""diff ways of Thresholding"""
# 1. adaptive thresholding (one of best)
# thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY , 11 , 2 )
# cv.imshow("Window" , thresh)
# cv.waitKey(0)

# 2. Otsu's Thresholding  (Not Effective)
# ret , tresh = cv.threshold(blur , 0 , 255 , cv.THRESH_BINARY + cv.THRESH_OTSU)
# cv.imshow("Window" , tresh)
# cv.waitKey(0)

#  3.Histogram Equalization
# equalized = cv.equalizeHist(blur)
# ret , thresh = cv.threshold(equalized , 127 , 255 , cv.THRESH_BINARY)
# cv.imshow('test' , thresh)
# cv.waitKey(0)

# 4.Morphological Ops (Use for fixing broken edges)
# kernel = cv.getStructuringElement(cv.MORPH_RECT , (3,3))
# thresh_dilated = cv.dilate(thresh , kernel , iterations=1 )
# cv.imshow('test' , thresh_dilated)
# cv.waitKey(0)

"""2. Find Contours"""
# real  = cv.imread('pictures/abc.jpg')
# gray = cv.cvtColor(real , cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray , (7,7) , 0)
# thresh = cv.adaptiveThreshold(blur , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY , 11 , 2)
# contours, hierachy = cv.findContours(thresh , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
# print(len(contours))
# cv.imshow("Window" , thresh)
# cv.waitKey(0)

"""Note this imp thing incase all objects are black and background are white then we will have to use inversion"""
# thresh = cv.bitwise_not(thresh) # use those only when needed
