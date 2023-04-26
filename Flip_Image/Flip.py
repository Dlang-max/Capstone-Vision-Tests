import cv2

# Create a VideoCapture object to capture the video stream from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    
    # Flip the frame horizontally using the flip() function
    flipped_frame = cv2.flip(frame, -1)

    # Show the flipped frame in a window
    cv2.imshow('Flipped Frame', flipped_frame)

    # Check if the user has pressed the 'q' key to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
