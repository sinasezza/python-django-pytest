import json
import pytest
import requests
import responses
from requests.exceptions import HTTPError
from requests.models import Response, Request


comps_url = 'http://localhost:8000/companies/'


def test_zero_companies_django_agnostic() -> None:
    response: Response = requests.get(url=comps_url)
    assert response.status_code == 200
    
    content = json.loads(response.content)


def cleanup_company(company_id: int) -> None:
    response = requests.delete(url=f'{comps_url}{company_id}/')
    assert response.status_code == 204
    

def test_create_company_with_layoffs_django_agnostic():
    response: Response = requests.post(
        url=comps_url, data={"name": "test-company3", "status": "Layoffs"}
    )

    assert response.status_code == 201
    response_content = json.loads(response.content)

    assert response_content.get("status") == "Layoffs"
    
    cleanup_company(response_content.get('id'))
    


@pytest.mark.countries
@pytest.mark.parametrize('cName', ['iran', 'spain', 'china', 'germany'])
def test_countries_api(cName: str) -> None:
    url = f'https://restcountries.com/v3.1/name/{cName}'
    
    response = requests.get(url=url)
    
    assert response.status_code == 200
    
    print(f"response content: {json.loads(response.content)}")



@pytest.mark.countries
@responses.activate
@pytest.mark.parametrize('cName', ['iran', 'spain', 'china', 'germany'])
def test_mocked_countries_api(cName: str) -> None:
    responses.add(method=responses.GET, url=f'https://restcountries.com/v3.1/name/{cName}', status=200, json={'name': cName.capitalize()})
    
    response = requests.get(url=f'https://restcountries.com/v3.1/name/{cName}')
    
    assert response.status_code == 200
        
    print(f"response content: {json.loads(response.content)}")
    
    assert json.loads(response.content).get('name') == cName.capitalize()
    