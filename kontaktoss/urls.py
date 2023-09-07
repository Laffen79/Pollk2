from django.urls import path
from kontaktoss.views import kontakt_oss

urlpatterns = [
    # Andre URL-ruter i prosjektet ditt
    path('kontakt/', kontakt_oss, name='kontakt_oss'),
]