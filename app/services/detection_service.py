def run_detection(model, image):
    try:
        # Run the YOLOv8 model
        results = model.predict(source=image, save=False)
        print("Raw YOLOv8 results:", results)  # Debug log

        # Parse results
        detections = []
        for box in results[0].boxes:  # Iterate over detected boxes
            detections.append({
                "label": model.names[int(box.cls)],  # Class name
                "confidence": float(box.conf),      # Confidence score
                "box": [float(x) for x in box.xyxy[0]]  # Bounding box coordinates
            })

        return detections
    except Exception as e:
        print(f"Error during detection: {e}")
        raise
