from django.contrib import admin
from .models import Produit, Categorie


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug')
    search_fields = ('nom', 'slug')


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'sku',
        'categorie',
        'prix',
        'stock',
        'promotion',
        'disponible',
    )

    list_filter = (
        'categorie',
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

    # ⭐ IMPORTANT
    fields = (
        'nom',
        'sku',
        'categorie',
        'image',
        'prix',
        'ancien_prix',
        'promotion',
        'description',
        'stock',
        'disponible',
    )