import hmac
import hashlib
import base64
import urllib.parse
import requests

API_KEY = "APIKEY123"
SECRET_KEY = "SECRET123"


def generate_signature(params):
    sorted_items = sorted(params.items(), key=lambda item: item[0].lower())

    query_parts = []

    for key, value in sorted_items:
        k = key.lower()
        v = urllib.parse.quote_plus(str(value)).lower()
        pair = k + "=" + v
        query_parts.append(pair)

    query_string = "&".join(query_parts)

    secret_bytes = SECRET_KEY.encode("utf-8")
    message_bytes = query_string.encode("utf-8")

    digest = hmac.new(secret_bytes, message_bytes, hashlib.sha1).digest()

    signature = base64.b64encode(digest).decode("utf-8")

    encoded_signature = urllib.parse.quote_plus(signature)

    return encoded_signature


def send_request(command, message):
    params = {}
    params["command"] = command
    params["message"] = message
    params["apikey"] = API_KEY

    signature = generate_signature(params)
    params["signature"] = signature

    response = requests.get("http://localhost:5000/client/api", params=params)

    return response.json()


print(send_request("encode", "hello"))
print(send_request("decode", "aGVsbG8="))