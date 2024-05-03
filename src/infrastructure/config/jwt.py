from dataclasses import dataclass


@dataclass
class JWTConfig:
    jwt_secret: str
    expiry_minutes: int
