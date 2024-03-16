from pydantic import BaseModel


class JWTConfig(BaseModel):
    jwt_secret: str
    expiry_minutes: int
