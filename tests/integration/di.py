from blacksheep import Application
from src.infrastructure.config.jwt import JWTConfig


def setup_test_di(app: Application, jwt_config: JWTConfig) -> None:
    del app.services._map[JWTConfig]  # noqa: SLF001
    app.services.add_instance(jwt_config)
