-- Create table for Telegram messages
CREATE TABLE IF NOT EXISTS telegram_messages (
    id SERIAL PRIMARY KEY,
    message_id INTEGER UNIQUE NOT NULL,
    channel VARCHAR(255),
    message_date TIMESTAMP,
    message_text TEXT
);

-- Create table for YOLO object detections
CREATE TABLE IF NOT EXISTS object_detections (
    id SERIAL PRIMARY KEY,
    image_name VARCHAR(255),
    detections JSONB,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
