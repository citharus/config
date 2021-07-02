#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use __init__.py except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

__title__ = 'config'
__author__ = 'citharus'
__license__ = 'Apache License 2.0'
__copyright__ = 'Copyright 2021-present citharus'
__link__ = 'https://github.com/citharus/config'
__version__ = '1.0.1'

from collections import namedtuple

from .exceptions import *
from .parse import *
from .types import *

VersionInfo = namedtuple(
    'VersionInfo',
    'major minor micro releaselevel serial',
)
version_info = VersionInfo(
    major=1,
    minor=0,
    micro=0,
    releaselevel='none',
    serial=0,
)
