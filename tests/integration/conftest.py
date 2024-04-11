from typing import AsyncGenerator, Callable, Coroutine, Generator

import pytest
from blacksheep import Application, JSONContent
from blacksheep.testing import TestClient
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from src.api.main import build_api
from src.application.dto.user import UserDTO
from src.application.persistence.menu_repo import MenuRepository
from src.application.persistence.user_repo import UserRepository
from src.infrastructure.config.db import DBConfig
from src.infrastructure.config.jwt import JWTConfig
from src.infrastructure.persistence.repositories.menu_repo import MenuRepositoryImpl
from src.infrastructure.persistence.repositories.user_repo import UserRepositoryImpl
from testcontainers.clickhouse import ClickHouseContainer

from tests.integration.di import DIOverride, setup_test_di


@pytest.fixture(name="clickhouse_db", scope="session")
def create_clickhouse_db() -> Generator[ClickHouseContainer, None, None]:
    with ClickHouseContainer() as ch:
        yield ch


@pytest.fixture(name="db_config", scope="session")
def create_db_config(clickhouse_db: ClickHouseContainer) -> DBConfig:
    return DBConfig(
        user="test",
        database="test",
        password="test",
        port=clickhouse_db.get_exposed_port(clickhouse_db.port),
    )


@pytest.fixture(name="jwt_config", scope="session")
def create_jwt_config() -> JWTConfig:
    return JWTConfig(jwt_secret="test-secret", expiry_minutes=0)


@pytest.fixture(name="app", scope="session")
async def create_app(
    jwt_config: JWTConfig,
    clickhouse_db: ClickHouseContainer,
) -> AsyncGenerator[Application, None]:
    app: Application = build_api()

    setup_test_di(app, DIOverride(jwt_config))

    await app.start()
    yield app
    await app.stop()


@pytest.fixture
def test_client(
    app: Application,
    user_repo: UserRepository,
) -> TestClient:
    setup_test_di(app, di_overrides=[DIOverride(user_repo, UserRepository)])
    client: TestClient = TestClient(app)
    return client


@pytest.fixture(name="sa_engine", scope="session")
def create_sa_engine(db_config: DBConfig) -> AsyncEngine:
    return create_async_engine(db_config.full_url)


@pytest.fixture(name="sa_session_factory", scope="session")
def create_sa_session_factory(sa_engine: AsyncEngine) -> async_sessionmaker:
    return async_sessionmaker(
        bind=sa_engine,
        autoflush=False,
        expire_on_commit=False,
    )


@pytest.fixture(name="sa_session")
async def retrieve_async_sa_session(
    sa_engine: AsyncEngine,
    sa_session_factory: async_sessionmaker,
) -> AsyncGenerator[AsyncSession, None]:
    async with sa_engine.connect() as conn, sa_session_factory(bind=conn) as session:
        yield session


@pytest.fixture(name="menu_repo")
async def create_menu_repository(sa_session: AsyncSession) -> MenuRepository:
    return MenuRepositoryImpl(sa_session)


@pytest.fixture(name="user_repo")
async def create_user_repository() -> AsyncGenerator[UserRepository, None]:
    user_repo = UserRepositoryImpl()
    yield user_repo
    user_repo.users.clear()


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
