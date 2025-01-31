CREATE TABLE medical_business (
    id SERIAL PRIMARY KEY,
    message_id INT,
    text TEXT,
    date TIMESTAMP,
    media BOOLEAN
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    message_id INT REFERENCES medical_business(message_id),
    image_path TEXT
);
