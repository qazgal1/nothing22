import cv2
import numpy as np

# load the image
img = cv2.imread("ffinale.png")

# create a window to display the image
cv2.namedWindow("Painting App")

# set the mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        # fill in the area that the user has marked with the blue color
        mask = np.zeros((img.shape[0] + 2, img.shape[1] + 2), np.uint8)
        cv2.floodFill(img, mask, (x, y), (0, 0, 0), (0, 0, 0), (0, 0, 0), cv2.FLOODFILL_FIXED_RANGE)

cv2.setMouseCallback("Painting App", draw_circle)

while True:
    # display the image
    cv2.imshow("Painting App", img)

    # check for key presses
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, quit the program
    if key == ord('q'):
        break

# find the contours of the filled region
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# create a mask with the filled region
mask = np.zeros_like(img)
cv2.drawContours(mask, contours, 0, (255, 255, 255), -1)

# set everything outside of the filled region to black
mask_inv = cv2.bitwise_not(mask)
img = cv2.bitwise_and(img, mask)
img = cv2.add(img, mask_inv)

# display the final image
cv2.imshow("Final Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
