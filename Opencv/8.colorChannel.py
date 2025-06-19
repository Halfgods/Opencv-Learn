import cv2 as cv
import numpy as np 

img = cv.imread('pictures/bgr.png')
img = cv.resize(img, (400, 400))  # Resize the image to 600x400 pixels
blank = np.zeros(img.shape[:2], dtype='uint8' )  # Create a blank image with the same shape as img
b,g,r = cv.split(img)
blue = cv.merge([b, blank, blank])  # Merge blue channel with blank green and red channels
green = cv.merge([blank, g, blank])  # Merge green channel with blank blue
red = cv.merge([blank, blank, r])  # Merge red channel with blank blue and green channels
final = cv.merge([b, g, r])  # Merge all channels back together
# cv.imshow('Blue' , blank)
# cv.imshow('Blue' , blue)
# cv.imshow('green' , green)
# cv.imshow('red' , red)
cv.imshow('Original Image', final)
print("Pixel value at (100,100):", img[100,100])  # Prints [B,G,R]
print("Blue channel value:", b[100,100])
print("Green channel value:", g[100,100])
print("Red channel value:", r[100,100])
cv.waitKey(0)