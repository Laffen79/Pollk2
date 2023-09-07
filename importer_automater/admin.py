from django.contrib import admin
from .models import VendanorProduct, VendanorNode, VendanorNodesInventory

admin.site.register(VendanorProduct)
admin.site.register(VendanorNode)
admin.site.register(VendanorNodesInventory)