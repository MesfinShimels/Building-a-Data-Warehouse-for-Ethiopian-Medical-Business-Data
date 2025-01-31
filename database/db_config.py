import psycopg2
import pandas as pd

DB_CONFIG = {
    "dbname": "medical_db",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}

def insert_data(df, table):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(f"""
            INSERT INTO {table} (message_id, text, date, media) 
            VALUES (%s, %s, %s, %s)
        """, (row["id"], row["text"], row["date"], row["media"]))
    
    conn.commit()
    cur.close()
    conn.close()

df = pd.read_csv('data_cleaning/cleaned_data.csv')
insert_data(df, 'medical_business')
