import cv2
import numpy as np
img = cv2.imread("filefortesting.png")
width, height = 1917, 360

#                    left top    right top   left bottom  right bottom
pts1 = np.float32([[220, 400], [1700, 400], [0, 795], [1916, 785]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgallmostnew = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow('Modified Image', imgallmostnew)
cv2.waitKey(0)