# api/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from api import models, schemas, crud
from api.database import SessionLocal, engine
import uvicorn

# Create all database tables (if not exist)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ethiopian Medical Business Data API")

# Dependency: get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ethiopian Medical Business Data API"}

@app.get("/messages/", response_model=list[schemas.TelegramMessage])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = crud.get_messages(db, skip=skip, limit=limit)
    return messages

@app.post("/messages/", response_model=schemas.TelegramMessage)
def create_message(message: schemas.TelegramMessageCreate, db: Session = Depends(get_db)):
    db_message = crud.get_message(db, message.message_id)
    if db_message:
        raise HTTPException(status_code=400, detail="Message already exists")
    return crud.create_message(db, message)

@app.get("/detections/", response_model=list[schemas.ObjectDetection])
def read_detections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    detections = crud.get_detections(db, skip=skip, limit=limit)
    return detections

@app.post("/detections/", response_model=schemas.ObjectDetection)
def create_detection(detection: schemas.ObjectDetectionCreate, db: Session = Depends(get_db)):
    return crud.create_detection(db, detection)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
