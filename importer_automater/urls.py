from django.urls import path
from . import views

app_name = 'importer_automater'

urlpatterns = [
    path('update_database/', views.update_database, name='update_database'),
]
