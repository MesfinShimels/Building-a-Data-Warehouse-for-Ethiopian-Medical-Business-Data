from telethon.sync import TelegramClient
import json
import os

# Telegram API credentials
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
PHONE_NUMBER = 'your_phone_number'

# Target channels
CHANNELS = [
    'DoctorsET', 'lobelia4cosmetics', 'yetenaweg', 'EAHCI'
]

# Output directory
OUTPUT_DIR = 'data_scraping/raw_data'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Start client
client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

async def scrape_telegram():
    await client.start()
    for channel in CHANNELS:
        messages = []
        async for message in client.iter_messages(channel, limit=100):
            messages.append({
                'id': message.id,
                'text': message.text,
                'date': str(message.date),
                'media': bool(message.media)
            })
        # Save messages to JSON file
        with open(f"{OUTPUT_DIR}/{channel}.json", "w") as f:
            json.dump(messages, f, indent=4)

    await client.disconnect()

with client:
    client.loop.run_until_complete(scrape_telegram())
