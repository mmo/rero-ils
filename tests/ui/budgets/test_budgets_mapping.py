# -*- coding: utf-8 -*-
#
# RERO ILS
# Copyright (C) 2019 RERO
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Acquisition budget record mapping tests."""
from utils import get_mapping

from rero_ils.modules.budgets.api import Budget, BudgetsSearch


def test_budgets_es_mapping(es, db, org_martigny, budget_2017_martigny_data):
    """Test acquisition budget elasticsearch mapping."""
    search = BudgetsSearch()
    mapping = get_mapping(search.Meta.index)
    assert mapping
    budget = Budget.create(
        budget_2017_martigny_data,
        dbcommit=True,
        reindex=True,
        delete_pid=True
    )
    assert mapping == get_mapping(search.Meta.index)
    budget.delete(force=True, dbcommit=True, delindex=True)
