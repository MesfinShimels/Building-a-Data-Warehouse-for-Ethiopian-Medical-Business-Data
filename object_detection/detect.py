import cv2
import torch
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Configure detection logging
logging.basicConfig(
    filename=os.getenv('DETECTION_LOG_PATH'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def detect_objects(image_path):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=os.getenv('YOLO_MODEL_PATH'))
    results = model(image_path)
    
    detections = []
    for *xyxy, conf, cls in results.xyxy[0]:
        detection = {
            'x1': xyxy[0].item(),
            'y1': xyxy[1].item(),
            'x2': xyxy[2].item(),
            'y2': xyxy[3].item(),
            'confidence': conf.item(),
            'class': results.names[int(cls)]
        }
        detections.append(detection)
        logging.info(f"Detected {detection['class']} with confidence {detection['confidence']:.2f}")
    
    return detections