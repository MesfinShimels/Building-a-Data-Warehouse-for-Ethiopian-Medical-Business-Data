# api/crud.py

from sqlalchemy.orm import Session
from api import models, schemas

def get_message(db: Session, message_id: int):
    return db.query(models.TelegramMessage).filter(models.TelegramMessage.message_id == message_id).first()

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TelegramMessage).offset(skip).limit(limit).all()

def create_message(db: Session, message: schemas.TelegramMessageCreate):
    db_message = models.TelegramMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_detections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ObjectDetection).offset(skip).limit(limit).all()

def create_detection(db: Session, detection: schemas.ObjectDetectionCreate):
    db_detection = models.ObjectDetection(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection
