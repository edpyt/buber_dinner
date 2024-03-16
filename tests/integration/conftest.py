from typing import AsyncGenerator, Callable, Coroutine

import pytest
from blacksheep import Application
from blacksheep.testing import TestClient
from src.api import build_api
from src.application.persistence.user_repo import IUserRepository
from src.domain.entities.user import User
from src.infrastructure.config.jwt import JWTConfig
from src.infrastructure.persistence.user_repo import UserRepository

from tests.integration.di import DIOverride, setup_test_di


@pytest.fixture(scope="session")
def jwt_config() -> JWTConfig:
    return JWTConfig(jwt_secret="test-secret", expiry_minutes=0)


@pytest.fixture(name="app", scope="session")
def create_app(jwt_config: JWTConfig) -> Application:
    app: Application = build_api()
    setup_test_di(app, DIOverride(jwt_config))
    return app


@pytest.fixture(name="user_repo")
async def create_user_repository() -> IUserRepository:
    return UserRepository()


@pytest.fixture
async def test_client(
    app: Application,
    user_repo: IUserRepository,
) -> AsyncGenerator[TestClient, None]:
    setup_test_di(app, DIOverride(user_repo, IUserRepository))
    await app.start()
    client: TestClient = TestClient(app)
    return client


@pytest.fixture
def create_user_factory(
    user_repo: UserRepository,
) -> Callable[[str, str, str, str], Coroutine[User, None, None]]:
    async def create_user(first_name: str, last_name: str, email: str, password: str) -> User:
        nonlocal user_repo

        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        await user_repo.add(user)

    return create_user
