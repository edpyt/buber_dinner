from rodi import Container

from src.application.persistence.menu_repo import MenuRepository
from src.application.persistence.user_repo import UserRepository
from src.infrastructure.persistence.menu_repo import MenuRepositoryImpl
from src.infrastructure.persistence.user_repo import UserRepositoryImpl


def setup_repositories_di(container: Container) -> None:
    container.add_singleton(UserRepository, UserRepositoryImpl)
    container.add_singleton(MenuRepository, MenuRepositoryImpl)
