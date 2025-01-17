from fastapi import APIRouter, UploadFile, File
from PIL import Image
from app.services.detection_service import run_detection
from app.models.yolo_model import load_model

router = APIRouter()
model = load_model()

@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    try:
        # Open the uploaded image
        img = Image.open(file.file).convert("RGB")
        detections = run_detection(model, img)  # Run detection
        return {"detections": detections}
    except Exception as e:
        print(f"Error in /detect: {e}")
        return {"error": str(e)}
