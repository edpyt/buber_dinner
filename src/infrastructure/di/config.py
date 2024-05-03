from rodi import Container

from src.infrastructure.config.config import Config, create_config_obj


def setup_config_di(di_container: Container) -> Config:
    config = create_config_obj()

    di_container.add_instance(config)
    di_container.add_instance(config.jwt_config)
    di_container.add_instance(config.db_config)
    di_container.add_instance(config.broker_config)

    return config
