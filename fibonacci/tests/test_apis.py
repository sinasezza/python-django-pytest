import pytest
from django.urls import reverse
from django.test import Client

url_endpoint = reverse("fibonacci-api:calc_fibonacci")


def test_fibonacci_api_no_query_params(client: Client):
    response = client.get(url_endpoint)

    assert response.status_code == 200, "Status code should be 200"
    assert response.json() == 0, "fibonacci(None) should be 0"


@pytest.mark.parametrize(
    argnames="n, expected", argvalues=[(0, 0), (1, 1), (2, 1), (3, 2)]
)
def test_fibonacci_api(client: Client, n: int | None, expected: int):
    response = client.get(url_endpoint, data={"n": n})

    assert response.status_code == 200, "Status code should be 200"
    assert response.json() == expected, f"fibonacci({n}) should be {expected}"
