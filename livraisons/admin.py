from django.contrib import admin
from .models import Livraison


@admin.register(Livraison)
class LivraisonAdmin(admin.ModelAdmin):

    list_display = (

        'client_nom',
        'produit',
        'chauffeur',
        'ville',
        'statut',
        'date_creation'

    )

    list_filter = (

        'statut',
        'ville',

    )

    search_fields = (

        'client_nom',
        'telephone',
        'produit',
        'chauffeur'

    )

    list_editable = (

        'statut',

    )

    ordering = (

        '-date_creation',

    )