import pytest
from typing import Callable
from datetime import datetime, timedelta, date
from fibonacci.exceptions import PerformanceException


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tock - tick
    print(f"diff time is {diff.total_seconds()} seconds")


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)) -> Callable:
    def run_function_and_validate_runtime(*args, **kwargs):
        tick = datetime.now()
        result = method(*args, **kwargs)
        tock = datetime.now()
        runtime = tock - tick
        print(f"runtime is {runtime.total_seconds()} seconds")

        if runtime > runtime_limit:
            raise PerformanceException(runtime=runtime, limit=runtime_limit)

        return result

    return run_function_and_validate_runtime
