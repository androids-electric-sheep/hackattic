import base64
import gzip
import json

import requests

ACCESS_TOKEN = "802a3b5e57c7d9d7"

# Get problem data
data = requests.get(
    f"https://hackattic.com/challenges/backup_restore/problem?access_token={ACCESS_TOKEN}"
).content
problem_data = json.loads(data)
encoded_dump = problem_data["dump"]
dump = base64.b64decode(encoded_dump)
decoded_dump = gzip.decompress(dump)

# Get alive ssns in sql
sql_lines = decoded_dump.split(b"\n")
alive_lines = [i for i in sql_lines if b"alive" in i]
ssns = [i.decode("utf-8").split("\t")[3] for i in alive_lines]
print(ssns)

# Send answer back to endpoint
solution_data = json.dumps({"alive_ssns": ssns})
response = requests.post(
    f"https://hackattic.com/challenges/backup_restore/solve?access_token={ACCESS_TOKEN}",
    data=solution_data,
)
print(response.content.decode("utf-8"))
