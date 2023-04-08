import cv2
import math

# Set camera properties
focal_length = 4.0   # Focal length in mm
sensor_width = 3.2   # Sensor width in mm
sensor_height = 2.4  # Sensor heicdght in mm

# Open the camera
cap = cv2.VideoCapture(0)

# Get camera resolution
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Calculate the horizontal and vertical FOV
h_fov = 2 * math.atan(sensor_width / (2 * focal_length)) * 180 / math.pi
v_fov = 2 * math.atan(sensor_height / (2 * focal_length)) * 180 / math.pi

print("Horizontal FOV:", h_fov, "degrees")
print("Vertical FOV:", v_fov, "degrees")

# Release the camera
cap.release()
