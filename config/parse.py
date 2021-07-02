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
from collections import namedtuple
from types import TracebackType
from typing import Union, Optional, Type, Any, AnyStr, IO, Tuple, Dict

from config.exceptions import NoFileException
from config.types import convert

__all__: list[str] = ['Parser']


class Parser:
    _SECTION: re.Pattern = re.compile(
        r'\[(?P<name>[^]]+)\]',
        re.VERBOSE,
    )

    _OPTION: re.Pattern = re.compile(
        r'(?P<name>.*?)\s*(=)\s*(?P<value>.*)$',
        re.VERBOSE,
    )

    def __init__(
            self,
            file: Optional[IO] = None,
            _dict: Type[dict] = dict,
            default: Optional[Any] = None,
            namedtuple: bool = False,
            *,
            delimiters: Tuple[str] = ('=',),
            comment_prefixes: Tuple[str] = ('#',),
            inline_comments: bool = False,
            type_conversion: bool = False,
    ) -> None:
        self.file: Optional[IO] = file
        self._dict: Type[dict] = _dict
        self._default: Optional[Any] = default
        self._namedtuple: bool = namedtuple
        self._delimiters: Tuple[str] = delimiters
        self._comment_prefixes: Tuple[str] = comment_prefixes
        self._inline_comments: bool = inline_comments
        self._type_conversion: bool = type_conversion

    def __enter__(self) -> Union[namedtuple, Dict[str, Any]]:
        return self.parse()

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            exc_traceback: Optional[TracebackType],
    ) -> None:
        self.file.close()

    def _remove_comment(self, line: AnyStr) -> AnyStr:
        comment: re.Match = re.search(
            rf'({"|".join(self._comment_prefixes)})',
            line,
        )
        if self._inline_comments and comment:
            return line[:comment.start()]
        return line

    def _to_dict(self, file: Optional[IO] = None) -> Dict[str, Any]:
        config: dict = self._dict()
        current: Optional[dict] = None

        for i, line in enumerate(self.file if file is None else file):
            line: AnyStr = self._remove_comment(line).strip()
            section: re.Match = self._SECTION.match(line)
            option: re.Match = self._OPTION.match(line)

            if section:
                name = section.group('name')
                if name in config:
                    current = config[name]
                else:
                    current = self._dict()
                    config[name] = current
            elif option:
                name, value = option.group('name', 'value')
                if not value:
                    current[name] = self._default
                else:
                    if self._type_conversion:
                        value = convert(value.strip())
                    current[name] = value
        return config

    def _to_namedtuple(self, file: Optional[IO] = None) -> namedtuple:
        config: Dict[str, Any] = self._to_dict(
            self.file if file is None else file
        )
        tuples: list[namedtuple] = [
            namedtuple(
                section,
                options.keys(),
            )(*options.values()) for section, options in config.items()
        ]
        return namedtuple("CONFIG", config.keys())(*tuples)

    def parse(
            self,
            file: Optional[IO] = None,
    ) -> Union[namedtuple, Dict[str, Any]]:
        """Parses the configuration file with the specified options.

        Parameters
        ----------
        file : Optional[IO]
            The file to parse. If the `file` is not specified the `file`
            provided to the Parser class will be used. If parse can not
            find a `file` an exception will be raised.

        Returns
        -------
        dict
            A dict containing all sections with their options.
        namedtuple
            A namedtuple containing all sections which are namedtuples
            them self containing their options.

        Raises
        ------
        NoFileException
            If a file was not specified by the Parser class nor the
            function.

        Examples
        --------
        >>> file = open('config.ini', 'r')
        >>> Parser(file).parse()
        {'SECTION': {'option': 'value'}}
        """
        try:
            if self._namedtuple:
                return self._to_namedtuple(file)
            return self._to_dict(file)
        except TypeError:
            raise NoFileException
