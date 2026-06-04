from django.db import models
import uuid

class Livraison(models.Model):

    STATUTS = (
        ('en_attente', 'En attente'),
        ('en_preparation', 'En préparation'),
        ('expediee', 'Expédiée'),
        ('en_livraison', 'En livraison'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    )

    client_nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=30)

    adresse = models.TextField()
    ville = models.CharField(max_length=100)

    #  GPS
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    code_suivi = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )

    # CODE SUIVI AUTOMATIQUE
    code_suivi = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    # SAVE AUTOMATIQUE
    def save(self, *args, **kwargs):

        if not self.code_suivi:
            self.code_suivi = str(uuid.uuid4()).replace('-', '')[:10].upper()

        super().save(*args, **kwargs)

    chauffeur = models.CharField(max_length=255)

    produit = models.CharField(max_length=255)
    quantite = models.PositiveIntegerField()

    statut = models.CharField(
        max_length=20,
        choices=STATUTS,
        default='en_attente'
    )

    date_creation = models.DateTimeField(auto_now_add=True)
    date_livraison = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.client_nom} - {self.produit}"