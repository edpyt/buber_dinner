from alembic.command import upgrade
from alembic.config import Config
from sqlalchemy.ext.asyncio import AsyncConnection


def migrate_db(connection: AsyncConnection, alembic_config: Config) -> None:
    alembic_config.attributes["connection"] = connection
    upgrade(alembic_config, "head")
