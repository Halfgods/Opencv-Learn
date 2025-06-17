<<<<<<< HEAD
import cv2 as cv
img = cv.imread('pictures/cat.jpg')
# Converting to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

# Canny Edge Detector
canny = cv.Canny(blur,175,175)

# Dilating 
dilated = cv.dilate(canny , (3,3) , iterations= 5 )

# Eroded
eroded = cv.erode(dilated , (3,3) , iterations= 5)

#  Resizing
resized = cv.resize(img, (500,500) ,interpolation=cv.INTER_LINEAR)

# Cropping
cropped = resized[100:400,200:500]

cv.imshow("Test" , cropped)
=======
import cv2 as cv
img = cv.imread('pictures/cat.jpg')
# Converting to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

# Canny Edge Detector
canny = cv.Canny(blur,175,175)

# Dilating 
dilated = cv.dilate(canny , (3,3) , iterations= 5 )

# Eroded
eroded = cv.erode(dilated , (3,3) , iterations= 5)

#  Resizing
resized = cv.resize(img, (500,500) ,interpolation=cv.INTER_LINEAR)

# Cropping
cropped = resized[100:400,200:500]

cv.imshow("Test" , cropped)
>>>>>>> 4e12cabbdd49b83263e1e42630ef03e2abd0bc1f
cv.waitKey(0)