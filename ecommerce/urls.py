from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.accueil_shop,
        name='accueil_shop'
    ),

    path(
        'boutique/',
        views.boutique,
        name='boutique'
    ),

]