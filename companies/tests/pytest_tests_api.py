import json
import pytest
from unittest import TestCase
from django.test import Client

# from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import status as rest_statuses
from ..models import Company


comps_url = reverse("companies:companies-list")

# this will apply for all tests in this file
pytestmark = pytest.mark.django_db


def test_zero_companies_should_return_empty_list(client) -> None:
    response: Response = client.get(comps_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


# def test_one_company_exists_should_succeed(client) -> None:
#     amazon = Company.objects.create(name="amazon")

#     response: Response = client.get(comps_url)
#     assert response.status_code == rest_statuses.HTTP_200_OK

#     companies = json.loads(response.content)
#     assert companies != []

#     the_amazon = companies[0]
#     assert the_amazon.get("name") == amazon.name
#     assert the_amazon.get("status") == "Hiring"


def test_one_company_exists_should_succeed(client, amazon) -> None:
    response: Response = client.get(comps_url)
    assert response.status_code == rest_statuses.HTTP_200_OK

    companies = json.loads(response.content)
    assert companies != []

    the_amazon = companies[0]
    assert the_amazon.get("name") == amazon.name
    assert the_amazon.get("status") == "Hiring"


def test_create_company_without_argument_should_fail(client) -> None:
    response: Response = client.post(comps_url)
    assert response.status_code, rest_statuses.HTTP_400_BAD_REQUEST


def test_create_existing_company_should_fail(client) -> None:
    Company.objects.create(name="test-company")
    response: Response = client.post(path=comps_url, data={"name": "test-company"})

    assert response.status_code == rest_statuses.HTTP_400_BAD_REQUEST


def test_create_company_with_only_name_all_fields_should_be_defaulted(client):
    response: Response = client.post(path=comps_url, data={"name": "test-company"})

    assert response.status_code == rest_statuses.HTTP_201_CREATED
    response_content = json.loads(response.content)

    assert response_content.get("name") == "test-company"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") is None
    assert response_content.get("notes") is None


def test_create_company_with_layoffs_status_should_succeed(client):
    response: Response = client.post(
        path=comps_url, data={"name": "test-company", "status": "Layoffs"}
    )

    assert response.status_code == rest_statuses.HTTP_201_CREATED
    response_content = json.loads(response.content)

    assert response_content.get("status") == "Layoffs"


def test_create_company_with_wrong_layoffs_status_should_fail(client):
    response: Response = client.post(
        path=comps_url, data={"name": "test-company", "status": "Wrong status"}
    )

    assert response.status_code == rest_statuses.HTTP_400_BAD_REQUEST
    response_content = json.loads(response.content)

    assert "Wrong status" in str(response_content)
