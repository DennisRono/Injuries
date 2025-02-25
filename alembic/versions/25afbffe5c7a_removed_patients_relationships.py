"""removed patients relationships

Revision ID: 25afbffe5c7a
Revises: b7b035cbafd6
Create Date: 2025-02-25 10:24:56.334424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25afbffe5c7a'
down_revision: Union[str, None] = 'b7b035cbafd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
