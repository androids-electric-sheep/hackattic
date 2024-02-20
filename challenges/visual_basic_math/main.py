import json

import cv2
import easyocr
import pytesseract
import requests

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
IMAGE_FILE = './challenge.png'

# Get problem data
problem_data = requests.get('https://hackattic.com/challenges/visual_basic_math/problem?access_token=802a3b5e57c7d9d7').content
image_url = json.loads(problem_data)['image_url']

# Get image file
with open(IMAGE_FILE, 'wb') as out_fh:
    image_data = requests.get(image_url).content
    out_fh.write(image_data)

reader = easyocr.Reader(['en'])
text_pieces = [i[-2].replace(' ', '') for i in reader.readtext(IMAGE_FILE, decoder='wordbeamsearch', allowlist='0123456789-+x÷', text_threshold=0.9)]
print(text_pieces)
