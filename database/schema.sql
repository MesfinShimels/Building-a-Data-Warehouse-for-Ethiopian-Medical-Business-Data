CREATE TABLE IF NOT EXISTS raw_scraped_data (
    id SERIAL PRIMARY KEY,
    channel_name VARCHAR(255),
    message_text TEXT,
    media_url TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS detection_results (
    id SERIAL PRIMARY KEY,
    image_path TEXT,
    detection_data JSONB,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cleaned_medical_data (
    id SERIAL PRIMARY KEY,
    business_name VARCHAR(255),
    contact_info JSONB,
    services TEXT[],
    location GEOGRAPHY(POINT),
    verified BOOLEAN DEFAULT FALSE
);