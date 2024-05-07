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


@pytest.mark.django_db
class BasicCompanyApiTestCase(TestCase):
    def setUp(self):
        # self.client = Client()
        self.client = APIClient()
        self.comps_url = reverse("companies:companies-list")

    def tearDown(self) -> None:
        return super().tearDown()


# ============================================================


@pytest.mark.django_db
class TestGetCompanies(BasicCompanyApiTestCase):
    def test_zero_companies_should_return_empty_list(self) -> None:
        response: Response = self.client.get(self.comps_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_succeed(self) -> None:
        amazon = Company.objects.create(name="amazon")

        response: Response = self.client.get(self.comps_url)
        self.assertEqual(response.status_code, rest_statuses.HTTP_200_OK)

        companies = json.loads(response.content)
        self.assertNotEqual(companies, [])

        the_amazon = companies[0]
        self.assertEqual(the_amazon.get("name"), amazon.name)
        self.assertEqual(the_amazon.get("status"), "Hiring")

        amazon.delete()


# ============================================================


class TestPostCompanies(BasicCompanyApiTestCase):
    def test_create_company_without_argument_should_fail(self) -> None:
        response: Response = self.client.post(self.comps_url)
        self.assertEqual(response.status_code, rest_statuses.HTTP_400_BAD_REQUEST)

    def test_create_existing_company_should_fail(self) -> None:
        Company.objects.create(name="test-company")
        response: Response = self.client.post(
            path=self.comps_url, data={"name": "test-company"}
        )

        self.assertEqual(response.status_code, rest_statuses.HTTP_400_BAD_REQUEST)

    def test_create_company_with_only_name_all_fields_should_be_defaulted(self):
        response: Response = self.client.post(
            path=self.comps_url, data={"name": "test-company"}
        )

        self.assertEqual(response.status_code, rest_statuses.HTTP_201_CREATED)
        response_content = json.loads(response.content)

        self.assertEqual(response_content.get("name"), "test-company")
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), None)
        self.assertEqual(response_content.get("notes"), None)

    def test_create_company_with_layoffs_status_should_succeed(self):
        response: Response = self.client.post(
            path=self.comps_url, data={"name": "test-company", "status": "Layoffs"}
        )

        self.assertEqual(response.status_code, rest_statuses.HTTP_201_CREATED)
        response_content = json.loads(response.content)

        self.assertEqual(response_content.get("status"), "Layoffs")

    def test_create_company_with_wrong_layoffs_status_should_fail(self):
        response: Response = self.client.post(
            path=self.comps_url, data={"name": "test-company", "status": "Wrong status"}
        )

        self.assertEqual(response.status_code, rest_statuses.HTTP_400_BAD_REQUEST)
        response_content = json.loads(response.content)

        self.assertIn("Wrong status", str(response_content))
