from flask import Flask, request, jsonify
import hmac
import hashlib
import base64
import urllib.parse

app = Flask(__name__)

API_USERS = {
    "APIKEY123": "SECRET123",
    "APIKEY456": "SECRET456"
}

def generate_signature(params, secret_key):
    clean_params = {}

    for key in params:
        if key.lower() != "signature":
            clean_params[key] = params[key]

    sorted_items = sorted(clean_params.items(), key=lambda item: item[0].lower())

    query_parts = []
    for key, value in sorted_items:
        k = key.lower()
        v = urllib.parse.quote_plus(str(value)).lower()
        pair = k + "=" + v
        query_parts.append(pair)

    query_string = "&".join(query_parts)

    secret_bytes = secret_key.encode("utf-8")
    message_bytes = query_string.encode("utf-8")

    digest = hmac.new(secret_bytes, message_bytes, hashlib.sha1).digest()

    signature = base64.b64encode(digest).decode("utf-8")

    return signature


@app.route("/client/api", methods=["GET"])
def api():
    params = request.args.to_dict()

    api_key = params.get("apikey")
    user_signature = params.get("signature")

    if api_key is None or user_signature is None:
        return jsonify({"error": "missing apikey or signature"})

    if api_key not in API_USERS:
        return jsonify({"error": "invalid apikey"})

    secret_key = API_USERS[api_key]

    expected_signature = generate_signature(params, secret_key)

    decoded_signature = urllib.parse.unquote_plus(user_signature)

    if not hmac.compare_digest(decoded_signature, expected_signature):
        return jsonify({"error": "signature mismatch"})

    command = params.get("command")
    message = params.get("message")

    if command == "encode":
        message_bytes = message.encode("utf-8")
        encoded_bytes = base64.b64encode(message_bytes)
        encoded_text = encoded_bytes.decode("utf-8")

        return jsonify({"result": encoded_text})

    elif command == "decode":
        message_bytes = message.encode("utf-8")
        decoded_bytes = base64.b64decode(message_bytes)
        decoded_text = decoded_bytes.decode("utf-8")

        return jsonify({"result": decoded_text})

    else:
        return jsonify({"error": "invalid command"})


if __name__ == "__main__":
    app.run(port=5000)