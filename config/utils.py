#  Copyright 2021-2021 citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use utils.py except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import re
from typing import AnyStr, Tuple

__all__: list[str] = ['remove_comment']


def remove_comment(line: AnyStr, prefixes: Tuple[str]) -> AnyStr:
    comment: re.Match = re.search(
        rf'({"|".join(prefixes)})',
        line,
    )
    if comment:
        return line[:comment.start()]
    return line
