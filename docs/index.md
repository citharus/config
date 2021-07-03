# CONFIG
The *config package* provides a simple config parser with easier
 accessibility.

The [**Parser**](#Parser) delivered with the *config package* provides a
context manager and a variety of options. For easier accessibility, the
[**Parser**](#Parser) has the option to convert the parsed config to a
nested namedtuple which contains the sections and their options.

## Parser
The simple parser of the *config package*.

### Positional parameters
**file**: file object, *optional*  
> The file to parse. If the *file* is not specified the parse method
> has to be provided with one. When using a context manager the Parse
> class has to be provided with the *file*.

**_dict**: dict, *default=dict*  
> The dict used by the Parser to create the config  

**default**: Any  
> The *default* value, when no value was provided in the config *file*.

**namedtuple**: bool, *default=False*  
> If the config should be converted to a *namedtuple*.

### Keyword parameters
**delimiters**: tuple[str], *default=('=',)*  
> A tuple of strings containing the option-value *delimiters*.

**comment_prefixes**: tuple[str], *default=('#',)*  
> A tuple of strings containing the *comment prefixes*.

**inline_comments**: bool, *default=False*  
> If inline comments are allowed.

**type_conversion**: bool, *default=False*  
> If basic types should be converted.

### Methods
#### parse
> ##### Parameters
> **file**: file object, *optional*  
> The file to parse. If the *file* is not specified the *file*
> provided to the [**Parser**](#Parser) will be used. If parse can not
> find a *file* an exception will be raised.
>
> ##### Returns
> **dict**  
> A dict containing all sections with their options.
>
> **namedtuple**  
> A namedtuple containing all sections which are namedtuples
> them self containing their options.
>
> ##### Raises
> **NoFileException**  
> If a file was not specified by the [**Parser**](#Parser) nor the
> function.
```pythonstub
>>> file = open('config.ini', 'r')
>>> Parser(file).parse()
{'SECTION': {'option': 'value'}}
```