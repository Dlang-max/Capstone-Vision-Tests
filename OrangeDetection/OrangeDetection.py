import cv2
import numpy as np

# Define the range of orange color in HSV
lower_orange = np.array([0, 238, 13])
upper_orange = np.array([24, 255, 47])

# Initialize the webcam
cap = cv2.VideoCapture(0)

cap.set( 10, 200 )


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for orange color
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Find contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest = contours[0]
    


    # Draw a bounding box around each contour
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        largest_w = cv2.boundingRect(largest)[2]
        largest_h = cv2.boundingRect(largest)[3]

        if( w > largest_w and h > largest_h ):
            largest = contour


    x, y, w, h = cv2.boundingRect(largest)    
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('orange detection', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
