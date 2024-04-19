from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Dinner(Base):
    __tablename__ = "dinner"

    id: Mapped[UUID] = mapped_column(primary_key=True)
