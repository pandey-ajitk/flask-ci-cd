from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store (for demo purposes only)
data_store = {}

# 1. Health Check API
@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="UP"), 200


# 2. SET API (Create / Update)
@app.route("/data", methods=["POST"])
def set_data():
    payload = request.get_json()

    if not payload or "key" not in payload or "value" not in payload:
        return jsonify(error="key and value are required"), 400

    key = payload["key"]
    value = payload["value"]

    data_store[key] = value

    return jsonify(
        message="Data stored successfully",
        key=key,
        value=value
    ), 201


# 3. GET API (Read)
@app.route("/data/<key>", methods=["GET"])
def get_data(key):
    if key not in data_store:
        return jsonify(error="Key not found"), 404

    return jsonify(
        key=key,
        value=data_store[key]
    ), 200
