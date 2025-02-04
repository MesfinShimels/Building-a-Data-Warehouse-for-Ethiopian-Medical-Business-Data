# object_detection/yolo_detection.py

import os
import subprocess
import logging
import cv2
import torch
from config import YOLO_REPO_URL, YOLO_DIR, IMAGES_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def clone_yolo_repo():
    """
    Clone the YOLOv5 repository if it does not exist.
    """
    if not os.path.exists(YOLO_DIR):
        logging.info("Cloning YOLOv5 repository...")
        try:
            subprocess.check_call(["git", "clone", YOLO_REPO_URL])
            logging.info("YOLOv5 repository cloned successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to clone YOLOv5 repository: {e}")
    else:
        logging.info("YOLOv5 repository already exists.")

def run_object_detection(image_path):
    """
    Run YOLO object detection on a given image using a pre-trained model.
    """
    # Import YOLO from the cloned repo (requires that YOLOv5 dependencies are installed)
    try:
        # Dynamically import the YOLOv5 model from the cloned repository
        from yolov5.models.experimental import attempt_load
        from yolov5.utils.torch_utils import select_device
        from yolov5.utils.general import non_max_suppression, scale_coords
    except ImportError:
        logging.error("YOLOv5 modules not found. Please ensure YOLOv5 is cloned and dependencies are installed.")
        return None

    # Device selection (CPU or GPU)
    device = select_device('cpu')  # Change to 'cuda' if GPU is available
    weights = os.path.join(YOLO_DIR, 'yolov5s.pt')  # Using a small pre-trained model

    # Download weights if not present (you can automate this or instruct users)
    if not os.path.exists(weights):
        logging.info("Downloading YOLOv5 pre-trained weights...")
        # Here you might download from a URL or instruct the user
        # For simplicity, we assume the weights are already available.
    
    # Load model
    model = attempt_load(weights, map_location=device)
    model.eval()

    # Read image
    img = cv2.imread(image_path)
    if img is None:
        logging.error(f"Failed to read image: {image_path}")
        return None

    # Prepare image for detection (this is a simplified example)
    img_resized = cv2.resize(img, (640, 640))
    img_tensor = torch.from_numpy(img_resized).permute(2, 0, 1).float() / 255.0
    img_tensor = img_tensor.unsqueeze(0).to(device)

    # Inference
    with torch.no_grad():
        pred = model(img_tensor)[0]
    pred = non_max_suppression(pred, 0.25, 0.45)

    # Process detections
    detections = []
    for det in pred:
        if det is not None and len(det):
            for *xyxy, conf, cls in det:
                # Extract bounding box coordinates and other details
                x1, y1, x2, y2 = [int(val.item()) for val in xyxy]
                detections.append({
                    "bbox": [x1, y1, x2, y2],
                    "confidence": conf.item(),
                    "class": int(cls.item())
                })
    return detections

def process_images():
    """
    Process all images in the designated folder and store detection results.
    """
    os.makedirs(IMAGES_PATH, exist_ok=True)
    image_files = [f for f in os.listdir(IMAGES_PATH) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    for image_file in image_files:
        image_path = os.path.join(IMAGES_PATH, image_file)
        logging.info(f"Processing image: {image_path}")
        detections = run_object_detection(image_path)
        if detections is not None:
            logging.info(f"Detections for {image_file}: {detections}")
            # Here you can extend functionality: store results to a file or database

def main():
    clone_yolo_repo()
    process_images()

if __name__ == "__main__":
    main()
