import itertools
import json
import string
import zipfile

import requests

ZIP_FILE = './challenge.zip'

# Get problem data
problem_data = requests.get('https://hackattic.com/challenges/brute_force_zip/problem?access_token=802a3b5e57c7d9d7').content
zip_url = json.loads(problem_data)['zip_url']

# Download zip file
with open(ZIP_FILE, 'wb') as out_fh:
    zip_data = requests.get(zip_url).content
    out_fh.write(zip_data)

for length in range(4,7):
    passwords = itertools.combinations(string.ascii_lowercase + string.digits, length)
    for password in passwords:
        try:
            password = bytes(''.join(password).encode('utf-8'))
            print(password)
            zip = zipfile.ZipFile(ZIP_FILE)
            file = zip.open('secret.txt', 'r', pwd=password)
            print(file.read())
        except RuntimeError:
            continue
        except Exception as e:
            continue
        
