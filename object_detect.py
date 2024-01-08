import cv2
import numpy as np

# Read the image
image = cv2.imread('objects-on.jpg')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the colors you want to detect
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

lower_green = np.array([30, 100, 100])
upper_green = np.array([70, 255, 255])

lower_blue = np.array([100, 100, 100])
upper_blue = np.array([130, 255, 255])

# Create masks for each color
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# Find the contours for each color
contours_red = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
contours_green = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
contours_blue = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

# Count the number of objects for each color
num_red_objects = len(contours_red)
num_green_objects = len(contours_green)
num_blue_objects = len(contours_blue)

# Print the results
print('Number of red objects:', num_red_objects)
print('Number of green objects:', num_green_objects)
print('Number of blue objects:', num_blue_objects)