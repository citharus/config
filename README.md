<p align="center"><img src="docs/logo.png" height="100"></p>
<h1 align="center">CONFIG</h1>

The *config* package provides a simple config parser with easier accissability.

The **Parser** delivered with the *config* package provides a context manager and a variety of options.
For easier accessibility, the **Parser** has the option to convert the parsed config to a nested *namedtuple* which contains the sections and their options.

## Example
The **Parser** with the default settings:
```python
>>> from config import Parser

>>> with open('config.ini', 'r') as file:
        with Parser(file) as config:
            print(config)

{'SECTION': {'str': 'string', 'none': None, 'int': '1', 'float': '1.1', 'bool': 'yes'}}
```

The **Parser** with *namedtuples* enabled:
```python
>>> from config import Parser

>>> with open("config.ini") as file:
        with Parser(file, namedtuple=True) as config:
            print(config)
            
CONFIG(SECTION=SECTION(str='string', none=None, int='1', float='1.1', bool='yes'))
```

The **Parser** with *type conversion* enabled:
```python
>>> from config import Parser

>>> with open('config.ini', 'r') as file:
        with Parser(file, type_conversion=True) as config:
            print(config)

{'SECTION': {'str': 'string', 'none': None, 'int': 1, 'float': 1.1, 'bool': True}}
```

## Installation
```console
git clone https://github.com/citharus/config.git && cd config
sudo python setup.py install
```
