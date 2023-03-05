import cv2
import numpy as np

# load the image
img = cv2.imread('filefortesting.PNG')

# define the top-left and bottom-right corners of the ROI
x1, y1 = 100, 100
x2, y2 = 300, 300

# create a binary mask for the ROI


# show the original image, the mask, and the masked image
cv2.imshow('Original Image', img)
cv2.imshow('ROI Mask', mask)
cv2.imshow('Masked Image', masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
