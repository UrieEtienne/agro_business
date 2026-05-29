from django.contrib import admin
from .models import (
    Client,
    Commande,
    LigneCommande
)


# =========================
# LIGNE COMMANDE INLINE
# =========================

class LigneCommandeInline(admin.TabularInline):

    model = LigneCommande

    extra = 1


# =========================
# CLIENT ADMIN
# =========================

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'telephone',
        'email'
    )

    search_fields = (
        'nom',
        'telephone'
    )


# =========================
# COMMANDE ADMIN
# =========================

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):

    list_display = (
        'numero_commande',
        'client',
        'montant_total',
        'statut',
        'paiement',
        'date_commande'
    )

    list_filter = (
        'statut',
        'paiement'
    )

    search_fields = (
        'numero_commande',
        'client__nom'
    )

    inlines = [
        LigneCommandeInline
    ]