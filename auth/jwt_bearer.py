# this function for check the request. it authorized or not 
  
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth.jwt import decodeJWT

class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)
    
    async def __call__(self, request: Request):
        credentials : HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid or Expired token")
            return credentials.credentials
        else: 
            raise HTTPException(status_code=403, detail="Invalid or Expired token")
    
    def verify(self, jwtoken: str):
        payload = decodeJWT(jwtoken)
        return payload is not None
