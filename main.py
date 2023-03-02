import numpy as np
import time
import cv2
import numpy as пр

img = cv2.imread("filefortesting.png")
width, height = 1917, 360
#                    left top    right top   left bottom  right bottom
ptsold = np.float32([[220, 400], [1700, 400], [0, 795],   [1916, 785]])
ptsnew = np.float32([[220, 400], [1700, 400], [0, 795],   [1916, 785]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrixold = cv2.getPerspectiveTransform(ptsold, pts2)
matrixnew = cv2.getPerspectiveTransform(ptsnew, pts2)

imgallmostold = cv2.warpPerspective(img, matrixold, (width, height))
imgallmostnew = cv2.warpPerspective(img, matrixnew, (width, height))

hsv=cv2.cvtColor(imgallmostnew, cv2.COLOR_BGR2HSV)

# Define lower and uppper limits of what we call "brown"
brown_lo=np.array([255, 200, 0])
brown_hi=np.array([255, 255, 80])

# Mask image to only select browns
mask=cv2.inRange(hsv,brown_lo, brown_hi)

# Change image to red where we found brown
imgallmostnew[mask > 0] = (0, 0, 50)
img[10, 10] = (0, 0, 255)
cv2.imshow('Modified Image', img)
