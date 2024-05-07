import pytest
from typing import Callable
from ..naive import fibonacci_naive
from ..cached import fibonacci_cached, fibonacci_lru_cached
from ..dynamic import fibonacci_dynamic, fibonacci_dynamic_space_efficient
from ..decorators import my_parameterize
from conftest import time_tracker


# @my_parameterize(identifiers="n, expected", values=[(0, 0), (1, 1), (2, 1), (20, 6765)])
# @pytest.mark.parametrize(
#     argnames="n, expected", argvalues=((0, 0), (1, 1), (2, 1), (20, 6765))
# )
# def test_naive(n: int, expected: int) -> None:
#     assert fibonacci_naive(n) == expected


# @pytest.mark.parametrize(
#     argnames="n, expected", argvalues=((0, 0), (1, 1), (2, 1), (20, 6765))
# )
# def test_cached(n: int, expected: int) -> None:
#     assert fibonacci_cached(n) == expected


@pytest.mark.parametrize(
    argnames="fib_func",
    argvalues=[
        fibonacci_naive,
        fibonacci_cached,
        fibonacci_lru_cached,
        fibonacci_dynamic,
        fibonacci_dynamic_space_efficient,
    ],
)
@pytest.mark.parametrize(argnames="n, expected", argvalues=[(15, 610)])
def test_fibonacci(
    time_tracker, fib_func: Callable[[int], int], n: int, expected: int
) -> None:
    assert fib_func(n) == expected
