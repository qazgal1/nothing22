import numpy as np

import cv2
import numpy as пр

img = cv2.imread("newimage.png")
width, height = 1917, 360
#                    left top    right top   left bottom  right bottom
ptsold = np.float32([[220, 400], [1700, 400], [0, 795],   [1916, 785]])
ptsnew = np.float32([[220, 400], [1700, 400], [0, 795],   [1916, 785]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrixold = cv2.getPerspectiveTransform(ptsold, pts2)
matrixnew = cv2.getPerspectiveTransform(ptsnew, pts2)

imgallmostold = cv2.warpPerspective(img, matrixold, (width, height))
imgallmostnew = cv2.warpPerspective(img, matrixnew, (width, height))

hsv=cv2.cvtColor(imgallmostnew,cv2.COLOR_BGR2HSV)

# Define lower and uppper limits of what we call "brown"
brown_lo=np.array([255, 200, 0])
brown_hi=np.array([255, 255, 80])

# Mask image to only select browns
mask=cv2.inRange(hsv,brown_lo, brown_hi)

# Change image to red where we found brown
imgallmostnew[mask > 0] = (0, 0, 50)


cv2.imwrite("result.png", imgallmostnew)

#
# def empty(a):
#     pass
#
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars", 640, 240)
# cv2.createTrackbar("Huw Min", "TrackBars",0,179,empty)
# cv2.createTrackbar("Huw Max", "TrackBars",179,179,empty)
# cv2.createTrackbar("Sat Min", "TrackBars",0,255,empty)
# cv2.createTrackbar("Sat Max", "TrackBars",255,255,empty)
# cv2.createTrackbar("Val Min", "TrackBars",0,255,empty)
# cv2.createTrackbar("Val Max", "TrackBars",255,255,empty)
#
# while True:
#     print("run")
#     imgHSV = cv2.cvtColor(imgallmostnew, cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Huw Min", "TrackBars")
#     h_max = cv2.getTrackbarPos("Huw Max", "TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
#
#     print(h_min, h_max, s_min, s_max, v_min, v_max)
#     lower = np.array([h_min,s_min, v_min])
#     upper = np.array([h_max,s_max, v_max])
#     mask = cv2.inRange(imgHSV, lower, upper)
#
#     cv2.imshow("croped image old", imgallmostold)
#     cv2.imshow("croped image mask", mask)
#     cv2.imshow("croped image imgHSV", imgHSV)
#     cv2.waitKey(1)
#
#
#
