"""
URL configuration for Pollk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('offentlig.urls')),
    path('importer_automater/', include(('importer_automater.urls', 'importer_automater_urls'), namespace='importer_automater')),
    path('forhandlere/', include(('forhandlere.urls', 'forhandlere'), namespace='forhandlere')),
    path('hent_produkt/', include('hent_produkt.urls')),
    path('greenfuels-noder/', include(('greenfuels_noder.urls', 'greenfuels_noder'), namespace='greenfuels_noder')),
    path('produkter/', include(('produkter.urls', 'produkter'), namespace='produkter')),
    path('', include('kontaktoss.urls')),
]
