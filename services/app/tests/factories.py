import factory
import factory.fuzzy

from beer import models


class ManufacturerFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Manufacturer

    name = factory.fuzzy.FuzzyText()


class BeerFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Beer

    manufacturer = factory.SubFactory(ManufacturerFactory)
    name = factory.fuzzy.FuzzyText()
    image = None
