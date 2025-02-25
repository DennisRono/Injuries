"""removed patients relationships

Revision ID: b7b035cbafd6
Revises: c2dacfb00570
Create Date: 2025-02-25 10:24:12.878324

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7b035cbafd6'
down_revision: Union[str, None] = 'c2dacfb00570'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
