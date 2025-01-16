from PIL import Image #Python Image Library for image manipulation

def run_detection(model, image):
    #run the model on the image
    results = model(image)
    #convert results into a dict to be sent back to user easier
    return results.pandas().xyxy[0].to_dict(orient="records")



