import inspect
from functools import wraps


def strict(func):
    sig = inspect.signature(func)
    annotations = func.__annotations__

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            if name in annotations:
                expected_type = annotations[name]
                if type(value) is not expected_type:
                    raise TypeError(
                        f"Argument '{name}' must be {expected_type.__name__}, "
                        f"got {type(value).__name__}"
                    )
        return func(*args, **kwargs)

    return wrapper
