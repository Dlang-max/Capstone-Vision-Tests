import cv2

# Create instances of cv2.VideoCapture for each camera
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while True:
    # Read a frame from each camera
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # Resize the frames to have the same height
    h, w = frame1.shape[:2]
    frame2 = cv2.resize(frame2, (w, h))

    # Concatenate the frames horizontally
    frame_concat = cv2.hconcat([frame1, frame2])

    # Display the concatenated frame
    cv2.imshow('Cameras', frame_concat)

    # Wait for a key press and exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources and close the windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()
