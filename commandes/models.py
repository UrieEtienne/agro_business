from django.db import models
from panier.models import Panier
from produits.models import Produit


class Commande(models.Model):

    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        related_name="commandes"
    )

    panier = models.OneToOneField(
        Panier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    quantite = models.PositiveIntegerField(default=1)

    nom_client = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()

    STATUTS = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('preparation', 'Préparation'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]

    statut = models.CharField(
        max_length=20,
        choices=STATUTS,
        default='en_attente'
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def montant_total(self):
        return self.panier.total_panier() if self.panier else 0