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

"""Patron type resolver."""


import jsonresolver

from ..jsonresolver import resolve_json_refs


@jsonresolver.route('/api/patron_types/<pid>', host='bib.rero.ch')
def patron_type_resolver(pid):
    """Patron type resolver."""
    return resolve_json_refs('ptty', pid)
