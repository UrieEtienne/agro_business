from django.contrib import admin
from .models import Produit


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'sku',
        'prix',
        'stock',
        'promotion',
        'disponible',
    )

    list_filter = (
        'promotion',
        'disponible',
    )

    search_fields = (
        'nom',
        'sku',
    )

    list_editable = (
        'prix',
        'stock',
        'promotion',
        'disponible',
    )