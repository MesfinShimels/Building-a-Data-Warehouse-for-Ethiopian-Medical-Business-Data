import cv2
import os
import torch
from ultralytics import YOLO

MODEL_PATH = 'yolov5s.pt'  # Replace with actual model path
IMAGE_DIR = 'data_scraping/images'

model = YOLO(MODEL_PATH)

for image_file in os.listdir(IMAGE_DIR):
    image_path = os.path.join(IMAGE_DIR, image_file)
    img = cv2.imread(image_path)

    results = model(img)
    results.show()

    for r in results:
        for box in r.boxes:
            print(f"Detected: {box.xyxy}, Class: {box.cls}")
