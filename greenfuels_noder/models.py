# from django.db import models

# Create your models here.

from django.db import models

class GreenFuelsNodes(models.Model):
    location = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    postcity = models.CharField(max_length=255)
    geo_lat = models.DecimalField(max_digits=18, decimal_places=16)
    geo_lng = models.DecimalField(max_digits=18, decimal_places=16)
    inventory = models.TextField(blank=True)

    def __str__(self):
        return self.location
