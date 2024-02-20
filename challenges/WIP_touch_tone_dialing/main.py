import json

import requests

WAV_FILE_PATH = "./challenge.wav"


def decode_dtfm(filename: str) -> str:
    raise NotImplementedError("Finish this")


# Get link to WAV file
problem_data = requests.get(
    "https://hackattic.com/challenges/touch_tone_dialing/problem?access_token=802a3b5e57c7d9d7"
).content
wav_url = json.loads(problem_data)["wav_url"]

# Get WAV file data
with open(WAV_FILE_PATH, "wb") as out_fh:
    wav_data = requests.get(wav_url).content
    out_fh.write(wav_data)

# Get answer and send to endpoint
answer = decode_dtfm(WAV_FILE_PATH)
response = requests.post(
    "https://hackattic.com/challenges/touch_tone_dialing/solve?access_token=802a3b5e57c7d9d7",
    data=json.dumps({"sequence": answer}),
)
print(response)
print(response.content.decode("utf-8"))
