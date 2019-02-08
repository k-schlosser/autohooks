# Copyright (C) 2017-2019 Greenbone Networks GmbH
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

import os
import subprocess

from pathlib import Path


def get_git_directory_path():
    path = os.environ['PWD']
    try:
        output = subprocess.check_output(
            ['git', '-C', path, 'rev-parse', '--git-dir'],
        )
    except subprocess.CalledProcessError as e:
        print('could not determine .git directory. {}'.format(
            e.output.decode()
        ))
        raise e

    git_dir = output.decode().strip()
    if not path in git_dir:
        git_dir_path = Path(path) / git_dir
    else:
        git_dir_path = Path(git_dir)

    return git_dir_path.resolve()


def get_autohooks_directory_path():
    return Path(__file__).resolve().parent


def get_git_hook_directory_path():
    git_dir_path = get_git_directory_path()
    return git_dir_path / 'hooks'