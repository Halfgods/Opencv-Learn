# import cv2 as cv
# import numpy as np

# img = cv.imread('pictures/shapes.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # Optional histogram equalization if needed
# equalized = cv.equalizeHist(gray)

# # Blur to reduce noise (better than nothing)
# blur = cv.GaussianBlur(equalized, (5, 5), 0)

# # Adaptive Thresholding
# thresh = cv.adaptiveThreshold(blur, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# # ⛏ Remove tiny white dots (noise)
# kernel = np.ones((3,3), np.uint8)
# thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)

# # 🎯 Remove very small contours (white garbage) manually
# contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# # Remove blobs with very small area
# for c in contours:
#     area = cv.contourArea(c)
#     if area < 1000:  # You can increase or decrease this based on test
#         cv.drawContours(thresh, [c], -1, (0, 0, 0), -1)  # fill them black

# dilated = cv.dilate(thresh , (3,3) , iterations= 3)
# contours , hierachy = cv.findContours(dilated ,cv.RETR_EXTERNAL , cv.CHAIN_APPROX_SIMPLE )
# cv.drawContours(img , contours , -1 , (0,225,0) , -1)
# cv.imshow("Cleaned", img)
# cv.waitKey(0)
# cv.destroyAllWindows()
import cv2 as cv
import numpy as np

# Load image and preprocess
img = cv.imread('pictures/shapes.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
equalized = cv.equalizeHist(gray)
blur = cv.GaussianBlur(equalized, (5, 5), 0)

# Adaptive Threshold
thresh = cv.adaptiveThreshold(blur, 255,
                               cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv.THRESH_BINARY,
                               11, 2)

# Clean noise using morphological opening
kernel = np.ones((3, 3), np.uint8)
opened = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)

# Remove tiny blobs by area
contours, _ = cv.findContours(opened, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in contours:
    if cv.contourArea(c) < 1000:
        cv.drawContours(opened, [c], -1, (0, 0, 0), -1)

# OPTIONAL: Do NOT over-dilate — comment out this line for better precision
# dilated = cv.dilate(opened, kernel, iterations=1)

# Final contour detection
final_contours, _ = cv.findContours(opened, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Draw filled contours on a copy of the original
filled = img.copy()
cv.drawContours(filled, final_contours, -1, (0, 255, 0), thickness=cv.FILLED)

cv.imshow("Final Contours", thresh)
cv.waitKey(0)
cv.destroyAllWindows()
