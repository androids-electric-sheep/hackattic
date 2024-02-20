import json
import pathlib
import glob
import os

import requests

ACCESS_TOKEN = '802a3b5e57c7d9d7'

for file in glob.glob('/srv/tftp/*.txt'):
    print(f'Removing {file}')
    os.unlink(file)

problem_data = requests.get(f'https://hackattic.com/challenges/trivial_filing/problem?access_token={ACCESS_TOKEN}').content
problem_files = json.loads(problem_data)['files']

for file, content in problem_files.items():
    target_file = pathlib.Path('/srv/tftp', file)
    print(f'Creating {target_file}')
    with open(target_file, 'w') as out_fh:
        out_fh.write(content)

print('Triggering request')
response = requests.post(f'https://hackattic.com/challenges/trivial_filing/solve?access_token={ACCESS_TOKEN}', data=json.dumps({'tftp_host': '159.65.89.215', 'tftp_port': '69'}))
print('Interpreting response')
print(response)
print(response.content.decode('utf-8'))
