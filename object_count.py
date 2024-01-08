# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# from numpy.lib.polynomial import poly

# img = cv2.imread('various-objects.jpg')
# img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(10,10))
# plt.axis('off')
# plt.imshow(img1)
# plt.show()

# box, label, count = cv.detect_common_objects(img)
# output = draw_bbox(img, box, label, count)

# output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(10,10))
# plt.axis('off')
# plt.imshow(output)
# plt.show()

# print("Number of objects in this image are " +str(len(label)))
import cv2
import numpy as np

# Read the image
image = cv2.imread('new_obj.JPG')  # Replace with the actual path to your image

# Convert the image to HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range for detecting red (you can adjust this based on your specific color)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Threshold the HSV image to get only red colors
mask = cv2.inRange(hsv, lower_red, upper_red)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Counter for the number of detected objects
object_count = 0

# Loop through the contours
for contour in contours:
    # Approximate the contour to a polygon
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Get the number of vertices (sides) in the polygon
    num_sides = len(approx)

    # Get the area of the contour
    area = cv2.contourArea(contour)

    # Set a threshold for area to filter out small contours
    if area > 100:
        # Draw the contour and display the shape and color information
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
        cv2.putText(image, f"{num_sides} sides", (approx[0][0][0], approx[0][0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Increment the object count
        object_count += 1

# Display the image
cv2.imshow('Detected Objects', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the total number of detected objects
print(f"Total Objects: {object_count}")
