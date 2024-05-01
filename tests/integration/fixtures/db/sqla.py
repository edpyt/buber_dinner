from typing import AsyncGenerator

import pytest
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)
from src.infrastructure.config.db import DBConfig
from src.infrastructure.persistence.db.main import create_sa_engine, session_factory


@pytest.fixture(name="sa_engine", scope="session")
async def create_test_sa_engine(
    db_config: DBConfig,
    run_db_migrations: None,
) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_sa_engine(db_config)
    engine.echo = True
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
