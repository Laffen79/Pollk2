from django.db import models

class VendanorNodes(models.Model):
    serialno = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    postcode = models.CharField(max_length=20)
    postcity = models.CharField(max_length=200)
    geo_lat = models.FloatField()
    geo_lng = models.FloatField()

class GreenFuelsNodes(models.Model):
    location = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    postcode = models.CharField(max_length=20)
    postcity = models.CharField(max_length=200)
    geo_lat = models.FloatField()
    geo_lng = models.FloatField()