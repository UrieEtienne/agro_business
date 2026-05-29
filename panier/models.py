from django.db import models
from produits.models import Produit


class Panier(models.Model):

    session_id = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def total_panier(self):

        total = 0

        for item in self.items.all():

            total += item.total_item()

        return total

    def __str__(self):

        return f"Panier {self.id}"


class PanierItem(models.Model):

    panier = models.ForeignKey(
        Panier,
        on_delete=models.CASCADE,
        related_name='items'
    )

    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE
    )

    quantite = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def total_item(self):

        return self.produit.prix * self.quantite

    def __str__(self):

        return self.produit.nom