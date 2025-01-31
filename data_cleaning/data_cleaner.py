import pandas as pd
import json
import os

INPUT_DIR = 'data_scraping/raw_data'
OUTPUT_FILE = 'data_cleaning/cleaned_data.csv'

def clean_text(text):
    return text.replace("\n", " ").strip() if text else ""

# Read and clean JSON files
data = []
for file in os.listdir(INPUT_DIR):
    with open(os.path.join(INPUT_DIR, file), "r") as f:
        messages = json.load(f)
        for msg in messages:
            data.append({
                "id": msg["id"],
                "text": clean_text(msg["text"]),
                "date": msg["date"],
                "media": msg["media"]
            })

# Convert to DataFrame and clean data
df = pd.DataFrame(data)
df.drop_duplicates(inplace=True)
df.to_csv(OUTPUT_FILE, index=False)
print(f"Cleaned data saved to {OUTPUT_FILE}")
