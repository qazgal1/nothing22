import cv2
import numpy as np
import time

# define the lower and upper bounds of the red color in HSV color space
lower_red = np.array([165, 0, 0])
upper_red = np.array([255, 255, 255])
width, height = 640, 360
#                   left top    right top   left bottom  right bottom
pts1 = np.float32([[85, 130], [550, 130], [0, 251], [640, 251]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=70)

# create a VideoCapture object to capture video from the default camera
cap = cv2.VideoCapture("seret.mp4")

# create a kernel for the morphological operations
kernel = np.ones((5, 5), np.uint8)

while True:
    # read a frame from the video stream
    ret, frame = cap.read()
    roi = frame[145: 255, 100: 540]

    # convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # create a mask for the red color
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # apply morphological opening to remove noise in the background
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # apply Gaussian blur to smooth the edges
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 60:
            cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)

    imS = cv2.resize(roi, (width*2, height*2))  # Resize image

    cv2.imshow('Red Only', imS)
    time.sleep(0.02)
    # exit if the user presses the 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
