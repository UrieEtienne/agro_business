from django.db import models
from django.utils import timezone
import uuid


class Facture(models.Model):

    STATUTS = (

        ('en_attente', 'En attente'),

        ('payee', 'Payée'),

        ('annulee', 'Annulée'),

    )

    numero = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    client_nom = models.CharField(
        max_length=255
    )

    client_email = models.EmailField()

    telephone = models.CharField(
        max_length=30
    )

    adresse = models.TextField()

    produit = models.CharField(
        max_length=255
    )

    quantite = models.PositiveIntegerField()

    prix_unitaire = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    tva = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=18
    )

    qr_code = models.ImageField(
        upload_to='qr_codes/',
        blank=True,
        null=True
    )

    statut = models.CharField(
        max_length=30,
        choices=STATUTS,
        default='en_attente'
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.numero:

            annee = timezone.now().year

            uid = uuid.uuid4().hex[:6].upper()

            self.numero = f"FAC-{annee}-{uid}"

        super().save(*args, **kwargs)

    def sous_total(self):

        return self.quantite * self.prix_unitaire

    def montant_tva(self):

        return (
            self.sous_total() * self.tva
        ) / 100

    def total(self):

        return (
            self.sous_total() +
            self.montant_tva()
        )

    def __str__(self):

        return self.numero