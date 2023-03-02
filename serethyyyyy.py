# importing the necessary libraries
import time

import cv2
import numpy as np
stopped = 1
# Creating a VideoCapture object to read the video
cap = cv2.VideoCapture('seret.mp4')

while cap.isOpened():
    if stopped == 1:
        ret, frame = cap.read()

        # Define the color range to replace (in this case, green to yellow)


        lower_green = np.array([0, 50, 0])  # Dark green
        upper_yellow = np.array([255, 255, 128])  # Light yellow
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create a mask for the specified color range
        maskNoYellow = cv2.inRange(frame, lower_green, upper_yellow)

        # Replace the pixels in the frame that fall within the color range
        frame[maskNoYellow != 0] = [0, 0, 0]  # Replace with blue

        # Convert the frame back to BGR format
        frameNoYollow = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        imgHSV = cv2.cvtColor(frameNoYollow, cv2.COLOR_BGR2HSV)

        h_minNUM = 102
        h_maxNUM = 179
        s_minNUM = 69
        s_maxNUM = 255
        v_minNUM = 41
        v_maxNUM = 255

        # print(h_min, h_max, s_min, s_max, v_min, v_max)
        lower = np.array([h_minNUM, s_minNUM, v_minNUM])
        upper = np.array([h_maxNUM, s_maxNUM, v_maxNUM])
        mask123 = cv2.inRange(imgHSV, lower, upper)

        # Display the modified frame
        cv2.imshow('Modified Frame', mask123)
        time.sleep(0.01)
    else:
        time.sleep(0.1)
    if cv2.waitKey(1) == ord(' '):
        stopped = stopped*-1
    if cv2.waitKey(1) == ord('q'):
        exit()
    # cv2.imshow("croped image imgHSV", imgHSV)


