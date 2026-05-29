from django.urls import path

from .views import (
    home,
    dashboard,
    publicites,
    temoignages
)

urlpatterns = [
    path('', home, name='home'),

    path('dashboard/', dashboard, name='dashboard'),

    path('publicites/', publicites, name='publicites'),

    path('temoignages/', temoignages, name='temoignages'),
]