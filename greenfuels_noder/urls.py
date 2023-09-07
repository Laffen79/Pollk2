from django.urls import path, include
from . import views
from .views import (
    greenfuels_noder_view,
    add_greenfuelsnode,
    edit_greenfuelsnode,
    delete_greenfuelsnode,
)

app_name = 'greenfuels_noder'

urlpatterns = [
    path('', greenfuels_noder_view, name='greenfuels_noder'),
    path('add/', add_greenfuelsnode, name='add_greenfuelsnode'),
    path('edit/<int:id>/', edit_greenfuelsnode, name='edit_greenfuelsnode'),
    path('delete/<int:id>/', delete_greenfuelsnode, name='delete_greenfuelsnode'),
]