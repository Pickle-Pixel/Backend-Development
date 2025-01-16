from fastapi import APIRouter, UploadFile, File
from PIL import Image
from app.services.detection_service import run_detection
from app.models.yolo_model import load_model

router = APIRouter()
model = load_model()

@router.post("/detect")
async def detect(file: UploadFile = File(...)):  # `File(...)` is required here
    try:
        img = Image.open(file.file)  # Open the uploaded file as an image
        detections = run_detection(model, img)
        return {"detections": detections}
    except Exception as e:
        return {"error": str(e)}
