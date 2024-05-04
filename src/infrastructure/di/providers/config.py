from dishka import Provider, Scope, provide

from src.infrastructure.config.broker import BrokerConfig
from src.infrastructure.config.config import Config, create_config_obj
from src.infrastructure.config.db import DBConfig
from src.infrastructure.config.jwt import JWTConfig


class ConfigProvider(Provider):
    scope = Scope.APP

    config = provide(create_config_obj, provides=Config)
    jwt_config = provide(Config.jwt_config, provides=JWTConfig)
    db_config = provide(Config.db_config, provides=DBConfig)
    broker_config = provide(Config.broker_config, provides=BrokerConfig)
