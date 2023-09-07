from django import forms
from .models import GreenFuelsNodes


class GreenFuelsNodesForm(forms.ModelForm):
    class Meta:
        model = GreenFuelsNodes
        fields = ('location', 'address1', 'postcode', 'postcity', 'geo_lat', 'geo_lng', 'inventory')
