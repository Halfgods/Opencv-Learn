import cv2 as cv
Matrix = cv.imread('pictures/4.png')
cv.imshow('3.png' , Matrix)
cv.waitKey(0)

# Another Method
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

Matrix = cv.imread('pictures/cat.jpg',-1)
# print(Matrix, Matrix.shape , Matrix.dtype)
plt.imshow(Matrix)
# cv.imshow('3.png' , Matrix)
# cv.waitKey(0)


# 0 greyscale
# 1 loads color image transparency is neglected
# -1loads image as such including alpha channel