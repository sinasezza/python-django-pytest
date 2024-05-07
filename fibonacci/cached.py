from functools import lru_cache

cache = {}


def fibonacci_cached(n: int) -> int:
    if n in cache:
        return cache[n]

    if n == 0 or n == 1:
        return n

    fn = fibonacci_cached(n - 2) + fibonacci_cached(n - 1)

    cache[n] = fn

    return fn


@lru_cache()
def fibonacci_lru_cached(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fibonacci_lru_cached(n - 2) + fibonacci_lru_cached(n - 1)
