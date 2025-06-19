import cv2 as cv
import numpy as np

blank = np.zeros((400,400) , dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30) , (370,370) , 255, -1 )
circle = cv.circle(blank.copy() , (blank.shape[0]//2 ,blank.shape[1]//2 ) , 200 , 255 , -1)
cv.imshow('rect' , rectangle)
cv.imshow('circle' , circle)

'''Bitwise And'''
bitwise_and = cv.bitwise_and(rectangle , circle)
cv.imshow('AND',bitwise_and)

'''Bitwise OR'''
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Or' , bitwise_or)

'''Bitwise XOR'''
bitwise_XOR = cv.bitwise_xor(rectangle , circle)
cv.imshow('Xor' , bitwise_XOR)

'''Bitwise Not'''
bitwise_Not = cv.bitwise_not(bitwise_XOR)
cv.imshow("NOT" , bitwise_Not)
bitwise_Not2 = cv.bitwise_not(bitwise_or)
cv.imshow("NOT@" , bitwise_Not2)


cv.waitKey(0)