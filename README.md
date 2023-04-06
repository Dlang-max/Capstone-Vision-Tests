# Capstone-Vision-Tests
Vision processing tests for my Senior Capstone

+ ### Images Folder
This folder contains code to take photos from a camera every 10 frames. The photos produced from this code will be annotated with LabelImg and used to train a CNN to detect ping pong balls. 

+ ### Unblur Folder
This folder contains code to unblur frames from a camera stream by increasing the shutter speed of a camera. When I was originally taking images of ping pong balls bouncing on a table they were extremely blurry. This is a massive issue because I need to accurately detect and draw a bounding box around a ping pong ball. I need this accuracy to determine how far away the ping pong ball is from the camera allowing me to predict the motion of the ping pong ball.  
