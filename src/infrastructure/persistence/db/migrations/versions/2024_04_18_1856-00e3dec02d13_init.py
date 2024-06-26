"""init

Revision ID: 00e3dec02d13
Revises:
Create Date: 2024-04-18 18:56:34.968723

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

import src.infrastructure.persistence.db.types as custom_types
from src.application.menu.dto.average_rating import AverageRatingDTO

# revision identifiers, used by Alembic.
revision: str = "00e3dec02d13"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "menu",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=100), nullable=False),
        sa.Column(
            "average_rating",
            custom_types.DataclassType(AverageRatingDTO),
            nullable=False,
        ),
        sa.Column("host_id", sa.Uuid(), nullable=False),
        sa.Column("created_date_time", sa.DateTime(), nullable=False),
        sa.Column("updated_date_time", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("menu")
    # ### end Alembic commands ###
