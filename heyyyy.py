import cv2
import numpy as np
# Create MOG2 background subtractor
mog = cv2.createBackgroundSubtractorMOG2()

min_size = 1000

# Initialize KLT parameters
klt_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Empty dictionary to hold object tracks
tracks = {}

# Open video capture
cap = cv2.VideoCapture('seret.mp4')

while True:
    # Read frame
    ret, frame = cap.read()

    if not ret:
        break

    # Apply MOG2 to subtract background
    fg_mask = mog.apply(frame)

    # Apply threshold to binarize mask
    threshold = cv2.threshold(fg_mask, 128, 255, cv2.THRESH_BINARY)[1]

    # Find contours of moving objects
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through contours and filter by size
    for contour in contours:
        # Calculate contour area
        area = cv2.contourArea(contour)

        # Filter out small contours
        if area > min_size:
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)

            # Try to find object in existing tracks
            matched_track = None
            for track in tracks.values():
                # Get last known position of track
                last_x, last_y = track[-1]

                # Check if bounding box overlaps with last known position
                if x <= last_x <= x + w and y <= last_y <= y + h:
                    matched_track = track
                    break

            if matched_track is not None:
                # Update existing track with new position
                p0 = np.array([last_x + w / 2, last_y + h / 2], np.float32).reshape(-1, 1, 2)
                p1, st, err = cv2.calcOpticalFlowPyrLK(prev_frame, frame, p0, None, **klt_params)
                x_new, y_new = p1[0][0]
                matched_track.append((x_new, y_new))
            else:
                # Create new track
                p0 = np.array([x + w / 2, y + h / 2], np.float32).reshape(-1, 1, 2)
                p1, st, err = cv2.calcOpticalFlowPyrLK(prev_frame, frame, p0, None, **klt_params)
                x_new, y_new = p1[0][0]
                tracks[len(tracks)] = [(x_new, y_new)]

            # Draw bounding box around object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display frame with bounding boxes
    cv2.imshow('frame132',  frame)

    # Store previous frame for KLT tracking
    prev_frame = frame.copy()
    if cv2.waitKey(1) == ord("q"):
        break
    # Exit loop when 'q


cap.release()
cv2.destroyAllWindows()