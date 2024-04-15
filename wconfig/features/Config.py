from functools import wraps
from typing import Type

from wconfig.utils.is_class import is_class


def Config(name: str):
    def decorator(obj: Type[object]):
        def class_wrapper():
            if hasattr(obj.__class__, 'path'):
                obj.path += name
            else:
                obj.path = [name]

            for n, cls in vars(obj).items():
                if hasattr(cls.__class__, 'path'):
                    cls.__class__.path = obj.path + cls.path

            return obj

        @wraps(obj)
        def func_wrapper(self, *args, **kwargs):
            if hasattr(obj.__wrapped__, 'path'):
                obj.__wrapped__.path = name + obj.__wrapped__.path
            else:
                obj.__wrapped__.path = [name]

            return obj(self, *args, **kwargs)

        if is_class(obj):
            return class_wrapper()
        return func_wrapper

    return decorator
