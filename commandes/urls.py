from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.liste_commandes,
        name='liste_commandes'
    ),

]