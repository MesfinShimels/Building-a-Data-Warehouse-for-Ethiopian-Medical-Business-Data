import os
import logging

# Directories for raw and cleaned data
RAW_DATA_DIR = os.path.join(os.getcwd(), "data", "fetched_data")
CLEAN_DATA_DIR = os.path.join(os.getcwd(), "data", "cleaned_data")
if not os.path.exists(CLEAN_DATA_DIR):
    os.makedirs(CLEAN_DATA_DIR)

def clean_line(line):
    # Basic cleaning: remove extra spaces and newline characters
    return line.strip()

def process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
        # Remove blank lines and clean each line
        cleaned_lines = [clean_line(line) for line in lines if line.strip()]
        output_file = os.path.join(CLEAN_DATA_DIR, os.path.basename(file_path))
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write("\n".join(cleaned_lines))
        logging.info(f"Processed and cleaned file: {file_path}")
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")

def process_all_files():
    for file_name in os.listdir(RAW_DATA_DIR):
        if file_name.endswith("_data.txt"):
            process_file(os.path.join(RAW_DATA_DIR, file_name))

if __name__ == "__main__":
    process_all_files()
