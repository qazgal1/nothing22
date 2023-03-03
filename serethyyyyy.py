# importing the necessary libraries
import time

import cv2
import numpy as np

stopped = 1
# Creating a VideoCapture object to read the video
cap = cv2.VideoCapture('seret.mp4')


# def replace_Color(Fullframe, low_color, high_color, color_to_replace=[0,0,0]):
#     lower_green = np.array(low_color)  # Dark green
#     upper_yellow = np.array(high_color)  # Light yellow
#     frame = cv2.cvtColor(Fullframe, cv2.COLOR_BGR2RGB)
#
#     # Create a mask for the specified color range
#     maskNoYellow = cv2.inRange(frame, lower_green, upper_yellow)
#
#     # Replace the pixels in the frame that fall within the color range
#     frame[maskNoYellow != 0] = color_to_replace
#     # Convert the frame back to BGR format
#     frameNoYollow = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#
#     return frameNoYollow


while cap.isOpened():
    if stopped == 1:
        ret, frame = cap.read()
        if ret:
            width, height = 1917, 360
            #                    left top    right top   left bottom  right bottom
            ptsold = np.float32([[220, 400], [1700, 400], [0, 795], [1916, 785]])
            ptsnew = np.float32([[220, 400], [1700, 400], [0, 795], [1916, 785]])
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrixold = cv2.getPerspectiveTransform(ptsold, pts2)
            matrixnew = cv2.getPerspectiveTransform(ptsnew, pts2)

            imgallmostold = cv2.warpPerspective(frame, matrixold, (width, height))
            imgallmostnew = cv2.warpPerspective(frame, matrixnew, (width, height))

            # Define the color range to replace (in this case, green to yellow)
            # FrameNoYellow = replace_Color(frame, [0, 50, 0], [255, 255, 128],)
            #cv2.imshow('Mod3ified Frame', FrameNoYellow)
            cv2.imshow('Modified Fram43e', imgallmostnew)
            print("wokrinh")
            imgHSV = cv2.cvtColor(imgallmostnew, cv2.COLOR_BGR2HSV)
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
        stopped = stopped * -1
    if cv2.waitKey(1) == ord('q'):
        exit()
    # cv2.imshow("croped image imgHSV", imgHSV)
