from django.contrib import admin
from .models import Commande


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom_client',
        'get_produit',
        'get_quantite',
    )

    def get_produit(self, obj):
        return obj.produit.nom
    get_produit.short_description = "Produit"

    def get_quantite(self, obj):
        return obj.quantite
    get_quantite.short_description = "Quantité"