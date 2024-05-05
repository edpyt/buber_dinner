from dishka import Provider, Scope, provide

from src.infrastructure.config.broker import BrokerConfig
from src.infrastructure.config.config import Config, create_config_obj
from src.infrastructure.config.db import DBConfig
from src.infrastructure.config.jwt import JWTConfig


class ConfigProvider(Provider):
    scope = Scope.APP

    config = provide(create_config_obj, provides=Config)

    @provide
    def jwt_config(self, config: Config) -> JWTConfig:
        return config.jwt_config

    @provide
    def db_config(self, config: Config) -> DBConfig:
        return config.db_config

    @provide
    def broker_config(self, config: Config) -> BrokerConfig:
        return config.broker_config
