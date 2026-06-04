from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.liste_commandes,
        name='liste_commandes'
    ),
     path(
        'commander/<int:produit_id>/',
        views.creer_commande,
        name='creer_commande'
    ),

]