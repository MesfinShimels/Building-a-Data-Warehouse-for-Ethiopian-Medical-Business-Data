from fastapi import FastAPI
from .database import engine
from .models import Base
from .api.v1.endpoints import router as api_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = FastAPI(title="Medical Data Warehouse API")

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Shutting down application")