from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.panier_detail,
        name='panier_detail'
    ),

    path(
        'ajouter/<int:produit_id>/',
        views.ajouter_panier,
        name='ajouter_panier'
    ),

    path(
        'supprimer/<int:item_id>/',
        views.supprimer_panier,
        name='supprimer_panier'
    ),

    path(
        'diminuer/<int:item_id>/',
        views.diminuer_quantite,
        name='diminuer_quantite'
    ),

]