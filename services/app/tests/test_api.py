import pytest
from http import HTTPStatus
from django.test.client import encode_multipart

from beer.models import Beer


@pytest.mark.django_db
def test_get_beer(client, beer):
    url = f'/beer/{beer.id}'
    response = client.get(url)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_list_beers(client, beer):
    url = f'/beer/'
    response = client.get(url)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_update_beer(api_client, beer):
    url = f'/beer/{beer.id}'
    data = {'name': 'Guinness'}
    content = encode_multipart('BoUnDaRyStRiNg', data)
    content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'

    response = api_client.patch(url, data=content, content_type=content_type)
    assert response.status_code == HTTPStatus.FOUND

    beer.refresh_from_db()

    assert beer.name == 'Guinness'


@pytest.mark.django_db
def test_create_beer(client):
    url = f'/beer/create'

    response = client.post(url, {'name': 'Hobgoblin'})
    assert response.status_code == HTTPStatus.FOUND
    assert Beer.objects.count() == 1
    assert Beer.objects.first().name == 'Hobgoblin'


@pytest.mark.django_db
def test_delete_beer(client, beer):
    url = f'/beer/{beer.id}'

    response = client.delete(url)
    assert response.status_code == HTTPStatus.FOUND
    assert Beer.objects.count() == 0
