#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use types.py except in compliance with the License.
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
    """Convert the value to the respective type.

        If no type was detected the value will remain a string.
    """
    for _type in TYPE.__subclasses__():
        if _type(value).pattern.fullmatch(value.strip()):
            return _type(value).convert()
        return value[1:] if value.startswith(" ") else value


class TYPE(ABC):
    """The abstract base class for the basic types.

    Parameters
    ----------
    value : str
        The `value` to check against the type and to eventually covert.
    pattern : str
        The `pattern` defining the basic type.
    flags : Union[re.RegexFlag, int], optional
        The regex `flags` used for the final `pattern`.

    Attributes
    ----------
    value : str
        The `value` to check against the type and to eventually covert.
    pattern : re.Pattern
        The compiles regex pattern containing the `pattern` and `flags`.

    Methods
    -------
    convert()
        Abstract method for type conversion.
    """
    def __init__(
            self,
            value: str,
            pattern: str,
            flags: Union[re.RegexFlag, int] = 0,
    ) -> None:
        self.value: str = value
        self.pattern: re.Pattern = re.compile(pattern, flags)

    def convert(self):
        raise NotImplemented


class INT(TYPE):
    """The basic type representing an integer.

    Notes
    -----
    The regex pattern for the integer type is `\d+`.
    """
    def __init__(self, value: str) -> None:
        super(INT, self).__init__(value, r'\d+')

    def convert(self) -> int:
        return int(self.value)


class FLOAT(TYPE):
    """The basic type representing a float.

    Notes
    -----
    The regex pattern for the float type is `\d+.\d+`.
    An acceptable float is '1.1' and not '1.' or '.1'.
    """
    def __init__(self, value: str) -> None:
        super(FLOAT, self).__init__(value, r'\d+\.\d+')

    def convert(self) -> float:
        return float(self.value)


class BOOL(TYPE):
    """The basic type representing a bool.

    Notes
    -----
    A true bool can be either "true" or "yes". A false bool is "false" or
    "no".
    """
    def __init__(self, value: str) -> None:
        super(BOOL, self).__init__(
            value,
            r'(true|false|yes|no)',
            re.IGNORECASE,
        )

    def convert(self) -> bool:
        return self.value.lower().strip() in ['true', 'yes']


class LIST(TYPE):
    """The basic type representing a one dimensional list.

    Notes
    -----
    The regex pattern for the one dimensional list is `\[[^]]*\]`.
    An acceptable list is "[item, item,item]" but not
    "[item, item,[item, item]]"
    """
    def __init__(self, value: str) -> None:
        super(LIST, self).__init__(value, r'\[[^]]*\]')

    def convert(self) -> list:
        return [convert(i) for i in self.value[1:-1].split(",")]
