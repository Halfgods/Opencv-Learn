<<<<<<< HEAD
import cv2 as cv
import numpy as np
Matrix = cv.imread('pictures/3.png')
"""Translation"""
# resized = cv.resize(Matrix,(500,500))
# def Translate(img,x,y):
#     TransMat = np.float32([[1,0,x],[0,1,y]])
#     dimension = (img.shape[0] , img.shape[1])
#     return cv.warpAffine(img, TransMat , dimension)
# trans = Translate(Matrix , -50,90)

"""Rotation"""
# def rotation(img,angle,RotPoint = None):
#     (height , width) = Matrix.shape[:2]
    
#     if RotPoint == None:
#         RotPoint = (width//2 , height//2 )
#     RotMat = cv.getRotationMatrix2D(RotPoint, angle , 1)
#     dimensions = (width , height)
#     return cv.warpAffine(img , RotMat , dimensions)    
# rotationpic = rotation(Matrix , -45)
# rotation2 = rotation(rotationpic , -45)

"""Resizing"""
# resized = cv.resize(Matrix , (400,400) , interpolation=cv.INTER_CUBIC)

'''Flipping'''
# flip = cv.flip(Matrix,-1)

'''Cropping'''
crop = Matrix[200:400,300:400]

cv.imshow('Test' , crop)
=======
import cv2 as cv
import numpy as np
Matrix = cv.imread('pictures/3.png')
"""Translation"""
# resized = cv.resize(Matrix,(500,500))
# def Translate(img,x,y):
#     TransMat = np.float32([[1,0,x],[0,1,y]])
#     dimension = (img.shape[0] , img.shape[1])
#     return cv.warpAffine(img, TransMat , dimension)
# trans = Translate(Matrix , -50,90)

"""Rotation"""
# def rotation(img,angle,RotPoint = None):
#     (height , width) = Matrix.shape[:2]
    
#     if RotPoint == None:
#         RotPoint = (width//2 , height//2 )
#     RotMat = cv.getRotationMatrix2D(RotPoint, angle , 1)
#     dimensions = (width , height)
#     return cv.warpAffine(img , RotMat , dimensions)    
# rotationpic = rotation(Matrix , -45)
# rotation2 = rotation(rotationpic , -45)

"""Resizing"""
# resized = cv.resize(Matrix , (400,400) , interpolation=cv.INTER_CUBIC)

'''Flipping'''
# flip = cv.flip(Matrix,-1)

'''Cropping'''
crop = Matrix[200:400,300:400]

cv.imshow('Test' , crop)
>>>>>>> 4e12cabbdd49b83263e1e42630ef03e2abd0bc1f
cv.waitKey(0)