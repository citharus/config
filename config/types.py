import re

__all__: list[str] = ["INTEGER", "FLOAT", "LIST"]

INTEGER: re.Pattern = re.compile(r"\d+")
FLOAT: re.Pattern = re.compile(r"\d+\.\d+")
LIST: re.Pattern = re.compile(r"\[.*?\]")
