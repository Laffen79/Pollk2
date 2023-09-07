from django.urls import path
from . import views

urlpatterns = [
    path('', views.propanflasker_liste, name='propanflasker_liste'),
    path('detail/<int:NOBB_nykjop>/', views.propanflaske_detail, name='propanflaske_detail'),
]
