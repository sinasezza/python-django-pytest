import pytest
from django.urls import reverse
from ..models import Company


comps_url = reverse("companies:companies-list")


@pytest.mark.parametrize(
    argnames="companies",
    argvalues=[["Test Company INC", "Test Company INC 2"], ["Instagram", "Facebook"]],
    ids=["test companies", "Zukerberg's companies"],
    indirect=True,
)
def test_multiple_companies_exists_should_succeed(db, client, companies) -> None:
    company_names = set(map(lambda company: company.name, companies))

    response_companies = client.get(comps_url).json()

    assert len(response_companies) == len(company_names)

    response_company_names = set(
        map(lambda company: company.get("name"), response_companies)
    )
    assert company_names == response_company_names
