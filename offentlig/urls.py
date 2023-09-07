from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('dealers/', views.dealers, name='dealers'),
    path('admin/', views.logg_inn, name='login'),
    path('logg-ut/', views.logg_ut, name='logout'),
]