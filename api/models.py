# api/models.py

from sqlalchemy import Column, Integer, String, DateTime, Float, JSON
from api.database import Base

class TelegramMessage(Base):
    __tablename__ = "telegram_messages"
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, unique=True, index=True)
    date = Column(DateTime)
    text = Column(String)

class ObjectDetection(Base):
    __tablename__ = "object_detections"
    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    detections = Column(JSON)  # Storing detection data as JSON
