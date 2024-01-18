# Pedestrian-detector-OpenCV-python

Pedestrian detector with Python, OpenCV, and YOLOv8!

Here I'm detecting humans crossing roads and walking person only prediction using the OpenCV library and YOLOv8 model.

step 1: =>      Install requirement.txt file for dependent libraries.

        =>      Download the coco.txt file and yolov8s.pt file.
        
        =>      Download any human walking file 

step 2: =>      Run Pedestrian_count.py file
        =>      Make sure you have assigned the path files like [coco.txt, yolov8.pt, video.mp4 files]
        =>      Detect the video frame and resize
        =>      Using **tracker.py** class will track each person's movement
        =>      Creating a Bounding box and updating each move
        =>      Point the Rectangle edges using a point Polygon Test
        =>      Mark the area points where people crossing
        =>      optional you can put text into the video
        =>      Finally Release the video and close all windows
