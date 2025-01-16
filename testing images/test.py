import requests

url = "http://127.0.0.1:8000/detect"

# Replace with the path to your image file
image_path = "isthisahat.png"

# Open the file and send it as form-data
with open(image_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print(response.json())
