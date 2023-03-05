import cv2
import numpy as np
import time
# Open video capture
cap = cv2.VideoCapture('seret.mp4')
width, height = 640, 360
#                   left top    right top   left bottom  right bottom
pts1 = np.float32([[85, 130], [550, 130], [0, 251], [640, 251]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
green = (0, 255, 0)
min_size = 550


def empty(a):
    pass


lower_green = np.array([0, 60, 0])  # Dark green
upper_yellow = np.array([255, 255, 128])  # Light yellow

while True:
    # Read frame
    ret, frame = cap.read()

    if not ret:
        break

    imgallmostold = cv2.warpPerspective(frame, matrix, (width, height))
    black = (0, 0, 0)
    cv2.rectangle(imgallmostold, (0, 0), (80, 360), black, -1)
    cv2.rectangle(imgallmostold, (560, 0), (640, 360), black, -1)
    cv2.rectangle(imgallmostold, (0, 0), (640, 100), black, -1)
    cv2.rectangle(imgallmostold, (424, 150), (500, 260), black, -1)
    cv2.rectangle(imgallmostold, (140, 150), (215, 260), black, -1)

    frame432432 = cv2.cvtColor(imgallmostold, cv2.COLOR_BGR2RGB)

    mask = cv2.inRange(frame432432, lower_green, upper_yellow)

    frame432432[mask != 0] = [0, 0, 0]
    frame432432 = cv2.cvtColor(frame432432, cv2.COLOR_RGB2BGR)

    imgHSV = cv2.cvtColor(frame432432, cv2.COLOR_BGR2HSV)
    h_min = 41
    h_max = 179
    s_min = 17
    s_max = 255
    v_min = 0
    v_max = 255
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(frame432432, frame432432, mask=mask)
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=1)
    object_detector.apply(imgResult)
    counters, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in counters:
        area = cv2.contourArea(cnt)
        if area > min_size:
            x, y, w, h = cv2.boundingRect(cnt)
            print(y)
            if (150-w < x < 500+w and 150-h < y < 260+h) or (140-w < x < 215+w and 150-h < y < 260+h):
                cv2.rectangle(imgResult, (x, y), (x + w, y + h), green, 3)
                print(x, y, w, h)

    cv2.imshow('Modified Frame', imgResult)
    cv2.imshow('Modified musk', mask)

    cv2.waitKey(2)
    time.sleep(0.0022)

cap.release()
cv2.destroyAllWindows()
