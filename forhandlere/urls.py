from django.urls import path
from . import views

app_name = 'forhandlere'

urlpatterns = [
    path('kart/', views.kart, name='kart'),
    path('node/<int:node_id>/', views.node_produkter, name='node_produkter'),
]