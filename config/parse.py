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

import re
from types import TracebackType
from typing import IO, MutableMapping, Tuple, Optional, Type, AnyStr


class Parser:
    _SECTION: re.Pattern = re.compile(
        r"\[(?P<name>[^]]+)\]",
        re.VERBOSE,
    )

    _OPTION: re.Pattern = re.compile(
        r"(?P<name>.*?)\s*(=)\s*(?P<value>.*)$",
        re.VERBOSE,
    )

    def __init__(
            self,
            file: Optional[IO] = None,
            default_dict: Type[dict] = dict,
            *,
            delimiters: Tuple[str] = ('=',),
            comment_prefixes: Tuple[str] = ('#',),
            inline_comments: bool = True,
    ) -> None:
        self.file: Optional[IO] = file
        self._default_dict: Type[dict] = default_dict
        self._delimiters: Tuple[str] = delimiters
        self._comment_prefixes: Tuple[str] = comment_prefixes
        self._inline_comments: bool = inline_comments

    def __enter__(self) -> Parser:
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            exc_traceback: Optional[TracebackType],
    ) -> None:
        pass

    def _remove_comments(self, line: AnyStr) -> AnyStr:
        comment: re.Match = re.search(
            rf"({'|'.join(self._comment_prefixes)})",
            line,
        )
        if comment:
            return line[:comment.start()]
        return line

    def to_dict(self, file: Optional[IO] = None) -> MutableMapping:
        config: dict = self._default_dict()
        current: Optional[MutableMapping] = None

        for i, line in enumerate(self.file if file is None else file):
            line: AnyStr = self._remove_comments(line).strip()

            section: re.Match = self._SECTION.match(line)
            option: re.Match = self._OPTION.match(line)

            if section:
                name = section.group("name")
                if name in config:
                    current = config[name]
                else:
                    current = self._default_dict()
                    config[name] = current

            elif option:
                name, value = option.group("name", "value")
                if value is None:
                    current[name] = None
                else:
                    value = value.strip()
                    current[name] = value

        return config
