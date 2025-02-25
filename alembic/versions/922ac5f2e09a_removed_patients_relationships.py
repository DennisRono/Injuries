"""removed patients relationships

Revision ID: 922ac5f2e09a
Revises: 025faa21fbb1
Create Date: 2025-02-25 09:54:02.300643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '922ac5f2e09a'
down_revision: Union[str, None] = '025faa21fbb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
