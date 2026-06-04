from django.db import models
from produits.models import Produit
from django.conf import settings


class Panier(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    session_id = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def total_panier(self):
        return sum(item.total_item() for item in self.items.all())

    def __str__(self):
        return f"Panier #{self.id}"


class PanierItem(models.Model):

    panier = models.ForeignKey(
        Panier,
        on_delete=models.CASCADE,
        related_name='items'
    )

    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    quantite = models.PositiveIntegerField(default=1)

    def total_item(self):
        return self.produit.prix * self.quantite