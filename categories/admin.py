from django.contrib import admin
from .models import Categorie, SousCategorie


# =========================
# CATEGORIE
# =========================
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'active',
        'created_at'
    )

    search_fields = (
        'nom',
    )

    list_filter = (
        'active',
    )

    prepopulated_fields = {
        'slug': ('nom',)
    }


# =========================
# SOUS CATEGORIE
# =========================
@admin.register(SousCategorie)
class SousCategorieAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'categorie',
        'active',
        'created_at'
    )

    search_fields = (
        'nom',
    )

    list_filter = (
        'active',
        'categorie'
    )

    prepopulated_fields = {
        'slug': ('nom',)
    }