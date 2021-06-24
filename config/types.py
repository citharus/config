import re
from typing import AnyStr, Union

__all__: list[str] = ['INT', 'FLOAT', 'LIST']


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
