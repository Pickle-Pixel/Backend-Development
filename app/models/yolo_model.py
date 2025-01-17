from ultralytics import YOLO

def load_model():
    try:
        # Load the YOLOv8 model (change to another model like yolov8s.pt if needed)
        model = YOLO("yolov8n.pt")  # Nano version for lightweight inference
        print("YOLOv8 model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading YOLOv8 model: {e}")
        raise
