# config.py

# Telegram API Credentials
TELEGRAM_API_ID = YOUR_API_ID          # Replace with your API ID (integer)
TELEGRAM_API_HASH = "YOUR_API_HASH"     # Replace with your API hash (string)

# List of target Telegram channels (you can add more from the provided links)
TELEGRAM_CHANNELS = [
    "DoctorsET",
    "Chemed",  # Assuming channel name for Chemed Telegram Channel
    "lobelia4cosmetics",
    "yetenaweg",
    "EAHCI"
]

# Database configuration (example for PostgreSQL)
DATABASE_URL = "postgresql://username:password@localhost:5432/your_database"

# Path to store raw data and images
RAW_DATA_PATH = "raw_data/"
IMAGES_PATH = "images/"

# YOLO configuration
YOLO_REPO_URL = "https://github.com/ultralytics/yolov5.git"
YOLO_DIR = "yolov5"
