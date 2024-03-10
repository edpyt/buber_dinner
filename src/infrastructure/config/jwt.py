from dataclasses import dataclass


@dataclass(frozen=True)
class JWTConfig:
    jwt_secret: str
    expiry_minutes: int
