from django.urls import path
from .views import (
    liste_factures,
    facture_pdf
)

urlpatterns = [

    path(
        '',
        liste_factures,
        name='liste_factures'
    ),

    path(
        'pdf/<int:facture_id>/',
        facture_pdf,
        name='facture_pdf'
    ),

 path('facture/pdf/<int:id>/', facture_pdf, name='facture_pdf'),
]