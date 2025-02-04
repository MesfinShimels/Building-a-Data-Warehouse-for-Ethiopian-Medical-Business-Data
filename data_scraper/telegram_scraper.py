# data_scraper/telegram_scraper.py

import os
import logging
from telethon import TelegramClient, errors
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_CHANNELS, RAW_DATA_PATH

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Ensure the raw data directory exists
os.makedirs(RAW_DATA_PATH, exist_ok=True)

def scrape_channel(client, channel):
    try:
        # Fetch the latest 100 messages from the channel
        messages = client.get_messages(channel, limit=100)
        logging.info(f"Fetched {len(messages)} messages from channel: {channel}")

        # Save messages to a file (one file per channel)
        file_path = os.path.join(RAW_DATA_PATH, f"{channel}_messages.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            for message in messages:
                # Write basic info; extend as needed for your data warehouse
                f.write(f"{message.id}\t{message.date}\t{message.text}\n")

        logging.info(f"Data saved to {file_path}")

    except errors.RPCError as e:
        logging.error(f"Error fetching messages from {channel}: {e}")

def main():
    # Create a Telegram client session
    client = TelegramClient("kara_solutions_session", TELEGRAM_API_ID, TELEGRAM_API_HASH)
    client.start()
    logging.info("Telegram client started.")

    # Loop over the list of channels to scrape data
    for channel in TELEGRAM_CHANNELS:
        logging.info(f"Scraping channel: {channel}")
        scrape_channel(client, channel)

    client.disconnect()
    logging.info("Telegram client disconnected.")

if __name__ == "__main__":
    main()
