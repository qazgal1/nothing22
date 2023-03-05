import cv2
import numpy as np


cap = cv2.VideoCapture("seret.mp4")


def resize(img):
    return cv2.resize(img, (512, 512))  # arg1- input image, arg- output_width, output_height
ret, frame = cap.read()
l_b = np.array([0, 230, 170])  # lower hsv bound for red
u_b = np.array([255, 255, 220])  # upper hsv bound to red

while ret:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, l_b, u_b)

    cv2.imshow("frame", resize(frame))

    cv2.imshow("mask", mask)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
