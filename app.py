import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify(message="Flask backend running on AWS App Runner")

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok")

@app.route("/echo", methods=["POST"])
def echo():
    payload = request.get_json(silent=True) or {}
    return jsonify(received=payload)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
