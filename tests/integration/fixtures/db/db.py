from typing import Generator

import pytest
from src.infrastructure.config.db import DBConfig
from testcontainers.postgres import PostgresContainer


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
