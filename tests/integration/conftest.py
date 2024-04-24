from typing import AsyncGenerator, Callable, Coroutine, Generator

import pytest
from alembic.command import upgrade
from alembic.config import Config as AlembicConfig
from blacksheep import Application, JSONContent
from blacksheep.testing import TestClient
from sqlalchemy import Connection
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
from src.infrastructure.persistence.db.main import create_sa_engine, session_factory
from src.infrastructure.persistence.repositories.menu_repo import MenuRepositoryImpl
from src.infrastructure.persistence.repositories.user_repo import UserRepositoryImpl
from testcontainers.postgres import PostgresContainer

from tests.integration.di import DIOverride, setup_test_di


@pytest.fixture(name="postgres_db", scope="session")
def create_postgres_db() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer("postgres:16-bullseye") as postgres:
        yield postgres


@pytest.fixture(name="db_config", scope="session")
def create_db_config(postgres_db: PostgresContainer) -> DBConfig:
    return DBConfig(
        user="test",
        database="test",
        password="test",
        port=postgres_db.get_exposed_port("5432"),
    )


@pytest.fixture(name="alembic_config", scope="session")
def create_alembic_config(db_config: DBConfig) -> AlembicConfig:
    alembic_cfg = AlembicConfig("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", db_config.full_url)
    return alembic_cfg


@pytest.fixture(name="jwt_config", scope="session")
def create_jwt_config() -> JWTConfig:
    return JWTConfig(jwt_secret="test-secret", expiry_minutes=0)


@pytest.fixture(name="app", scope="session")
async def create_app(
    jwt_config: JWTConfig,
    postgres_db: PostgresContainer,
) -> AsyncGenerator[Application, None]:
    app: Application = build_api()

    setup_test_di(app, DIOverride(jwt_config))

    await app.start()
    yield app
    await app.stop()


@pytest.fixture
def di_overrides(user_repo: UserRepository, menu_repo: MenuRepository) -> list[DIOverride]:
    return [DIOverride(user_repo, UserRepository), DIOverride(menu_repo, MenuRepository)]


@pytest.fixture
def test_client(app: Application, di_overrides: list[DIOverride]) -> TestClient:
    setup_test_di(app, *di_overrides)
    return TestClient(app)


@pytest.fixture(scope="session")
async def _run_db_migrations(alembic_config: AlembicConfig) -> None:
    def migrate_db(connection: Connection) -> None:
        nonlocal alembic_config

        alembic_config.attributes["connection"] = connection
        upgrade(alembic_config, "head")

    migration_engine = create_async_engine(alembic_config.get_main_option("sqlalchemy.url"))
    async with migration_engine.connect() as conn:
        await conn.run_sync(migrate_db)
    await migration_engine.dispose()


@pytest.fixture(name="sa_engine", scope="session")
async def create_test_sa_engine(
    db_config: DBConfig,
    _run_db_migrations: None,
) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_sa_engine(db_config)
    # engine.echo = True
    yield engine
    await engine.dispose()


@pytest.fixture(name="sa_session_factory", scope="session")
async def create_sa_session_factory(sa_engine: AsyncEngine) -> async_sessionmaker:
    session_maker = session_factory(sa_engine)
    session_maker.configure(autoflush=False)
    return session_maker


@pytest.fixture(name="sa_session")
async def create_async_sa_session(
    sa_engine: AsyncEngine,
    sa_session_factory: async_sessionmaker,
) -> AsyncGenerator[AsyncSession, None]:
    # Transactional session
    async with sa_engine.connect() as conn:
        trans = await conn.begin()
        async with sa_session_factory(bind=conn) as session:
            yield session
        await trans.rollback()


@pytest.fixture(name="menu_repo")
def create_menu_repository(sa_session: AsyncSession) -> MenuRepository:
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
    auth_response_data = await auth_response.json()
    return auth_response_data["token"]
