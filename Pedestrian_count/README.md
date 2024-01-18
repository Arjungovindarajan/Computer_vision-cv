# Pedestrian-detector-OpenCV-python

Pedestrian detector with Python, OpenCV and YOLOv8 !

Hear im detecting human crossing road and walking persion only prediction using OpenCV libsrary and YOLOv8 model.

step 1: =>      install requirement.txt file for dependend libraries.
        =>      Download coco.txt file and yolov8s.pt file.
        =>      Download any human walking file 

step 2: =>      Run Pedestrian_count.py file
        =>      Make sure you have asign the path files like [coco.txt, yolov8.pt, video.mp4 files]
        =>      Detect the video frame and resizing
        =>      Using **tracker.py** class will tracking the each person movement
        =>      Creating Bounding box and update the each move
        =>      Point the Rectangle edges use point Polygon Test
        =>      Mark the area points where people crossing
        =>      optional you can Puttext into the video
        =>      Finally Release the video and close all windows