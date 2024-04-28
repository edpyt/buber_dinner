from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseClass


class MenuReview(BaseClass):
    __tablename__ = "menu_review"

    id: Mapped[UUID] = mapped_column(primary_key=True)
