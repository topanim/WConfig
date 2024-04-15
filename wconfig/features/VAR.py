import os
from functools import wraps
from typing import Callable

from wconfig.static.T import T
from wconfig.utils.get_path import get_path
from wconfig.utils.lead import lead


def VAR(
        path: str = "",
        _T: T = str,
        *,
        handle: bool = False
) -> T | None:
    def decorator(func: Callable[[T | None], object]):
        @wraps(func)
        def wrapper(self):
            p = get_path(self, func, path)
            var = lead(os.getenv(p), _T)

            if handle:
                return func(self, var)
            return var

        return wrapper

    return decorator
