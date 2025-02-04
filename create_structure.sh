#!/bin/bash

# Create directory structure
mkdir -p ethiopian-medical-dw/{data_scraping/raw_data,dbt/{models/{staging,marts/core},tests},object_detection/detection_results,fastapi_app/api/v1,database,logs}

# Create empty files
touch ethiopian-medical-dw/.env
touch ethiopian-medical-dw/requirements.txt
touch ethiopian-medical-dw/data_scraping/{telegram_scraper.py,image_downloader.py}
touch ethiopian-medical-dw/dbt/{dbt_project.yml,profiles.yml}
touch ethiopian-medical-dw/dbt/models/{schema.yml,staging/stg_medical_data.sql,marts/core/dim_medical_businesses.sql}
touch ethiopian-medical-dw/object_detection/detect.py
touch ethiopian-medical-dw/fastapi_app/{main.py,database.py,models.py,schemas.py,crud.py}
touch ethiopian-medical-dw/fastapi_app/api/v1/endpoints.py
touch ethiopian-medical-dw/database/{init_db.py,schema.sql}
touch ethiopian-medical-dw/logs/{scraping.log,cleaning.log,detection.log}

# Add execute permissions to script files
chmod +x ethiopian-medical-dw/data_scraping/telegram_scraper.py
chmod +x ethiopian-medical-dw/object_detection/detect.py

echo "Project structure created successfully!"