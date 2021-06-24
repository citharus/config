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
from typing import Type, Dict

__all__: list[str] = ['INT', 'FLOAT', 'LIST', 'convert']

TYPES: Dict[str, re.Pattern] = {
    "INT": re.compile(r'\d+'),
    "FLOAT": re.compile(r'\d+\.\d+'),
    "LIST": re.compile(r'\[.*?\]'),
}


def convert(value: str) -> Type[TYPE]:
    for _type, pattern in TYPES.items():
        if pattern.fullmatch(value.strip(" ")):
            return eval(_type)(value).convert()


class TYPE:
    def __init__(self, value: str) -> None:
        self.value: str = value


class INT(TYPE):
    def __init__(self, value: str) -> None:
        super(INT, self).__init__(value)

    def convert(self) -> int:
        return int(self.value)


class FLOAT(TYPE):
    def __init__(self, value: str) -> None:
        super(FLOAT, self).__init__(value)

    def convert(self) -> float:
        return float(self.value)


class LIST(TYPE):
    def __init__(self, value: str) -> None:
        super(LIST, self).__init__(value)

    def convert(self) -> list:
        return [convert(i) for i in self.value[1:-1].split(",")]
