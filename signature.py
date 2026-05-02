API_KEY = "40PS7t5FhVUKO6TDS4d7oiSQQOSuQSbUstUtBBDV6Rgc7boney-UKbag4afG58Rz64B_es5O7xkTEB2rQSeJ4w";
SECRET_KEY = "aJkbbL095FGaNSPaVKjMeKz_QQxDShmbAcQ3aqCBsGGdY_l0e2aJskw5_QqypjiJlJ6xpzv5huH23_nvD1Jt1A";
BASE_URL = "http://108.62.3.216:8081/client/api";

import hashlib
import hmac
import base64
import urllib.parse

import urllib.parse
import hmac
import hashlib
import base64


def sign(params, secret_key):
    sorted_params = sorted(params.items(), key=lambda item: item[0].lower())

    encoded_parts = []

    for key, value in sorted_params:
        str_value = str(value)

        encoded_value = urllib.parse.quote_plus(str_value)
        encoded_value = encoded_value.replace("+", "%20")

        part = f"{key}={encoded_value}"
        encoded_parts.append(part)

    query_string = "&".join(encoded_parts)
    query_string = query_string.lower()

    secret_bytes = secret_key.encode("utf-8")
    message_bytes = query_string.encode("utf-8")

    digest = hmac.new(secret_bytes, message_bytes, hashlib.sha1).digest()

    signature = base64.b64encode(digest).decode("utf-8")

    final_signature = urllib.parse.quote_plus(signature)

    return final_signature


def build_query_string(params):
    parts = []

    for key, value in params.items():
        str_value = str(value)
        encoded_value = urllib.parse.quote_plus(str_value)
        parts.append(f"{key}={encoded_value}")

    return "&".join(parts)


def call_cloudstack(params):
    params["apikey"] = API_KEY
    params["response"] = "json"

    signature = sign(params, SECRET_KEY)

    query_string = build_query_string(params)

    url = BASE_URL + "?" + query_string + "&signature=" + signature

    print("\nFINAL API URL:\n")
    print(url)


createUser = {
    "command": "createUser",
    "username": "test",
    "password": "Test@12345",
    "firstname": "Test",
    "lastname": "1",
    "email": "testuser1@mail.com",
    "account": "admin",
    "domainid": "5aa8563d-ba33-11f0-ad56-d2085c6e6ed0"
}

deleteUser = {
    "command": "deleteUser",
    "id": "ef34fdd9-cef0-49ff-98ef-441427560b0d"
}

call_cloudstack(createUser)