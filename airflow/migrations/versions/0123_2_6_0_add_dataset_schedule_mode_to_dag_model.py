#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""add dataset schedule mode to DAG model

Revision ID: 7afd6d4021a9
Revises: 290244fb8b83
Create Date: 2022-12-13 11:34:26.648465

"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7afd6d4021a9"
down_revision = "290244fb8b83"
branch_labels = None
depends_on = None
airflow_version = "2.6.0"


def upgrade():
    op.add_column("dag", sa.Column("run_on_any_dataset_changed", sa.Boolean(), nullable=False, default=False))


def downgrade():
    op.drop_column("dag", "run_on_any_dataset_changed")