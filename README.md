README: Ethiopian Medical Business Data Warehouse
Overview
This project aims to build a robust data warehouse to store Ethiopian medical business data scraped from Telegram channels. The collected data is cleaned, structured, and integrated into a PostgreSQL database. Additionally, we implement object detection on images using the YOLO model.
Project Structure
project_root/
│-- data_scraping/
│   │-- telegram_scraper.py
│   │-- image_downloader.py
│   │-- logs/
│-- data_cleaning/
│   │-- data_cleaner.py
│   │-- dbt_models/
│-- object_detection/
│   │-- yolo_model.py
│-- database/
│   │-- schema.sql
│   │-- db_config.py
│-- reports/
│   │-- interim_report.md
│-- main.py
│-- requirements.txt
│-- README.md
Features
Data Scraping: Uses Telethon to extract messages and images from Telegram.
Data Cleaning: Handles duplicates, missing values, and standardizes formats.
Database Storage: PostgreSQL schema optimized for structured storage.
ETL Pipeline: DBT-based transformations ensure data consistency.
Object Detection: YOLO model applied to identify medical products in images.
Logging and Monitoring: Tracks errors and performance metrics.
Installation
1.Clone the repository: 
git clone https://github.com/your-repo/medical-data-warehouse.git
cd medical-data-warehouse
2.
3.Set up a virtual environment and install dependencies: 
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
4.
5.Set up PostgreSQL and create the required tables: 
psql -U your_user -d medical_db -f database/schema.sql
6.
7.Configure API keys and credentials in a .env file: 
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE=your_phone_number
8.
Usage
Scrape Telegram data: 
python data_scraping/telegram_scraper.py

Download images: 
python data_scraping/image_downloader.py

Clean data: 
python data_cleaning/data_cleaner.py

Insert data into PostgreSQL: 
python database/db_config.py

Run object detection: 
python object_detection/yolo_model.py

Requirements
The dependencies are listed in requirements.txt. Install them using:
pip install -r requirements.txt
Future Work
Optimize scraping for real-time updates
Improve object detection accuracy
Develop analytical dashboards# Ethiopian Medical Business Data Warehouse

This project scrapes data from Telegram channels, cleans and transforms it, runs object detection on images using YOLO, stores the data in a PostgreSQL warehouse, and exposes it via a FastAPI application.

## File Structure


Author
Mesfin Shimels 
