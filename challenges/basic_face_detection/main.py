import json

import cv2
import requests

IMAGE_PATH = "./challenge.jpg"

# Get image url for challenge
problem_data = requests.get(
    "https://hackattic.com/challenges/basic_face_detection/problem?access_token=802a3b5e57c7d9d7"
).content
image_url = json.loads(problem_data)["image_url"]

# Download image
with open(IMAGE_PATH, "wb") as out_fh:
    image_data = requests.get(image_url).content
    out_fh.write(image_data)

# Parse image and detect faces
img = cv2.imread(IMAGE_PATH)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
face = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

# Draw square indicators around faces for debugging purposes
for x, y, w, h in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imwrite("./solved.jpg", img_rgb)

# Calculate face positions
x_split = img_rgb.shape[0] / 8
y_split = img_rgb.shape[1] / 8
positions = []
for x, y, w, h in face:
    position = [y // y_split, x // x_split]
    position = [int(i) for i in position]
    positions.append(position)

# Send back answer
answer = json.dumps({"face_tiles": positions})
response = requests.post(
    "https://hackattic.com/challenges/basic_face_detection/solve?access_token=802a3b5e57c7d9d7",
    data=answer,
)
print(response)
print(response.content.decode("utf-8"))
