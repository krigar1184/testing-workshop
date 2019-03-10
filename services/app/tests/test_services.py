import pytest
import requests_mock
from beer.service.add_beer_image import add_beer_image


@pytest.mark.parametrize('beer__image', [None])
@pytest.mark.django_db
def test_add_beer_image(beer):
    def test_callback(request, context):
        with open('./media/sample_image') as f:
            return f.read()

    with requests_mock.mock() as m:
        m.get(requests_mock.ANY)
        add_beer_image(beer.id)

    beer.refresh_from_db()
    assert beer.image is not None
