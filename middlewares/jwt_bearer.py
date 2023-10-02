from fastapi.security import HTTPBearer
from utils.jwt_manager import valid_token
from fastapi import Request,HTTPException


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) :
        auth = await super().__call__(request)
        data = valid_token(auth.credentials)
        if data["email"] != "admin@admin.com":
            raise HTTPException(status_code=403,detail="Credentials invalid")