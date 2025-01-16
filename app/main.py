from fastapi import FastAPI
from app.routes.detection import router as detector_router

app = FastAPI()

app.include_router(detector_router)


@app.get("/")
def root():
    return {"message": "YOLO API is Running!"}