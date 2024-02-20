import json

import cv2
import requests

ACCESS_TOKEN = "802a3b5e57c7d9d7"
QR_CODE_FILE = "qr_code.png"

# Get QR code image url to download
data = requests.get(
    f"https://hackattic.com/challenges/reading_qr/problem?access_token={ACCESS_TOKEN}"
).content
data = json.loads(data)
image_url = data["image_url"]

# Download image and save file
with open(QR_CODE_FILE, "wb") as out_fh:
    out_fh.write(requests.get(image_url).content)

# Read value from QR code
img = cv2.imread(QR_CODE_FILE)
detect = cv2.QRCodeDetector()
value, points, straight_qrcode = detect.detectAndDecode(img)
print(value.strip())

# Submit back to endpoint
solution_data = json.dumps({"code": value})
response = requests.post(
    f"https://hackattic.com/challenges/reading_qr/solve?access_token={ACCESS_TOKEN}",
    data=solution_data,
)
print(response.content.decode("utf-8"))
