import time
import jwt
from decouple import config
import os

JWT_SECRET = os.getenv("secret")
JWT_ALGORITHM = os.getenv("algorithm")


# Return Genenrate token
def token_response(token: str):
    return{
        "access token": token
    }
    
# For signing in JWT
def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm = JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm = JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}