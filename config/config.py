
---

## **4. config/config.py**

# Create **config/config.py**:

# python
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Environment configurations
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
DATABASE_URL = os.getenv("DATABASE_URL")
YOLO_MODEL_PATH = os.getenv("YOLO_MODEL_PATH")

# Setup logging
LOG_DIR = os.path.join(os.getcwd(), "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "app.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Config and logging setup complete.")
