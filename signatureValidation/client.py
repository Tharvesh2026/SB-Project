import hmac
import hashlib
import requests

SECRET_KEY = b'privateKey'

def generate_signature(message):
    return hmac.new(
        SECRET_KEY,
        message.encode(),
        hashlib.sha1
    ).hexdigest()


message = "hello world"
signature = generate_signature(message)

url = "http://localhost:5000/api"

params = {
    "command": "encode",
    "message": message,
    "signature": signature
}

response = requests.get(url, params=params)

print(response.json())