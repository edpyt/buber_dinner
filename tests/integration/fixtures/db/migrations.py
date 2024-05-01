
import pytest
from alembic.command import upgrade
from alembic.config import Config as AlembicConfig
from sqlalchemy import Connection
from sqlalchemy.ext.asyncio import (
    create_async_engine,
)
from src.infrastructure.config.db import DBConfig


@pytest.fixture(name="alembic_config", scope="session")
def create_alembic_config(db_config: DBConfig) -> AlembicConfig:
    alembic_cfg = AlembicConfig("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", db_config.full_url)
    return alembic_cfg


@pytest.fixture(scope="session")
async def run_db_migrations(alembic_config: AlembicConfig) -> None:  # noqa: PT004
    def migrate_db(connection: Connection) -> None:
        nonlocal alembic_config

        alembic_config.attributes["connection"] = connection
        upgrade(alembic_config, "head")

    migration_engine = create_async_engine(alembic_config.get_main_option("sqlalchemy.url"))
    async with migration_engine.connect() as conn:
        await conn.run_sync(migrate_db)
    await migration_engine.dispose()
