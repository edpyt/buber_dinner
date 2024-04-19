from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, ForeignKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.application.menu.dto.average_rating import AverageRatingDTO
from src.infrastructure.persistence.db.types.dataclass import DataclassType

from .base import Base


class Menu(Base):
    __tablename__ = "menu"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=100))
    description: Mapped[str] = mapped_column(String(length=100))
    average_rating: Mapped[AverageRatingDTO] = mapped_column(DataclassType(AverageRatingDTO))
    host_id: Mapped[UUID]

    sections: Mapped[list["MenuSection"]] = relationship(back_populates="menu")
    dinner_ids: Mapped[list["MenuDinnerIds"]] = relationship(backref="menu")
    review_ids: Mapped[list["MenuReviewIds"]] = relationship(backref="menu")

    created_date_time: Mapped[datetime]
    updated_date_time: Mapped[datetime]


class MenuSection(Base):
    __tablename__ = "menu_sections"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(100))

    items: Mapped[list["MenuItem"]] = relationship(back_populates="section")

    menu: Mapped[Menu] = relationship(back_populates="sections")
    menu_id: Mapped[UUID] = mapped_column(ForeignKey("menu.id"), primary_key=True)


class MenuItem(Base):
    __tablename__ = "menu_items"
    __table_args__ = (
        ForeignKeyConstraint(
            ["section_id", "menu_id"],
            ["menu_sections.id", "menu_sections.menu_id"],
        ),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(100))

    section_id: Mapped[UUID] = mapped_column(primary_key=True)
    menu_id: Mapped[UUID] = mapped_column(primary_key=True)
    section: Mapped[MenuSection] = relationship(
        back_populates="items",
        foreign_keys=[menu_id, section_id],
    )


class MenuDinnerIds(Base):
    __tablename__ = "menu_dinner_ids"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    menu_id: Mapped[UUID] = mapped_column(ForeignKey("menu.id"))
    dinner_id: Mapped[UUID] = mapped_column(ForeignKey("dinner.id"))


class MenuReviewIds(Base):
    __tablename__ = "menu_review_ids"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    menu_id: Mapped[UUID] = mapped_column(ForeignKey("menu.id"))
    review_id: Mapped[UUID] = mapped_column(ForeignKey("menu_review.id"))
