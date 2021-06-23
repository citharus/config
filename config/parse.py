#  Copyright 2021-2021 citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import annotations

from typing import Tuple


class Parser:
    def __init__(
            self,
            dict_type: dict = dict,
            delimiters: Tuple[str] = ('=',),
            comment_prefixes: Tuple[str] = ('#',),
            inline_comments: bool = True,
    ) -> None:
        self._dict_type: dict = dict_type
        self._delimiters: Tuple[str] = delimiters
        self._comment_prefixes: Tuple[str] = comment_prefixes
        self._inline_comments: bool = inline_comments
