import json

import jwt
import requests
from flask import Flask, jsonify, request

# Get jwt_secret for validating requests
problem_content = requests.get(
    "https://hackattic.com/challenges/jotting_jwts/problem?access_token=802a3b5e57c7d9d7"
).content
jwt_secret = json.loads(problem_content)["jwt_secret"]

# Setup flask app to respond to requests
app = Flask(__name__)
count = 0
total = ""


@app.route("/", methods=["POST"])
def index():
    global total
    global count
    if count == 0:  # Manually trigger readiness once server is up and running
        # Send endpoint to server to start requests
        count += 1
        response = requests.post(
            "https://hackattic.com/challenges/jotting_jwts/solve?access_token=802a3b5e57c7d9d7",
            data=json.dumps({"app_url": "http://46.101.86.250:5000"}),
        )
        return {}, 200

    token = request.data.decode("utf-8")

    # Validate token and append if correct
    try:
        decoded_token = jwt.decode(
            token,
            key=jwt_secret,
            algorithms=[
                "HS256",
            ],
        )
        if "append" not in decoded_token:
            # We should be done
            return jsonify({"solution": total})
        total += decoded_token["append"]
    except:
        return {}, 200
    return {}, 200
