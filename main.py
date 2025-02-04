import os
import argparse
import logging
from subprocess import run
from fastapi import FastAPI
import uvicorn

# Define paths for the task scripts
BASE_DIR = os.getcwd()
SCRAPE_SCRIPT = os.path.join(BASE_DIR, "scripts", "fetch_data.py")
PROCESS_SCRIPT = os.path.join(BASE_DIR, "scripts", "process_data.py")
DETECT_SCRIPT = os.path.join(BASE_DIR, "scripts", "detect_objects.py")

def run_task(script_path):
    result = run(["python", script_path])
    if result.returncode != 0:
        logging.error(f"Task {script_path} failed.")
    else:
        logging.info(f"Task {script_path} completed successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Data Warehouse Workflow")
    parser.add_argument("--scrape", action="store_true", help="Scrape Telegram channels")
    parser.add_argument("--process", action="store_true", help="Process and clean scraped data")
    parser.add_argument("--detect", action="store_true", help="Run object detection on images")
    parser.add_argument("--serve", action="store_true", help="Run FastAPI server")
    args = parser.parse_args()

    if args.scrape:
        run_task(SCRAPE_SCRIPT)
    if args.process:
        run_task(PROCESS_SCRIPT)
    if args.detect:
        run_task(DETECT_SCRIPT)
    if args.serve:
        app = FastAPI()

        @app.get("/")
        def read_root():
            return {"message": "Welcome to the Ethiopian Medical Business Data Warehouse API"}

        logging.info("Starting FastAPI server...")
        uvicorn.run(app, host="0.0.0.0", port=8000)
        
    # If no argument is provided, print help
    if not (args.scrape or args.process or args.detect or args.serve):
        parser.print_help()
