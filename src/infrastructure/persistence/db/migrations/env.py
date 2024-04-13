import asyncio
import os
from logging.config import fileConfig

from alembic import context
from clickhouse_sqlalchemy.alembic.dialect import include_object, patch_alembic_version
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from src.api.config import create_config_obj
from src.infrastructure.persistence.db.models.base import Base

# Models
from src.infrastructure.persistence.db.models.menu import Menu  # noqa: F401

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

if not (full_url := config.get_main_option("sqlalchemy.url")):
    db_config = create_config_obj().db_config
    db_config.host = os.getenv("DB_HOST", db_config.host)
    full_url = db_config.full_url

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=full_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        patch_alembic_version(context)
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        include_object=include_object,
    )

    with context.begin_transaction():
        patch_alembic_version(context)
        try:
            context.run_migrations()
        except Exception as e:  # noqa: BLE001
            print("Error:", repr(e), str(e))  # noqa: T201


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        url=full_url,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    connectable = config.attributes.get("connection", None)
    if connectable is None:
        asyncio.run(run_async_migrations())
    else:
        do_run_migrations(connectable)


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
