import math

# meters
SHOULDER_LENGTH = 0.254
ELBOW_LENGTH = 0.254

x = 0
y = 0

print("Enter x:")
x = float(input())

print("Enter y:")
y = float(input())

elbow_angle = math.acos((x * x + y * y - SHOULDER_LENGTH * SHOULDER_LENGTH - ELBOW_LENGTH * ELBOW_LENGTH) / (2 * ELBOW_LENGTH * SHOULDER_LENGTH))
shoulder_angle = math.atan2(y, x) - math.atan2(ELBOW_LENGTH * math.sin(elbow_angle), SHOULDER_LENGTH + ELBOW_LENGTH * math.cos(elbow_angle))

elbow_angle = math.degrees(elbow_angle)
shoulder_angle = math.degrees(shoulder_angle)

shoulder_angle = 90 - shoulder_angle

print("Elbow Angle: ", elbow_angle)
print("Shoulder Angle: ", shoulder_angle)
