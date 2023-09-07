from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import GreenFuelsNodes

@admin.register(GreenFuelsNodes)
class GreenFuelsNodesAdmin(admin.ModelAdmin):
    list_display = ('location', 'address1', 'postcode', 'postcity', 'geo_lat', 'geo_lng', 'inventory')