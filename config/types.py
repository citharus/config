from __future__ import annotations

import re
from typing import AnyStr, Union, Type, Dict

__all__: list[str] = ['INT', 'FLOAT', 'LIST']

TYPES: Dict[str, re.Pattern] = {
    "INT": re.compile(r'\d+'),
    "FLOAT": re.compile(r'\d+\.\d+'),
    "LIST": re.compile(r'\[.*?\]'),
}


def find_type(value: str) -> Type[TYPE]:
    for _type, pattern in TYPES.items():
        if pattern.fullmatch(value):
            return eval(_type)


class TYPE:
    def __init__(
            self,
            pattern: AnyStr,
            flags: Union[int, re.RegexFlag] = 0,
    ) -> None:
        self.pattern: re.Pattern = re.compile(pattern, flags)


class INT(TYPE):
    def __init__(self) -> None:
        super(INT, self).__init__(r'\d+')


class FLOAT(TYPE):
    def __init__(self) -> None:
        super(FLOAT, self).__init__(r'\d+\.\d+')


class LIST(TYPE):
    def __init__(self) -> None:
        super(LIST, self).__init__(r'\[.*?\]')
