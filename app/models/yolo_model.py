import torch #library for deep learning

def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s') #load the model

