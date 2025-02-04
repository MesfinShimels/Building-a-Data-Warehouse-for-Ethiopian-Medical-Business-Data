# data_transformation/clean_transform.py

import os
import logging

RAW_DATA_PATH = "raw_data/"
CLEAN_DATA_PATH = "clean_data/"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def clean_data():
    """
    This function reads raw data files, removes duplicates,
    handles missing values, and standardizes data formats.
    It then writes the cleaned data to a new directory.
    """
    os.makedirs(CLEAN_DATA_PATH, exist_ok=True)
    raw_files = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith("_messages.txt")]

    for file_name in raw_files:
        file_path = os.path.join(RAW_DATA_PATH, file_name)
        clean_file_path = os.path.join(CLEAN_DATA_PATH, file_name)

        logging.info(f"Processing file: {file_path}")
        seen_messages = set()
        cleaned_lines = []

        with open(file_path, "r", encoding="utf-8") as infile:
            for line in infile:
                # Basic cleaning: remove duplicate messages (by message id)
                message_id = line.split("\t")[0]
                if message_id in seen_messages:
                    continue
                seen_messages.add(message_id)

                # Further cleaning: you can add more logic to handle missing values, etc.
                if "None" in line or line.strip() == "":
                    continue

                cleaned_lines.append(line)

        # Write the cleaned data to the new file
        with open(clean_file_path, "w", encoding="utf-8") as outfile:
            outfile.writelines(cleaned_lines)

        logging.info(f"Cleaned data saved to {clean_file_path}")

def main():
    clean_data()

if __name__ == "__main__":
    main()
