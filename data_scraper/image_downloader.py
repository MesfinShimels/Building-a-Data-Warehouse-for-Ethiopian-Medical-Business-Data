import os
from telethon.sync import TelegramClient

API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
PHONE_NUMBER = 'your_phone_number'

IMAGE_DIR = "data_scraping/images"
os.makedirs(IMAGE_DIR, exist_ok=True)

CHANNELS = ['lobelia4cosmetics', 'DoctorsET']

client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

async def download_images():
    await client.start()
    for channel in CHANNELS:
        async for message in client.iter_messages(channel, limit=50):
            if message.media:
                file_path = await message.download_media(file=IMAGE_DIR)
                print(f"Downloaded: {file_path}")
    await client.disconnect()

with client:
    client.loop.run_until_complete(download_images())
