from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)


class Beer(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to='uploads/', null=True, blank=False)
