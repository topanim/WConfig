# WConfig: Library to simplify working with the environment

[![PyPI version](https://badge.fury.io/py/whaox-wconfig.svg)](https://badge.fury.io/py/whaox-wconfig)

## Libraries used
 * [dotenv](https://github.com/theskumar/python-dotenv)

## Installation

```commandline
pip install whaox-wconfig
```

## Features
* Modularity
* Type conversion
* Auto-return or handling

## Setup

> First, let's set up ours `.env` file

```dotenv
API_KEY=YOUR_API_KEY

API_URL=https://example.com

LOGGING=False
```

## Usage
> Don't forget add this lines to your `main.py` file
 ```python
from dotenv import load_dotenv

load_dotev()
```
> Now let's create a config class

```python
class Config:
    
    @VAR("API_KEY")
    def api_key(self): pass
```

> You can easily get variables from your `.env` file

```python
config = Config()
config.api_key()

>>> YOUR_API_KEY
```

## Type conversion

> You can cast the value to the desired type, to do this, specify the type in the `_T` parameter
>
> NOTE: Supported types are `str, bool, int, float` 

```python
class Config:
    
    @VAR("LOGGING", bool)
    def logging(self) -> bool: pass
```

## Handling

> You can handle the received value if you need by setting the `handle` flag to `True`.

```python
class Config:
    
    @VAR("API_KEY", handle=True)
    def api_key(self, var): 
        return 'prefix-' + var
```

## Modularity
> You can split your config class into modules

```python
@Config("API")
class Api:
    
    @VAR("KEY")
    def key(self): pass
    
    @VAR("URL")
    def url(self): pass


class Config:
    api = Api()
    
    @VAR("LOGGING", bool)
    def logging(self): pass   
```

```python
config = Config()

config.api.key()
config.logging()
```
