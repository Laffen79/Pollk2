from django.urls import path
from . import views

app_name = 'hent_produkt'

urlpatterns = [
    path('node_inventory/<str:serialno>/', views.get_node_inventory, name='node_inventory'),
]