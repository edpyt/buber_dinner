from typing import AsyncGenerator

import pytest
from blacksheep import Application
from pytest_mock import MockerFixture
from src.api.main import build_api
from src.infrastructure.config.broker import BrokerConfig
from src.infrastructure.config.config import Config
from src.infrastructure.config.db import DBConfig
from src.infrastructure.config.jwt import JWTConfig


@pytest.fixture(name="jwt_config", scope="session")
def create_jwt_config() -> JWTConfig:
    return JWTConfig(jwt_secret="test-secret", expiry_minutes=9999)


@pytest.fixture(name="config", scope="session", autouse=True)
def create_config(
    session_mocker: MockerFixture,
    jwt_config: JWTConfig,
    db_config: DBConfig,
    broker_config: BrokerConfig,
) -> Config:
    config = Config(
        jwt_config=jwt_config,
        db_config=db_config,
        broker_config=broker_config,
    )

    session_mocker.patch("src.infrastructure.config.config.create_config_obj", return_value=config)
    session_mocker.patch("src.infrastructure.di.config.create_config_obj", return_value=config)

    return config


@pytest.fixture(name="app", scope="session")
async def create_app(jwt_config: JWTConfig) -> AsyncGenerator[Application, None]:
    app: Application = build_api()

    await app.start()
    yield app
    await app.stop()
