import time
from typing import List, Tuple, Callable
from functools import wraps


Decorator = Callable


def my_parameterize(identifiers: str, values: List[Tuple[int, int]]) -> Callable:
    def my_parameterized_decorator(function: Callable) -> Callable:
        def run_function_parameterized() -> None:
            list_of_kwargs_for_function = ...

    return my_parameterized_decorator


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {func.__name__} took {end_time - start_time} seconds to execute."
        )
        return result

    return wrapper
