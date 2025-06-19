import cv2 as cv

img = cv.imread('pictures/red_apple.jpg')
img = cv.resize(img, (400, 400))  # Resize the image to 600x400 pixels
'''Average Blur'''
blur = cv.blur(img , (3,3))
# blur2 = cv.blur(img , (5,5))
cv.imshow('blur1', blur)
# cv.imshow('blur2', blur2)

'''Guassian Blur'''
guass = cv.GaussianBlur(img , (3,3), 0)
cv.imshow('guass', guass)

'''Median Blur''' # Top2
median = cv.medianBlur(img ,3)
cv.imshow('Median' , median)


'''bilateral Blur'''  #Indeed the sharpest one top1 
bilateral = cv.bilateralFilter(img , 3 ,15 , 15)
cv.imshow('bilateral', bilateral)
cv.waitKey(0)