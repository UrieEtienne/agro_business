from django.urls import path

from .views import (

    liste_stocks,
    alertes_stock,
    mouvements_stock

)

urlpatterns = [

    path(
        '',
        liste_stocks,
        name='liste_stocks'
    ),

    path(
        'alertes/',
        alertes_stock,
        name='alertes_stock'
    ),

    path(
        'mouvements/',
        mouvements_stock,
        name='mouvements_stock'
    ),

]