from django.contrib import admin
from .models import Paiement


@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):

    list_display = (

        'reference',
        'client_nom',
        'telephone',
        'montant',
        'methode',
        'statut',
        'date_creation'

    )

    list_filter = (

        'methode',
        'statut'

    )

    search_fields = (

        'reference',
        'telephone',
        'client_nom'

    )

    ordering = (

        '-date_creation',

    )