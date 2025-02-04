import os
import logging
import torch
import cv2

# Directories for images and detection outputs
IMAGES_DIR = os.path.join(os.getcwd(), "data", "images")
DETECTIONS_DIR = os.path.join(os.getcwd(), "data", "detections")
if not os.path.exists(DETECTIONS_DIR):
    os.makedirs(DETECTIONS_DIR)

# Load the YOLOv5 model via torch.hub
# This will automatically download the model if not present
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_and_save(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            logging.error(f"Failed to read image: {image_path}")
            return
        results = model(img)
        # Save detection results as CSV (you may also save JSON or visualize the results)
        detections_csv = results.pandas().xyxy[0].to_csv(index=False)
        base_name = os.path.basename(image_path).split('.')[0]
        output_file = os.path.join(DETECTIONS_DIR, f"{base_name}_detections.csv")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(detections_csv)
        logging.info(f"Object detection completed for {image_path}")
    except Exception as e:
        logging.error(f"Error in object detection for {image_path}: {e}")

def process_all_images():
    for file_name in os.listdir(IMAGES_DIR):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            detect_and_save(os.path.join(IMAGES_DIR, file_name))

if __name__ == "__main__":
    process_all_images()
