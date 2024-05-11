from typing import AsyncGenerator, Callable, Coroutine

import pytest
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from src.application.common.mapper.interface import MenuMapper
from src.application.dto.user import UserDTO
from src.application.persistence.menu_repo import MenuRepository
from src.application.persistence.user_repo import UserRepository
from src.infrastructure.persistence.repositories.menu_repo import MenuRepositoryImpl
from src.infrastructure.persistence.repositories.user_repo import UserRepositoryImpl


@pytest.fixture(name="menu_repo")
def create_menu_repository(sa_session: AsyncSession, menu_mapper: MenuMapper) -> MenuRepository:
    return MenuRepositoryImpl(sa_session, menu_mapper=menu_mapper)


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
