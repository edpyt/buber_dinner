from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class MenuReview(Base):
    __tablename__ = "menu_review"

    id: Mapped[UUID] = mapped_column(primary_key=True)
