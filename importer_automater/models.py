from django.db import models

class VendanorProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    picture_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    name_long = models.CharField(max_length=255)

    class Meta:
        app_label = 'importer_automater'

class VendanorNode(models.Model):
    id = models.IntegerField(primary_key=True)
    retailer_id = models.CharField(max_length=255)
    group_id = models.CharField(max_length=255)
    serialno = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, default='')
    postcode = models.CharField(max_length=255)
    postcity = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, default='')
    country = models.CharField(max_length=255)
    geo_lat = models.CharField(max_length=255)
    geo_lng = models.CharField(max_length=255)

    class Meta:
        app_label = 'importer_automater'

class VendanorNodesInventory(models.Model):
    node = models.ForeignKey(VendanorNode, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    count = models.JSONField()
    location = models.CharField(max_length=255)

    class Meta:
        unique_together = ('node', 'product_id')