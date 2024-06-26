from pydantic import BaseModel

from src.infrastructure.config.broker import BrokerConfig
from src.infrastructure.config.db import DBConfig
from src.infrastructure.config.jwt import JWTConfig
from src.infrastructure.config_loader import read_toml


class Config(BaseModel):
    jwt_config: JWTConfig = JWTConfig(jwt_secret="secret", expiry_minutes=99)  # noqa: S106
    db_config: DBConfig = DBConfig()
    broker_config: BrokerConfig = BrokerConfig()


def create_config_obj() -> Config:
    config_data = read_toml()
    return Config(
        jwt_config=config_data["jwt"],
        db_config=config_data["db"],
        broker_config=config_data["broker"],
    )
