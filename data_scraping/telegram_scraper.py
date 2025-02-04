import os
import logging
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    filename=os.getenv('SCRAPING_LOG_PATH'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

async def scrape_channel(channel_handle):
    client = TelegramClient(
        'session', 
        int(os.getenv('API_ID')), 
        os.getenv('API_HASH')
    )
    
    await client.start(os.getenv('PHONE'))
    
    try:
        channel = await client.get_entity(channel_handle)
        messages = await client.get_messages(channel, limit=100)
        
        scraped_data = []
        for msg in messages:
            data = {
                'date': msg.date,
                'text': msg.text,
                'media': bool(msg.media),
                'author': msg.post_author
            }
            scraped_data.append(data)
            logging.info(f"Scraped message: {msg.id}")
            
        return scraped_data
        
    except Exception as e:
        logging.error(f"Error scraping {channel_handle}: {str(e)}")
    finally:
        await client.disconnect()