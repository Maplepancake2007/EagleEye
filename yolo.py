from ultralytics import YOLO
import cv2
model= YOLO("yolov8n.pt")

results = model('bus.jfif',classes=0,conf=0.5)
items=results[0]
for item in items:
    cls = int(item.boxes.cls)
    if cls == 0:
        print("person")