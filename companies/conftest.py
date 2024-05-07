import pytest
from typing import Callable, List
from .models import Company


@pytest.fixture
def amazon() -> Company:
    return Company.objects.create(name="amazon")


@pytest.fixture()
def company(**kwargs) -> Callable:
    def _company_factory(**kwargs) -> Company:
        company_name = kwargs.pop("name", "Test Company INC")
        return Company.objects.create(name=company_name, **kwargs)

    return _company_factory


@pytest.fixture
def companies(request, company) -> List[Company]:
    companies = []

    names = request.param

    for name in names:
        companies.append(company(name=name))

    return companies
