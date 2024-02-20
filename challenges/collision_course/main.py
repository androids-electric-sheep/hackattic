import base64
import json
import os

import requests

PREFIX_FILE = './chosen_prefix.txt'

# Get problem data
problem_data = requests.get('https://hackattic.com/challenges/collision_course/problem?access_token=802a3b5e57c7d9d7').content
include_string = json.loads(problem_data)['include']

with open(PREFIX_FILE, 'w') as out_fh:
    out_fh.write(include_string)

# run md5_fastcoll
os.system(f'./hashclash/bin/md5_fastcoll -p {PREFIX_FILE} -o first.txt second.txt')

contents = []
for filename in ('first.txt', 'second.txt'):
    with open(filename, 'rb') as in_fh:
        data = in_fh.read()
        data = base64.b64encode(data).decode('utf-8')
        contents.append(data)

answer = json.dumps({'files': contents})
response = requests.post('https://hackattic.com/challenges/collision_course/solve?access_token=802a3b5e57c7d9d7', data=answer)
print(response)
print(response.content.decode('utf-8'))
