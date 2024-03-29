from pathlib import Path

from pydantic import BaseModel

from src.infrastructure.config.jwt import JWTConfig
from src.infrastructure.config_loader import read_toml


class Config(BaseModel):
    jwt_config: JWTConfig


def create_config() -> Config:
    config_data = read_toml(Path("./config_dist/config.toml"))
    jwt_config = JWTConfig(**config_data["jwt_settings"])
    return Config(jwt_config=jwt_config)
