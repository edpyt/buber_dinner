from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.application.persistence.menu_repo import MenuRepository
from src.application.persistence.user_repo import UserRepository
from src.infrastructure.persistence.db.main import (
    create_sa_engine,
    create_session,
    session_factory,
)
from src.infrastructure.persistence.repositories.menu_repo import MenuRepositoryImpl
from src.infrastructure.persistence.repositories.user_repo import UserRepositoryImpl


class PersistenceProvider(Provider):
    sa_engine = provide(
        create_sa_engine,
        provides=AsyncEngine,
        scope=Scope.APP,
    )
    sa_session_factory = provide(
        session_factory,
        provides=async_sessionmaker,
        scope=Scope.APP,
    )
    sa_session = provide(
        create_session,
        provides=AsyncSession,
        scope=Scope.REQUEST,
    )

    user_repo = provide(
        UserRepositoryImpl,
        provides=UserRepository,
        scope=Scope.APP,
    )
    menu_repo = provide(
        MenuRepositoryImpl,
        provides=MenuRepository,
        scope=Scope.REQUEST,
    )
