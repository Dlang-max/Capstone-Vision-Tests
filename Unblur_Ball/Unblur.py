import cv2

cap = cv2.VideoCapture(0)  # create a VideoCapture object to access the camera

cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)  # disable auto-exposure
cap.set(cv2.CAP_PROP_EXPOSURE, -9)  # set the exposure to -4 (corresponds to a shutter speed of 1/1000)
cap.set(10, 400)

while True:
    ret, frame = cap.read()  # read a frame from the camera
    cv2.imshow('frame', frame)  # show the frame in a window named "frame"
    if cv2.waitKey(1) == ord('q'):  # wait for a key press and check if it's the 'q' key
        break

cap.release()  # release the camera
cv2.destroyAllWindows()  # destroy all windows
