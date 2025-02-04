# api/schemas.py

from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class TelegramMessageBase(BaseModel):
    message_id: int
    date: datetime
    text: Optional[str] = None

class TelegramMessageCreate(TelegramMessageBase):
    pass

class TelegramMessage(TelegramMessageBase):
    id: int

    class Config:
        orm_mode = True

class Detection(BaseModel):
    bbox: List[int]
    confidence: float
    class_: int

class ObjectDetectionBase(BaseModel):
    image_name: str
    detections: List[Detection]

class ObjectDetectionCreate(ObjectDetectionBase):
    pass

class ObjectDetection(ObjectDetectionBase):
    id: int

    class Config:
        orm_mode = True
