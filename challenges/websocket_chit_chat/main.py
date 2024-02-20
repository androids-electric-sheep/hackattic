import asyncio
import json
import time

import requests
from websockets.sync.client import connect

INTERVALS = [0.7, 1.5, 2, 2.5, 3]

# Get websocket token
problem_data = requests.get(
    "https://hackattic.com/challenges/websocket_chit_chat/problem?access_token=802a3b5e57c7d9d7"
).content
token = json.loads(problem_data)["token"]


def main():
    round = 0
    with connect(f"wss://hackattic.com/_/ws/{token}") as websocket:
        last = time.time()
        _ = websocket.recv()  # Clear introduction message
        while True:
            message = websocket.recv()
            current = time.time()
            diff = current - last

            # Calculate proximity
            interval = min(INTERVALS, key=lambda x: abs(x - diff))
            print(f"Difference: {diff}")
            print(f"Detected interval: {interval}")
            answer = str(int(interval * 1000))
            websocket.send(answer)
            response = websocket.recv()

            # Check for end condition
            if "congratulations" in response:
                secret = response.split('"')[1]
                print(f"Secret: {secret}")
                response = requests.post(
                    "https://hackattic.com/challenges/websocket_chit_chat/solve?access_token=802a3b5e57c7d9d7",
                    data=json.dumps({"secret": secret}),
                )
                print(response)
                print(response.content.decode("utf-8"))
                return

            print(response)
            last = current


main()
