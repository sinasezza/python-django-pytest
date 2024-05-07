import logging
import pytest
from unittest import TestCase

logger = logging.getLogger("Company-logs")


class OtherTestCases(TestCase):
    @pytest.mark.xfail
    def test_should_be_ok_if_fails(self):
        self.assertEqual(1, 2)

    @pytest.mark.skip
    def test_should_be_skipped(self):
        self.assertEqual(1, 2)

    def raise_exception(self) -> None:
        raise ValueError("Expected exception")

    def test_raise_exception_should_pass(self) -> None:
        with pytest.raises(ValueError) as e:
            self.raise_exception()
        assert "Expected exception" == str(e.value)


def function_that_logs_something() -> None:
    try:
        raise ValueError("Expected function")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")


def test_logged_warning_level(caplog) -> None:
    function_that_logs_something()
    assert "I am logging Expected function" in caplog.text


def test_logged_info_level(caplog) -> None:
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        assert "I am logging info level" in caplog.text


@pytest.mark.under_test
def test_print():
    print("I am logging")
    assert 1 == 1
    print("I am logging info level")