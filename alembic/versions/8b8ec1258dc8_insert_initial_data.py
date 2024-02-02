"""insert initial data

Revision ID: 8b8ec1258dc8
Revises: 
Create Date: 2023-12-10 16:42:49.565823

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '8b8ec1258dc8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    from models import RobolancerDB

    op.bulk_insert(RobolancerDB.__table__,
                   [
                       {
                           "id": 1,
                           "title": "Deep Fake",
                           "description": "Manipulation of facial appearance through deep generative methods on cheap",
                           "thumbnail": "1.jpg",
                           "location": "Bratislava",
                           "hourly_rate": 10
                       },
                       {
                           "id": 2,
                           "title": "Digital Woman",
                           "description": "Like a digital man but better",
                           "thumbnail": "2.jpg",
                           "location": "London",
                           "hourly_rate": 15
                       },
                       {
                           "id": 3,
                           "title": "Vacuum Robot",
                           "description": "A little sucker for a reasonable money",
                           "thumbnail": "3.jpg",
                           "location": "Seoul",
                           "hourly_rate": 5
                       },
                       {
                           "id": 4,
                           "title": "Robot Boris",
                           "description": "Like Yeltsin but has two fingers more",
                           "thumbnail": "4.jpg",
                           "location": "Moscow",
                           "hourly_rate": 100
                       },
                       {
                           "id": 5,
                           "title": "Delivery Robot",
                           "description": "Stucking almost for 10 years already",
                           "thumbnail": "5.jpg",
                           "location": 'San Francisco',
                           "hourly_rate": 7
                       },
                       {
                           "id": 6,
                           "title": "Robodog",
                           "description": "Like a dog but robot",
                           "thumbnail": "6.jpg",
                           "location": "Yulin",
                           "hourly_rate": 2
                       },
                       {
                           "id": 7,
                           "title": "A Bus Robot",
                           "description": "No driver to thanks",
                           "thumbnail": "7.jpg",
                           "location": 'Brisbane',
                           "hourly_rate": 10
                       },

                   ]
                   )


def downgrade() -> None:
    pass
