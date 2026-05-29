from django.db import models


class Stock(models.Model):

    produit = models.OneToOneField(

        'produits.Produit',

        on_delete=models.CASCADE,

        related_name='stock_ecommerce'

    )

    quantite = models.PositiveIntegerField(
        default=0
    )

    seuil_alerte = models.PositiveIntegerField(
        default=5
    )

    derniere_mise_a_jour = models.DateTimeField(
        auto_now=True
    )

    def stock_faible(self):

        return self.quantite <= self.seuil_alerte

    def __str__(self):

        return self.produit.nom


class MouvementStock(models.Model):

    TYPES = (

        ('entree', 'Entrée'),

        ('sortie', 'Sortie'),

    )

    stock = models.ForeignKey(

        Stock,

        on_delete=models.CASCADE,

        related_name='mouvements'

    )

    type_mouvement = models.CharField(

        max_length=20,

        choices=TYPES

    )

    quantite = models.PositiveIntegerField()

    commentaire = models.TextField(
        blank=True,
        null=True
    )

    date_mouvement = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.type_mouvement} - {self.stock.produit.nom}"