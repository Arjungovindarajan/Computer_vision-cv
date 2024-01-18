import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import Tracker


model=YOLO('yolov8s.pt')


# def RGB(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE :  
#         colorsBGR = [x, y]
#         print(colorsBGR)

# cv2.namedWindow('RGB')
# cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture('Pedestrian.mp4')


with open("coco.txt", "r") as my_file:
    class_list = my_file.read().split("\n")

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
output_video = cv2.VideoWriter('output_video.avi', fourcc, 10.0, (1720, 900))

count=0
tracker=Tracker()   


area1 = [(2,408),(4,246),(1018,236),(1018,422)]


while True:    
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue


    frame=cv2.resize(frame,(1020,500))

    results=model.predict(frame)
    a = results[0].boxes.data

    px=pd.DataFrame(a).astype("float")
#    print(px)
    
    list=[]
    persion_c = set()
    for index,row in px.iterrows():
        x1, y1, x2, y2, _, d = map(int, row)
        c = class_list[d]

        if c == "person":
            list.append([x1,y1,x2,y2])
            # persion_c.add(int(id))

    bbox_idx = tracker.update(list)
    # print(bbox_idx)
    current_persons = len(bbox_idx)
    cv2.putText(frame, f'Now in frame: {current_persons}', (10, 40), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
    id_counts = {}

    for bbox in bbox_idx:
        x3,y3,x4,y4,id=bbox
        cx=int(x3+x4)//2
        cy=int(y3+y4)//2
        results = cv2.pointPolygonTest(np.array(area1,np.int32), ((x3,y4)), False)
        if results>=0:
            cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),2)
            cv2.circle(frame,(x4,y4), 5, (255,0,255),-1)
            cv2.putText(frame,str(int(id)),(x3,y3),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)
            id_counts[id] = id_counts.get(id, 0) + 1
            # print("id_method", type(id), id)
    # total_persons = (len(persion_c))
    for unique_id, count in id_counts.items():
        cv2.putText(frame, f'Total Persons: {unique_id}', (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
    
    cv2.polylines(frame, [np.array(area1,np.int32)],True,(0,0,255),2)
    cv2.imshow("RGB", frame)
    output_video.write(frame)

    if cv2.waitKey(1) & 0xFF==27:
        break

output_video.release()
cap.release()
cv2.destroyAllWindows()