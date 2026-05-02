from flask import Flask, request, jsonify
import hmac
import hashlib
import base64

app = Flask(__name__)

SECRET_KEY = b'privateKey'


def generate_signature(message: str) -> str:
    return hmac.new(
        SECRET_KEY,
        message.encode(),
        hashlib.sha1
    ).hexdigest()


def secure_compare(sig1, sig2):
    return hmac.compare_digest(sig1, sig2)


@app.route('/api', methods=['GET'])
def api():
    command = request.args.get('command')
    message = request.args.get('message')
    signature = request.args.get('signature')

    if not command or not message or not signature:
        return jsonify({"error": "Missing parameters"}), 400

    # Verify signature
    expected_signature = generate_signature(message)

    if not secure_compare(signature, expected_signature):
        return jsonify({"error": "Invalid signature"}), 403

    try:
        if command == "encode":
            encoded = base64.b64encode(message.encode()).decode()
            return jsonify({"result": encoded})

        elif command == "decode":
            decoded = base64.b64decode(message.encode()).decode()
            return jsonify({"result": decoded})

        else:
            return jsonify({"error": "Invalid command"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)