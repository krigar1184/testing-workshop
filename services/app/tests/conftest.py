import pytest
from pytest_factoryboy import register
import factories
from rest_framework.test import APIClient


register(factories.ManufacturerFactory, 'manufacturer')
register(factories.BeerFactory, 'beer')


@pytest.fixture
def api_client():
    return APIClient()
