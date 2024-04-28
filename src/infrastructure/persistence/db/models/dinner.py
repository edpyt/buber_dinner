from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseClass


class Dinner(BaseClass):
    __tablename__ = "dinner"

    id: Mapped[UUID] = mapped_column(primary_key=True)
