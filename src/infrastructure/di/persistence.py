from rodi import Container
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.application.persistence.menu_repo import MenuRepository
from src.application.persistence.user_repo import UserRepository
from src.infrastructure.persistence.db.main import (
    create_sa_engine,
    create_session,
    session_factory,
)
from src.infrastructure.persistence.menu_repo import MenuRepositoryImpl
from src.infrastructure.persistence.user_repo import UserRepositoryImpl


def setup_persistence_di(container: Container) -> None:
    container.add_singleton_by_factory(create_sa_engine, AsyncEngine)
    container.add_singleton_by_factory(session_factory, async_sessionmaker)
    container.add_scoped_by_factory(create_session, AsyncSession)

    container.add_singleton(UserRepository, UserRepositoryImpl)
    container.add_singleton(MenuRepository, MenuRepositoryImpl)
