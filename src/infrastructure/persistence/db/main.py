from typing import AsyncGenerator

from rodi import ActivationScope
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.infrastructure.config.db import DBConfig


def create_sa_engine(db_config: DBConfig) -> AsyncEngine:
    # BUG: why `rodi` sends ActivationScope here??
    if isinstance(db_config, ActivationScope):
        db_config = db_config.get(DBConfig)
    return create_async_engine(db_config.full_url)


def session_factory(engine: AsyncEngine) -> async_sessionmaker:
    return async_sessionmaker(bind=engine)


async def create_session(
    session_factory: async_sessionmaker,
) -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
