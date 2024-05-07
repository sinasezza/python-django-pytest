import pytest
from time import sleep

from ..dynamic import fibonacci_dynamic_space_efficient
from conftest import track_performance


@pytest.mark.performance
@track_performance
def test_performance():
    fibonacci_dynamic_space_efficient(1000)
