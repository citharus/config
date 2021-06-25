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
from abc import ABC
from typing import Type, Union

__all__: list[str] = ['INT', 'FLOAT', 'BOOL', 'LIST', 'convert']


def convert(value: str) -> Union[Type[TYPE], str]:
    for _type in TYPE.__subclasses__():
        if _type(value).pattern.fullmatch(value.strip()):
            return _type(value).convert()
        else:
            return value


class TYPE(ABC):
    def __init__(
            self,
            value: str,
            pattern: str,
            flags: Union[re.RegexFlag, int] = 0,
    ) -> None:
        self.value: str = value
        self.pattern: re.Pattern = re.compile(pattern, flags)

    def convert(self) -> None:
        pass


class INT(TYPE):
    def __init__(self, value: str) -> None:
        super(INT, self).__init__(value, r'\d+')

    def convert(self) -> int:
        return int(self.value)


class FLOAT(TYPE):
    def __init__(self, value: str) -> None:
        super(FLOAT, self).__init__(value, r'\d+\.\d+')

    def convert(self) -> float:
        return float(self.value)


class BOOL(TYPE):
    def __init__(self, value: str) -> None:
        super(BOOL, self).__init__(
            value,
            r'(true|false|yes|no)',
            re.IGNORECASE,
        )

    def convert(self) -> bool:
        return self.value.lower() in ['yes', 'true']


class LIST(TYPE):
    def __init__(self, value: str) -> None:
        super(LIST, self).__init__(value, r'\[.*\]')

    def convert(self) -> list:
        return [convert(i) for i in self.value[1:-1].split(",")]
