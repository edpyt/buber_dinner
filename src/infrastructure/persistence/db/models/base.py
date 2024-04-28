from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase): ...


class BaseClass(Base):
    __abstract__ = True

    def __init__(self, entity: object | None = None, **kwargs) -> None:
        """Initialize SQLAlchemy model.

        :param entity: Optional `Entity` instance attribute
        :param kwargs: SQLAlchemy model params
        """
        super().__init__(**kwargs)
        self.entity = entity
