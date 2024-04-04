from typing import AsyncGenerator, Callable, Coroutine

import pytest
from blacksheep import Application, JSONContent
from blacksheep.testing import TestClient
from src.api import build_api
from src.application.dto.user import UserDTO
from src.application.persistence.user_repo import UserRepository
from src.infrastructure.config.jwt import JWTConfig
from src.infrastructure.persistence.user_repo import UserRepositoryImpl

from tests.integration.di import DIOverride, setup_test_di


@pytest.fixture(scope="session")
def jwt_config() -> JWTConfig:
    return JWTConfig(jwt_secret="test-secret", expiry_minutes=0)


@pytest.fixture(name="app", scope="session")
async def create_app(jwt_config: JWTConfig) -> AsyncGenerator[Application, None]:
    app: Application = build_api()
    setup_test_di(app, DIOverride(jwt_config))
    await app.start()
    yield app
    await app.stop()


@pytest.fixture(name="user_repo")
async def create_user_repository() -> AsyncGenerator[UserRepository, None]:
    user_repo = UserRepositoryImpl()
    yield user_repo
    user_repo.users.clear()


@pytest.fixture
def test_client(
    app: Application,
    user_repo: UserRepository,
) -> TestClient:
    setup_test_di(app, DIOverride(user_repo, UserRepository))
    client: TestClient = TestClient(app)
    return client


@pytest.fixture(name="token")
async def create_auth_token(test_client: TestClient) -> str:
    auth_response = await test_client.post(
        "/auth/register",
        content=JSONContent(
            {
                "first_name": "Amichai",
                "last_name": "Mantinband",
                "email": "amichai@mantinband.com",
                "password": "Amiko1232!",
            },
        ),
    )
    return (await auth_response.json())["token"]


@pytest.fixture
def create_user_factory(
    user_repo: UserRepository,
) -> Callable[[str, str, str, str], Coroutine[UserDTO, None, None]]:
    async def create_user(first_name: str, last_name: str, email: str, password: str) -> UserDTO:
        nonlocal user_repo

        user = UserDTO.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        await user_repo.add(user)

    return create_user
