from flask import Flask, jsonify, request

app = Flask(__name__)

data_store = {}


@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="UP"), 200


@app.route("/data", methods=["POST"])
def set_data():
    payload = request.get_json()

    if not payload or "key" not in payload or "value" not in payload:
        return jsonify(error="key and value are required"), 400

    data_store[payload["key"]] = payload["value"]

    return jsonify(
        message="Data stored successfully",
        key=payload["key"],
        value=payload["value"],
    ), 201


@app.route("/data/<key>", methods=["GET"])
def get_data(key):
    if key not in data_store:
        return jsonify(error="Key not found"), 404

    return (
        jsonify(
            key=key,
            value=data_store[key],
        ),
        200,
    )
