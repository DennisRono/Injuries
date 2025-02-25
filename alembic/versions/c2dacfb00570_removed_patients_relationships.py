"""removed patients relationships

Revision ID: c2dacfb00570
Revises: 922ac5f2e09a
Create Date: 2025-02-25 10:06:12.776451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2dacfb00570'
down_revision: Union[str, None] = '922ac5f2e09a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
