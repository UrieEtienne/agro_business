from django.contrib import admin
from .models import Facture


@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):

    list_display = (

        'id',
        'client_nom',
        'produit',
        'quantite',
        'prix_unitaire',
        'statut',
        'date_creation'

    )

    list_filter = (

        'statut',

    )

    search_fields = (

        'client_nom',
        'telephone',
        'produit'

    )

    ordering = (

        '-date_creation',

    )