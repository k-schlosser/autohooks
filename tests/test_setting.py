# Copyright (C) 2019 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from autohooks.setting import Mode


class ModeTestCase(unittest.TestCase):
    def test_get_effective_mode(self):
        self.assertEqual(Mode.PIPENV.get_effective_mode(), Mode.PIPENV)
        self.assertEqual(Mode.PYTHONPATH.get_effective_mode(), Mode.PYTHONPATH)
        self.assertEqual(Mode.UNDEFINED.get_effective_mode(), Mode.PYTHONPATH)
        self.assertEqual(Mode.UNKNOWN.get_effective_mode(), Mode.PYTHONPATH)

    def test_get_pipenv_mode_from_string(self):
        self.assertEqual(Mode.from_string('pipenv'), Mode.PIPENV)
        self.assertEqual(Mode.from_string('PIPENV'), Mode.PIPENV)

    def test_get_pythonpath_mode_from_string(self):
        self.assertEqual(Mode.from_string('pythonpath'), Mode.PYTHONPATH)
        self.assertEqual(Mode.from_string('PYTHONPATH'), Mode.PYTHONPATH)

    def test_get_invalid_mode_from_string(self):
        self.assertEqual(Mode.from_string('foo'), Mode.UNKNOWN)
        self.assertEqual(Mode.from_string(None), Mode.UNDEFINED)
        self.assertEqual(Mode.from_string(''), Mode.UNDEFINED)


if __name__ == '__main__':
    unittest.main()
