from django.contrib import admin

from .models import (

    Stock,
    MouvementStock

)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):

    list_display = (

        'produit', 
        'quantite',
        'seuil_alerte',
        'derniere_mise_a_jour'

    )

    search_fields = (

        'produit__nom',

    )

    ordering = (

        'quantite',

    )


@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):

    list_display = (

        'stock',
        'type_mouvement',
        'quantite',
        'date_mouvement'

    )

    list_filter = (

        'type_mouvement',

    )

    ordering = (

        '-date_mouvement',

    )