import os
import asyncio
import logging
from telethon import TelegramClient
from config.config import TELEGRAM_API_ID, TELEGRAM_API_HASH

# Directory to store fetched data
DATA_DIR = os.path.join(os.getcwd(), "data", "fetched_data")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# List of Telegram channel URLs to scrape
CHANNELS = [
    "https://t.me/DoctorsET",
    "https://t.me/chemed",
    "https://t.me/lobelia4cosmetics",
    "https://t.me/yetenaweg",
    "https://t.me/EAHCI"
]

client = TelegramClient('session', TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def fetch_channel_data(channel_url):
    try:
        await client.start()
        # Extract the channel username from the URL
        channel_username = channel_url.rstrip('/').split('/')[-1]
        messages = await client.get_messages(channel_username, limit=100)
        file_path = os.path.join(DATA_DIR, f"{channel_username}_data.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            for message in messages:
                # Save message id, date, and text (customize as needed)
                f.write(f"{message.id}\t{message.date}\t{message.text}\n")
        logging.info(f"Fetched data from channel: {channel_username}")
    except Exception as e:
        logging.error(f"Error fetching data from {channel_url}: {e}")

async def main():
    tasks = [fetch_channel_data(channel) for channel in CHANNELS]
    await asyncio.gather(*tasks)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
